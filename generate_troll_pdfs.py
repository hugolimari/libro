import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_troll_index_pdf(filepath, title, author, subtitle, index_items):
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
        'TrollTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=24,
        leading=30,
        alignment=1,
        spaceAfter=12
    )

    style_sub = ParagraphStyle(
        'TrollSub',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12,
        leading=16,
        alignment=1,
        spaceAfter=20
    )

    style_author = ParagraphStyle(
        'TrollAuthor',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=15,
        alignment=1
    )

    style_index_heading = ParagraphStyle(
        'TrollIndexHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=18,
        leading=22,
        spaceBefore=20,
        spaceAfter=15
    )

    style_index_item = ParagraphStyle(
        'TrollItem',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11.5,
        leading=19,
        leftIndent=15,
        spaceAfter=4
    )

    story = []

    # Página 1: Portada simple y sobria
    story.append(Spacer(1, 200))
    story.append(Paragraph(title.upper(), style_title))
    story.append(Paragraph(subtitle, style_sub))
    story.append(HRFlowable(width="60%", thickness=1, color=colors.black, spaceAfter=20))
    story.append(Paragraph(f"<b>{author.upper()}</b>", style_author))
    story.append(PageBreak())

    # Página 2: Solo el índice crudo y nada más
    story.append(Paragraph("INDICE GENERAL", style_index_heading))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.black, spaceAfter=18))

    for item in index_items:
        story.append(Paragraph(item, style_index_item))

    doc.build(story)
    print(f"SUCCESS: Generado troll PDF en {filepath}")

if __name__ == "__main__":
    os.makedirs(r"d:\pirata\downloads", exist_ok=True)

    # 1. SAMPIERI - METODOLOGÍA DE LA INVESTIGACIÓN (Bait supremo para docentes)
    sampieri_index = [
        "1. Los enfoques cuantitativo y cualitativo en la investigación científica",
        "2. Origen de las investigaciones cuantitativas, cualitativas o mixtas",
        "3. Planteamiento cuantitativo del problema de investigación",
        "4. Desarrollo de la perspectiva teórica: revisión de la literatura y construcción del marco teórico",
        "5. Definición del alcance de la investigación: exploratorio, descriptivo, correlacional o explicativo",
        "6. Formulación de hipótesis y operacionalización de variables",
        "7. Concepción o elección del diseño de investigación: experimental y no experimental",
        "8. Selección y delimitación de la muestra probabilística y no probabilística",
        "9. Recolección de datos cuantitativos: instrumentos y medición",
        "10. Análisis estadístico de los datos: pruebas paramétricas y no paramétricas",
        "11. El inicio del proceso cualitativo: inmersión inicial en el campo",
        "12. Recolección y análisis de datos cualitativos",
        "13. Diseños del proceso de investigación cualitativa: teoría fundamentada y fenomenología",
        "14. Los métodos mixtos y triangulación metodológica",
        "15. Elaboración del reporte de resultados para publicación y tesis de grado"
    ]
    create_troll_index_pdf(
        r"d:\pirata\downloads\Metodologia_Investigacion_Sampieri.pdf",
        "Metodología de la Investigación",
        "Roberto Hernández Sampieri",
        "Manual de referencia para el diseño de tesis y proyectos científicos",
        sampieri_index
    )

    # 2. HÁBITOS ATÓMICOS - JAMES CLEAR
    clear_index = [
        "1. El sorprendente poder de los diminutos hábitos atómicos",
        "2. La manera en que tus hábitos moldean tu identidad (y viceversa)",
        "3. Cómo construir mejores hábitos en cuatro sencillos pasos",
        "4. La 1ª Ley: Hacerlo obvio (Diseño de entornos y señales)",
        "5. La 2ª Ley: Hacerlo atractivo (La tentación y el condicionamiento dopaminérgico)",
        "6. La 3ª Ley: Hacerlo sencillo (La ley del menor esfuerzo y la regla de los dos minutos)",
        "7. La 4ª Ley: Hacerlo satisfactorio (La regla cardinal del cambio de conducta)",
        "8. Tácticas avanzadas: Cómo pasar de ser simplemente bueno a ser verdaderamente grandioso",
        "9. La regla de Ricitos de Oro: Cómo mantener la motivación en la vida y el trabajo",
        "10. El inconveniente de crear buenos hábitos y la trampa del estancamiento"
    ]
    create_troll_index_pdf(
        r"d:\pirata\downloads\Habitos_Atomicos_James_Clear.pdf",
        "Hábitos Atómicos",
        "James Clear",
        "Cambios pequeños, resultados extraordinarios",
        clear_index
    )

    # 3. PENSAR RÁPIDO, PENSAR DESPACIO - DANIEL KAHNEMAN
    kahneman_index = [
        "1. Dos sistemas: El Sistema 1 (rápido, intuitivo) y el Sistema 2 (lento, deliberativo)",
        "2. Atención y esfuerzo cognitivo: La ley del mínimo gasto de energía mental",
        "3. La máquina asociativa: Priming, coherencia y facilidad cognitiva",
        "4. Juicios heurísticos y sesgos cognitivos sistemáticos",
        "5. La ilusión de validez y la sobreestimación del control",
        "6. Intuición vs. Fórmulas algorítmicas en la toma de decisiones complejas",
        "7. La teoría de las perspectivas: Aversión a las pérdidas y riesgo asimétrico",
        "8. El efecto anclaje y la disponibilidad mental",
        "9. Dos yo: El yo que experimenta frente al yo que recuerda",
        "10. Conclusiones y reflexiones sobre la racionalidad humana"
    ]
    create_troll_index_pdf(
        r"d:\pirata\downloads\Pensar_Rapido_Pensar_Despacio_Daniel_Kahneman.pdf",
        "Pensar Rápido, Pensar Despacio",
        "Daniel Kahneman",
        "Los dos sistemas que modulan el juicio, la toma de decisiones y los sesgos",
        kahneman_index
    )
