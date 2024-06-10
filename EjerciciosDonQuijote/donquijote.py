import PyPDF2
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import os
import re

# Función para extraer texto de un archivo PDF y quitar signos de puntuación
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    
    # Remover signos de puntuación
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

# Función para contar las palabras y generar el HTML
def count_words_and_generate_html(pdf_file, output_html):
    # Extraer texto del PDF
    text = extract_text_from_pdf(pdf_file)

    # Tokenizar el texto en palabras
    words = word_tokenize(text)

    # Crear una distribución de frecuencia de palabras
    freq_dist = FreqDist(words)

    # Obtener el total de palabras únicas
    total_unique_words = len(set(words))

    # Ordenar la distribución de frecuencia por frecuencia descendente
    sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

    # Generar HTML
    html_content = f"<h1>Total de palabras en {os.path.basename(pdf_file)}: {len(words)}</h1>"
    html_content += f"<h1>Total de palabras únicas: {total_unique_words}</h1>"
    html_content += "<h2>Distribución de frecuencia de palabras:</h2>"
    html_content += "<ul>"
    for word, frequency in sorted_freq_dist:
        html_content += f"<li>{word}: {frequency}</li>"
    html_content += "</ul>"

    # Escribir el contenido HTML en un archivo
    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print(f"Se ha generado el archivo HTML en: {output_html}")

# Nombre del archivo PDF
pdf_file = "donquijote.pdf"

# Nombre del archivo HTML de salida
output_html = "resultado.html"

# Contar palabras y generar HTML
count_words_and_generate_html(pdf_file, output_html)
