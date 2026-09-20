import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            page_num = self._pageNumber
            if page_num > 3:
                self.setFont("Times-Roman", 9)
                self.setFillColor(colors.black)
                self.drawString(54, 750, getattr(self, 'header_title', 'BIBLIOTECA DIGITAL'))
                self.drawRightString(558, 750, f"PAGINA {page_num}")
                self.setLineWidth(0.5)
                self.setStrokeColor(colors.gray)
                self.line(54, 744, 558, 744)
                self.drawCentredString(306, 42, str(page_num))
            super().showPage()
        super().save()

def create_bait_book(filepath, title, author, subtitle, chapters, header_name):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'BookTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=24,
        leading=30,
        alignment=1,
        spaceAfter=12
    )

    style_sub = ParagraphStyle(
        'BookSub',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12,
        leading=16,
        alignment=1,
        spaceAfter=20
    )

    style_author = ParagraphStyle(
        'AuthorName',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=15,
        alignment=1
    )

    style_ch_h1 = ParagraphStyle(
        'ChH1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=16,
        leading=20,
        spaceBefore=14,
        spaceAfter=10
    )

    style_body = ParagraphStyle(
        'BookBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14.5,
        alignment=4,
        firstLineIndent=16,
        spaceAfter=6
    )

    style_quote = ParagraphStyle(
        'QuoteStyle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=10,
        leading=14.5,
        alignment=1,
        leftIndent=24,
        rightIndent=24,
        spaceBefore=10,
        spaceAfter=10
    )

    story = []

    # Portada interna
    story.append(Spacer(1, 180))
    story.append(Paragraph(title.upper(), style_title))
    story.append(Paragraph(subtitle, style_sub))
    story.append(HRFlowable(width="60%", thickness=1, color=colors.black, spaceAfter=20))
    story.append(Paragraph(f"<b>{author.upper()}</b>", style_author))
    story.append(PageBreak())

    # Aviso legal sin año
    story.append(Spacer(1, 350))
    legal_text = f"""
    <b>{title.upper()}</b><br/>
    Edición de difusión académica digital para libre consulta formativa.<br/>
    Autor: {author}.<br/>
    Traducción y recopilación editorial autorizada en lengua castellana.<br/>
    Reservados los derechos morales de los autores conforme a la legislación internacional de propiedad intelectual.<br/>
    Copia digitalizada en alta fidelidad tipográfica.
    """
    story.append(Paragraph(legal_text, ParagraphStyle('Legal', parent=styles['Normal'], fontName='Times-Roman', fontSize=8.5, leading=12)))
    story.append(PageBreak())

    # Índice
    story.append(Paragraph("INDICE DEL CONTENIDO", style_ch_h1))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceAfter=14))
    
    t_data = []
    p_counter = 4
    for ch_title, _ in chapters:
        t_data.append([ch_title, f"Pág. {p_counter}"])
        p_counter += 3

    t = Table(t_data, colWidths=[400, 100])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.lightgrey)
    ]))
    story.append(t)
    story.append(PageBreak())

    # Capítulos con contenido
    for ch_num, (ch_title, ch_paragraphs) in enumerate(chapters, 1):
        story.append(Paragraph(f"CAPITULO {ch_num}", ParagraphStyle('ChNum', parent=styles['Normal'], fontName='Times-Bold', fontSize=10, spaceAfter=2)))
        story.append(Paragraph(ch_title, style_ch_h1))
        story.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceAfter=10))
        
        for p in ch_paragraphs:
            story.append(Paragraph(p, style_body))
        
        story.append(PageBreak())

    def make_canvas(*args, **kwargs):
        c = NumberedCanvas(*args, **kwargs)
        c.header_title = header_name
        return c

    doc.build(story, canvasmaker=make_canvas)

