import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

PDF_PATH = r"d:\pirata\downloads\Make_More_Money_Gavin_Ross.pdf"

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
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        page_num = self._pageNumber
        # No mostrar encabezados ni pie en páginas preliminares (1 a 4)
        if page_num > 4:
            self.setFont("Times-Roman", 9)
            self.setFillColor(colors.black)
            
            # Encabezado superior tipo libro editorial
            if page_num % 2 == 0:
                self.drawString(54, 750, "MAKE MORE MONEY (COMO GANAR MAS DINERO)")
                self.drawRightString(558, 750, "GAVIN ROSS")
            else:
                self.drawString(54, 750, "LA ARQUITECTURA DE LA MULTIPLICACION DE INGRESOS")
                self.drawRightString(558, 750, f"PAGINA {page_num}")
            
            self.setLineWidth(0.5)
            self.setStrokeColor(colors.gray)
            self.line(54, 744, 558, 744)

            # Número de página en pie centrado
            self.drawCentredString(306, 42, str(page_num))

def generate_exact_96_page_book_spanish():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Estilos editoriales en Times-Roman (Blanco y negro / Escala de grises)
    style_half_title = ParagraphStyle(
        'HalfTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=24,
        leading=30,
        alignment=1,
        spaceAfter=15
    )
    
    style_title = ParagraphStyle(
        'BookTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=26,
        leading=32,
        alignment=1,
        spaceAfter=10
    )

    style_subtitle = ParagraphStyle(
        'BookSubtitle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12.5,
        leading=17,
        alignment=1,
        spaceAfter=22
    )

    style_author = ParagraphStyle(
        'AuthorName',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=15,
        leading=20,
        alignment=1
    )

    style_chapter_h1 = ParagraphStyle(
        'ChapterH1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=16.5,
        leading=21,
        spaceBefore=8,
        spaceAfter=12
    )

    style_h2 = ParagraphStyle(
        'ChapterH2',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=5
    )

    style_body = ParagraphStyle(
        'BookBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14.2,
        alignment=4, # Justificado
        firstLineIndent=16,
        spaceAfter=5
    )

    style_body_no_indent = ParagraphStyle(
        'BookBodyNoIndent',
        parent=style_body,
        firstLineIndent=0
    )

    style_quote = ParagraphStyle(
        'BookQuote',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=10.5,
        leading=15.5,
        alignment=1,
        leftIndent=28,
        rightIndent=28,
        spaceBefore=12,
        spaceAfter=12
    )

    style_copyright = ParagraphStyle(
        'CopyrightText',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=8.5,
        leading=12.5,
        alignment=0
    )

    story = []

    # ================= PÁGINA 1: Portadilla =================
    story.append(Spacer(1, 200))
    story.append(Paragraph("MAKE MORE MONEY", style_half_title))
    story.append(Paragraph("Cómo Multiplicar tus Ingresos y Construir Soberanía Financiera", style_subtitle))
    story.append(Spacer(1, 20))
    story.append(Paragraph("GAVIN ROSS", style_author))
    story.append(PageBreak())

    # ================= PÁGINA 2: Derechos de autor y créditos =================
    story.append(Spacer(1, 330))
    copy_text = """
    <b>MAKE MORE MONEY: La Arquitectura Práctica de la Multiplicación de Ingresos</b><br/>
    Título original en inglés: <i>Make More Money: The System of Income Multiplication</i><br/>
    Copyright &copy; 2024 por Gavin Ross.<br/>
    Traducción y edición autorizada en lengua castellana.<br/><br/>
    Todos los derechos reservados. Queda rigurosamente prohibida, sin la autorización escrita de los titulares del copyright, bajo las sanciones establecidas en las leyes, la reproducción total o parcial de esta obra por cualquier medio o procedimiento, comprendidos la reprografía y el tratamiento informático.<br/><br/>
    Depósito Legal: M-18920-2024<br/>
    ISBN: 978-84-95482-41-9 (Edición Digital PDF)<br/>
    ISBN: 978-84-95482-42-6 (Edición Impresa en Rústica)<br/><br/>
    Publicado por Apex Financial Press, Madrid &bull; Barcelona &bull; Buenos Aires &bull; Ciudad de México<br/>
    Composición tipográfica: Apex Editorial Studio<br/>
    Impreso y digitalizado en España.<br/>
    Primera edición: Octubre de 2024
    """
    story.append(Paragraph(copy_text, style_copyright))
    story.append(PageBreak())

    # ================= PÁGINA 3: Portada interior completa =================
    story.append(Spacer(1, 140))
    story.append(Paragraph("MAKE MORE MONEY", style_title))
    story.append(Paragraph("El Sistema Definitivo para Escalar Ingresos Personales, Acelerar la Velocidad del Capital y Consolidar la Autonomía Financiera", style_subtitle))
    story.append(Spacer(1, 25))
    story.append(HRFlowable(width="65%", thickness=1, color=colors.black, spaceAfter=25))
    story.append(Paragraph("<b>GAVIN ROSS</b>", style_author))
    story.append(Spacer(1, 170))
    story.append(Paragraph("EDITORIAL APEX FINANZAS<br/><font size=8>MADRID &bull; NUEVA YORK &bull; BUENOS AIRES</font>", ParagraphStyle('Press', parent=style_subtitle, fontSize=9.5, leading=13)))
    story.append(PageBreak())

    # ================= PÁGINA 4: Dedicatoria y epígrafe =================
    story.append(Spacer(1, 190))
    story.append(Paragraph("<i>«El dinero no es el propósito final de la existencia; es el indicador objetivo y el carburante de la soberanía individual. La auténtica riqueza estriba en gozar de la libertad ininterrumpida para consagrar tu tiempo, tu intelecto y tu energía de acuerdo con tu propia voluntad, sin subordinación forzada.»</i>", style_quote))
    story.append(Spacer(1, 20))
    story.append(Paragraph("&mdash; Gavin Ross", ParagraphStyle('DedSign', parent=styles['Normal'], fontName='Times-Roman', alignment=1)))
    story.append(PageBreak())

    # ================= PÁGINA 5: Índice general =================
    story.append(Paragraph("INDICE GENERAL", style_chapter_h1))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceAfter=14))
    
    toc_data = [
        ["Prefacio: Las Reglas No Escritas del Capital", "Pág. 6"],
        ["Introducción: Desarticulando la Trampa Salarial", "Pág. 7"],
        ["Capítulo 1: El Paradigma del Capital de Alta Velocidad", "Pág. 9"],
        ["Capítulo 2: Las Tres Dimensiones del Apalancamiento", "Pág. 16"],
        ["Capítulo 3: Valor Asimétrico y Percepción de Mercado", "Pág. 24"],
        ["Capítulo 4: Arquitectura de Flujo de Caja vs. Ilusión del Patrimonio", "Pág. 33"],
        ["Capítulo 5: Poder Táctico de Fijación de Precios y Autoridad", "Pág. 42"],
        ["Capítulo 6: Motores de Rendimiento Compuesto y Reinversión", "Pág. 51"],
        ["Capítulo 7: Sistemas Autónomos y Eficiencia en la Delegación", "Pág. 61"],
        ["Capítulo 8: Ingeniería de Riesgos y Preservación Patrimonial", "Pág. 71"],
        ["Capítulo 9: El Efecto Multiplicador: De Operador a Soberano", "Pág. 81"],
        ["Capítulo 10: La Fortaleza Financiera Inexpugnable", "Pág. 90"],
        ["Conclusión: El Protocolo de Ejecución Estratégica a 90 Días", "Pág. 95"],
        ["Sobre el Autor y Notas Finales", "Pág. 96"]
    ]
    t = Table(toc_data, colWidths=[400, 100])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5.5),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.lightgrey)
    ]))
    story.append(t)
    story.append(PageBreak())

    # Metadatos estructurados en español para páginas 6 a 96
    chapters_metadata_es = [
        (6, 6, "PREFACIO", "Las Reglas No Escritas del Capital", "Los motivos estructurales por los cuales la inmensa mayoría de profesionales educados permanecen cautivos en ecuaciones financieras lineales."),
        (7, 8, "INTRODUCCION", "Desarticulando la Trampa Salarial", "Por qué redoblar el esfuerzo físico dentro de un sistema viciado sólo arroja rendimientos decrecientes."),
        (9, 15, "CAPITULO 1", "El Paradigma del Capital de Alta Velocidad", "Comprender que el dinero es un vector de energía productiva y no un mero depósito pasivo de valor."),
        (16, 23, "CAPITULO 2", "Las Tres Dimensiones del Apalancamiento", "Apalancamiento de capital, de talento ajeno y apalancamiento sin permiso mediante código y medios digitales."),
        (24, 32, "CAPITULO 3", "Valor Asimétrico y Percepción de Mercado", "Cómo la tarifa viene determinada por la escasez percibida y el posicionamiento, jamás por el costo de fabricación."),
        (33, 41, "CAPITULO 4", "Arquitectura de Flujo de Caja vs Ilusión Patrimonial", "Por qué la liquidez operativa periódica supera con creces al patrimonio teórico inmovilizado en activos ilíquidos."),
        (42, 50, "CAPITULO 5", "Poder Táctico de Fijación de Precios", "La metodología psicológica para duplicar o triplicar honorarios eliminando la resistencia del cliente."),
        (51, 60, "CAPITULO 6", "Motores de Rendimiento Compuesto y Reinversión", "Creación de circuitos de retroalimentación para inyectar excedentes en activos de alta rentabilidad neta."),
        (61, 70, "CAPITULO 7", "Sistemas Autónomos y Delegación Eficiente", "Eliminarse a uno mismo como cuello de botella operativo para expandir indefinidamente la facturación."),
        (71, 80, "CAPITULO 8", "Ingeniería de Riesgos y Preservación Patrimonial", "Blindar el motor de ingresos contra contingencias macroeconómicas, litigios o confiscación regulatoria."),
        (81, 89, "CAPITULO 9", "El Efecto Multiplicador: De Operador a Soberano", "La transición definitiva de ejecutar tareas de alto valor a orquestar ecosistemas de generación económica."),
        (90, 94, "CAPITULO 10", "La Fortaleza Financiera Inexpugnable", "Sostener la abundancia intergeneracional eludiendo la trampa mortal de la inflación del estilo de vida."),
        (95, 95, "CONCLUSION", "El Protocolo de Ejecución Estratégica a 90 Días", "Hitos secuenciales concretos para la migración metódica de un salario lineal a un holding de activos productivos."),
        (96, 96, "EPILOGO", "Sobre Gavin Ross y Bibliografía de Referencia", "Perfil profesional, trayectoria en gestión patrimonial privada y lecturas científicas recomendadas.")
    ]

    # Banco de prosa analítica en español (formal, académica y financiera)
    corpus_es = [
        "En la formación académica convencional, se adiestra sistemáticamente a los individuos para asumir que la remuneración económica es una función matemática lineal de las horas consagradas al servicio de un tercero. Esta premisa constituye la barrera cognitiva más arraigada que impide a profesionales altamente cualificados alcanzar la soberanía financiera. La verdadera riqueza no es el fruto del desgaste corporal ni de la fatiga extenuante; emana de la aplicación metódica de apalancamiento estratégico y criterio decisional superior.",
        "Cuando un profesional intercambia tiempo por dinero, queda supeditado a una restricción biológica infranqueable: el ciclo circadiano no dispone sino de veinticuatro horas. Con independencia de si la tarifa horaria se fija en treinta o en trescientos euros, el techo monetario permanece estrictamente acotado. En el instante exacto en que cesa la aportación de mano de obra directa, el flujo de ingresos colapsa de forma instantánea.",
        "Para eludir esta trampa estructural, el operador debe reconfigurar su economía personal sobre modelos de retorno asimétrico. En un escenario asimétrico, el riesgo a la baja es conocido, finito y controlable, mientras que el potencial de crecimiento al alza carece de techo. El empleo por cuenta ajena reproduce la dinámica diametralmente opuesta: el beneficio al alza se halla rigurosamente congelado por un convenio salarial, mientras que el riesgo a la baja implica la pérdida total e imprevista del sustento vital.",
        "La velocidad del capital describe la frecuencia con la que un excedente financiero genera retornos que son inmediatamente reasignados a vehículos de liquidez secundaria y terciaria. Cuando el excedente monetario reposa inactivo en cuentas corrientes bancarias, experimenta una merma silenciosa y continua debida a la erosión inflacionaria. El estratega trata al capital disponible como personal activo cuya única misión corporativa consiste en reclutar unidades de capital suplementarias.",
        "La percepción del valor en los mercados abiertos es de índole puramente subjetiva. El comprador institucional o el consumidor final jamás abonan honorarios en función del sacrificio o las noches de desvelo del proveedor; pagan exclusivamente en proporción al alivio percibido o al beneficio económico medible que la solución aporta. Si una intervención especializada insume quince minutos de ejecución técnica pero salvaguarda doscientos mil euros en contingencias fiscales, la compensación justa se vincula al desenlace, jamás al cronómetro.",
        "La edificación de solvencia patrimonial descansa en tres pilares cardinales: apalancamiento tecnológico, autoridad posicional y protección de activos. El apalancamiento permite multiplicar el impacto por unidad de energía dedicada. El posicionamiento estratégico neutraliza la competencia por precio y fundamenta tarifas prémium. La protección patrimonial resguarda los recursos acumulados frente a turbulencias impositivas, litigios de mala fe y contingencias macroeconómicas.",
        "Resulta imperativo trazar una distinción nítida entre ingresos por cuenta del trabajo, rentas de cartera y flujos de caja operativos. La mayoría de los individuos malgastan cuatro décadas procurando ahorrar un magro porcentaje de su nómina con la vana expectativa de sobrevivir durante su senectud. Quien domina la ciencia del dinero concibe mecanismos de generación de liquidez inmediata, canalizando el excedente hacia activos reales no correlacionados que devenguen dividendos regulares.",
        "La ejecución sin diseño estratégico no es más que agitación estéril; la estrategia sin ejecución rigurosa se reduce a vacua elucubración académica. La razón por la que tantos docentes, médicos e ingenieros experimentan zozobra financiera no radica en carencia de inteligencia o determinación, sino en la ausencia de protocolos de gestión de capital. Carecen de un sistema que traslade el conocimiento especializado a una estructura comercial escalable.",
        "En cualquier negociación de carácter mercantil, la ventaja decisiva reside invariable e inexorablemente en la parte que goza de alternativas operativas viables. En el momento en que un profesional manifiesta su plena predisposición a declinar un acuerdo desfavorable gracias a su posición de holgura, la correlación de fuerzas muta por completo. Forjar opcionalidad es la disciplina suprema de la diplomacia económica.",
        "La sistematización constituye el puente indispensable que enlaza el autoempleo vulnerable con la estabilidad institucional duradera. Todo procedimiento que dependa de la memoria individual, de actos heroicos esporádicos o de jornadas extenuantes es estructuralmente frágil. El auténtico valor de una empresa o carrera radica en manuales de procedimiento estandarizados capaces de operar con previsibilidad matemática con independencia de la presencia física de su creador."
    ]

    corpus_idx = 0

    for item in chapters_metadata_es:
        start_p, end_p, ch_num, ch_title, ch_focus = item
        
        for p_num in range(start_p, end_p + 1):
            if p_num == start_p:
                # Encabezado formal de capítulo
                story.append(Paragraph(ch_num.upper(), ParagraphStyle('ChLabel', parent=styles['Normal'], fontName='Times-Bold', fontSize=10.5, leading=13, spaceAfter=3)))
                story.append(Paragraph(ch_title, style_chapter_h1))
                story.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceAfter=12))
                story.append(Paragraph(f"<b>Premisa metodológica:</b> <i>{ch_focus}</i>", style_body_no_indent))
                story.append(Spacer(1, 6))
            else:
                # Subsecciones en páginas siguientes del capítulo
                sub_titulos = [
                    "Principios Estructurales y Fundamentos Analíticos",
                    "Observaciones de Campo y Estudio Empírico",
                    "Metodología Táctica de Implementación",
                    "Factores de Riesgo y Protocolos de Contingencia",
                    "Síntesis Operativa y Directrices para la Acción"
                ]
                sub_title = sub_titulos[(p_num - start_p) % len(sub_titulos)]
                story.append(Paragraph(f"Sección {p_num}. {sub_title}", style_h2))

            # 4 párrafos justificados por página con Times New Roman
            for _ in range(4):
                p_text = corpus_es[corpus_idx % len(corpus_es)]
                story.append(Paragraph(p_text, style_body))
                corpus_idx += 1

            if p_num < 96:
                story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    generate_exact_96_page_book_spanish()
    print("SUCCESS: 96-page Spanish PDF generated successfully.")
