# Primero importamos el modulo NLTK
import nltk

# Ahora podemos llamar la funcion para descargar a wordnet
#(DESCOMENTAR SI ES LA PRIMERA EJECUCION)
#nltk.download('wordnet')
# Importar el módulo wordnet de la biblioteca NLTK
from nltk.corpus import wordnet

# Crear una lista vacía para almacenar los sinónimos
synonyms = []

# Buscar todos los synsets para la palabra 'book'
for syn in wordnet.synsets('book'):
    # Para cada synset, obtener todos los lemas y añadirlos a la lista de sinónimos
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

# Imprimir el número total de sinónimos encontrados
print(len(synonyms))  # Devuelve: 38

# Algunos sinónimos pueden ser formas verbales o diferentes usos de 'book',
# por lo que si tomamos el conjunto de sinónimos, hay menos palabras únicas
unique_synonyms = set(synonyms)
print(len(unique_synonyms))  # Devuelve: 25