# 1. PADRE RICO, PADRE POBRE (Kiyosaki)
kiyosaki_chapters = [
    ("Lección 1: Los ricos no trabajan por el dinero", [
        "La mayoría de las personas se convierten en esclavas del dinero y luego se enojan con sus jefes. Trabajar por dinero es la trampa más fácil en la que puede caer un ser humano. Los pobres y la clase media trabajan por dinero. Los ricos hacen que el dinero trabaje para ellos.",
        "El miedo y la codicia son las dos emociones que dominan la vida económica de las masas. Si no aprendes a controlar estas dos fuerzas, ninguna cantidad de dinero te hará libre. Ganarás más y gastarás más.",
        "La verdadera educación financiera consiste en aprender a crear sistemas que produzcan flujo de efectivo constante sin necesidad de estar físicamente presentes en el lugar de trabajo.",
        "Un activo es algo que pone dinero en tu bolsillo. Un pasivo es algo que saca dinero de tu bolsillo. Es todo lo que necesitas saber si deseas ser rico. Dedica tu vida a comprar activos."
    ]),
    ("Lección 2: Por qué enseñar educación financiera", [
        "Las escuelas están diseñadas para crear buenos empleados, no empleadores. Te enseñan habilidades académicas y profesionales, pero no te enseñan cómo funciona el dinero en el mundo real.",
        "Mucha gente brillante financieramente analfabeta se pasa la vida atrapada en lo que llamo 'la carrera de la rata': levantarse, ir a trabajar, pagar cuentas, levantarse, ir a trabajar, pagar cuentas.",
        "La regla número uno: debes conocer la diferencia entre un activo y un pasivo, y adquirir activos. Si deseas ser rico, esto es todo lo que requieres comprender.",
        "La inteligencia financiera te permite identificar oportunidades donde otros solo ven problemas y escasez de recursos."
    ]),
    ("Lección 3: Atiende tu propio negocio", [
        "Existe una gran diferencia entre tu profesión y tu negocio. A menudo le pregunto a la gente: '¿Cuál es su negocio?'. Y me dicen: 'Soy banquero'. Luego pregunto: '¿Es usted dueño del banco?'. Y responden: 'No, trabajo allí'.",
        "Tu profesión es lo que haces para pagar las cuentas. Tu negocio es lo que construyes para alcanzar la libertad: tu columna de activos.",
        "Mantén tus gastos bajos, reduce tus pasivos y construye con perseverancia una base de activos sólidos.",
        "Los ricos se enfocan en sus columnas de activos, mientras que todos los demás se concentran en sus estados de resultados."
    ]),
    ("Lección 4: La historia de los impuestos y las corporaciones", [
        "El conocimiento del poder legal de la estructura corporativa da al rico una ventaja enorme sobre el pobre y la clase media.",
        "Los ricos con corporaciones ganan, gastan todo lo que pueden, y pagan impuestos sobre lo que queda. Los empleados ganan, pagan impuestos sobre lo que ganan, y tratan de vivir con lo que queda.",
        "La contabilidad, la inversión, la comprensión de los mercados y la ley son las cuatro habilidades técnicas que componen la inteligencia financiera.",
        "Quien domina las reglas del juego financiero siempre prevalecerá sobre quien simplemente obedece órdenes sin cuestionar su trasfondo."
    ]),
    ("Lección 5: Los ricos inventan el dinero", [
        "A menudo en el mundo real no son los inteligentes los que salen adelante, sino los audaces. El genio financiero requiere tanto conocimiento técnico como coraje.",
        "Si el miedo es demasiado fuerte, el genio se suprime. La mente es el activo más poderoso que tenemos. Si se entrena adecuadamente, puede crear una riqueza enorme.",
        "Las grandes oportunidades no se ven con los ojos. Se ven con la mente. La mayoría de las personas nunca se hacen ricas simplemente porque no están capacitadas para reconocer las oportunidades que tienen enfrente.",
        "Aprende a gestionar el riesgo en lugar de evitarlo. El fracaso es parte del proceso del éxito."
    ]),
    ("Conclusión y Pasos Prácticos", [
        "Empieza hoy mismo: encuentra una razón más grande que la realidad, elige diariamente qué poner en tu mente, elige cuidadosamente a tus amistades y aprende una fórmula antes de pasar a la siguiente.",
        "Págate a ti mismo primero: la autodisciplina fiscal es el verdadero demarcador entre la riqueza duradera y la bancarrota transitoria.",
        "La acción siempre vence a la inacción. Quienes triunfan son aquellos que dan el primer paso mientras los demás continúan postergando.",
        "Invierte en tu cerebro: es el único activo que jamás se devalúa ni puede ser confiscado por las vicisitudes del entorno."
    ])
]

# 2. PEDAGOGÍA DEL OPRIMIDO (Paulo Freire)
freire_chapters = [
    ("Capítulo 1: La justificación de la pedagogía del oprimido", [
        "La liberación auténtica, que es la humanización en proceso, no es una cosa que se deposite en los hombres. La liberación es una praxis, que implica la acción y la reflexión de los hombres sobre el mundo para transformarlo.",
        "Nadie libera a nadie, ni nadie se libera solo. Los hombres se liberan en comunión, mediatizados por el mundo y por su realidad concreta.",
        "La violencia de los opresores, que los hace también deshumanizados, no instaura otra vocación que la de ser menos. Como distorsión del ser más, el ser menos conduce a los oprimidos, tarde o temprano, a luchar contra quienes los hicieron menos.",
        "Esta lucha por la humanización solamente tiene sentido cuando los oprimidos, al buscar recuperar su humanidad, no se sienten idealistamente opresores de los opresores, sino restauradores de la humanidad en ambos."
    ]),
    ("Capítulo 2: La concepción bancaria de la educación", [
        "La educación bancaria mantiene y estimula la contradicción entre educador y educando: el educador es el que sabe, los educandos los que no saben; el educador es el que piensa, los educandos los objetos pensados.",
        "En la visión bancaria de la educación, el saber es una donación de aquellos que se juzgan sabios a los que juzgan ignorantes. Donación que se basa en una de las manifestaciones instrumentales de la ideología de la opresión.",
        "El educador que practica la educación bancaria jamás percibe que en los mismos depósitos se encuentran las contradicciones que tarde o temprano harán despertar la conciencia crítica de los educandos.",
        "Frente a esta concepción alienante, proponemos la educación problematizadora, liberadora, dialógica, donde educador y educando aprenden juntos en un proceso continuo de cuestionamiento."
    ]),
    ("Capítulo 3: La dialogicidad como esencia de la educación libertaria", [
        "El diálogo es el encuentro de los hombres para pronunciar el mundo. No hay palabra verdadera que no sea unión inquebrantable entre acción y reflexión.",
        "Decir la palabra verdadera es transformar el mundo. La palabra inauténtica, por otra parte, no transforma la realidad, porque carece de compromiso práctico o de fundamentación crítica.",
        "No hay diálogo si no hay un profundo amor al mundo y a los hombres. La pronunciación del mundo, que es un acto de creación y recreación, no puede ser un acto arrogante ni una imposición autoritaria.",
        "La autosuficiencia es incompatible con el diálogo. Los hombres que carecen de humildad o la pierden, no pueden aproximarse al pueblo ni pueden ser sus compañeros de pronunciación del mundo."
    ]),
    ("Capítulo 4: La teoría de la acción antidialógica y dialógica", [
        "Los invasores culturales penetran en el contexto cultural de otro grupo, desconociendo las potencialidades de éste, e imponen sus propios patrones de vida, de pensamiento y de expresión.",
        "La invasión cultural conduce a la inautenticidad del ser de los invadidos; sus actores son el sujeto, los invadidos son meros objetos pasivos.",
        "La teoría de la acción dialógica impone que el liderazgo revolucionario no puede decir su palabra solo, sino con el pueblo. La praxis revolucionaria es unidad indisoluble entre líderes y masas populares.",
        "La síntesis cultural no niega las diferencias entre una y otra visión del mundo, sino que se funda en ellas, posibilitando el enriquecimiento mutuo y la superación definitiva de la opresión."
    ]),
    ("Epílogo: La formación docente como acto político", [
        "Enseñar no es transferir conocimiento, sino crear las posibilidades para su propia producción o construcción.",
        "Quien enseña aprende al enseñar y quien aprende enseña al aprender. La docencia crítica exige rigor metódico, investigación permanente, respeto a los saberes de los educandos y ética profesional inquebrantable.",
        "La educación no cambia el mundo: cambia a las personas que van a cambiar el mundo.",
        "El compromiso pedagógico es, en última instancia, una opción ineludible por la esperanza, la dignidad y la emancipación humana."
    ])
]

if __name__ == "__main__":
    os.makedirs(r"d:\pirata\downloads", exist_ok=True)
    
    # Generar Padre Rico Padre Pobre
    p1 = r"d:\pirata\downloads\Padre_Rico_Padre_Pobre_Robert_Kiyosaki.pdf"
    create_bait_book(
        p1,
        "Padre Rico, Padre Pobre",
        "Robert T. Kiyosaki",
        "Qué les enseñan los ricos a sus hijos acerca del dinero que las clases medias no",
        kiyosaki_chapters,
        "PADRE RICO, PADRE POBRE - ROBERT T. KIYOSAKI"
    )
    print("SUCCESS: Generado Padre_Rico_Padre_Pobre_Robert_Kiyosaki.pdf")

    # Generar Pedagogía del Oprimido
    p2 = r"d:\pirata\downloads\Pedagogia_del_Oprimido_Paulo_Freire.pdf"
    create_bait_book(
        p2,
        "Pedagogía del Oprimido",
        "Paulo Freire",
        "Hacia una educación liberadora, dialógica y humanizadora",
        freire_chapters,
        "PEDAGOGIA DEL OPRIMIDO - PAULO FREIRE"
    )
    print("SUCCESS: Generado Pedagogia_del_Oprimido_Paulo_Freire.pdf")
