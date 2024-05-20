# Primero importamos el modulo NLTK
import nltk

# Ahora podemos llamar la funcion para descargar a wordnet
#(DESCOMENTAR SI ES LA PRIMERA EJECUCION)
#nltk.download('wordnet')
# Importar el módulo wordnet de la biblioteca NLTK
from nltk.corpus import wordnet

# Lista de etiquetas de parte del discurso (POS) en WordNet
pos_tags = ['n', 'v', 'a', 's', 'r']

# Función para imprimir la etiqueta POS y su significado
def print_pos_tags():
    for tag in pos_tags:
        if tag == 'n':
            print(f"'{tag}': Sustantivo")
        elif tag == 'v':
            print(f"'{tag}': Verbo")
        elif tag == 'a':
            print(f"'{tag}': Adjetivo")
        elif tag == 's':
            print(f"'{tag}': Adjetivo Satélite")
        elif tag == 'r':
            print(f"'{tag}': Adverbio")

# Llamar a la función para mostrar las etiquetas POS
print_pos_tags()

# Buscar los synsets para la palabra 'great' (grande)
synsets_great = wordnet.synsets('great')

# Imprimir todos los synsets para la palabra 'great'
print("Synsets para la palabra 'great':")
for syn in synsets_great:
    print(f"- {syn.name()}: {syn.definition()}")

# Buscar synsets para 'great' como sustantivo
noun_synsets = wordnet.synsets('great', pos='n')

# Imprimir solo los synsets que son sustantivos para 'great'
print("Synsets de sustantivos para 'great':")
for noun_syn in noun_synsets:
    print(f"- {noun_syn.name()}: {noun_syn.definition()}")

# Buscar synsets para 'great' como adjetivo
adj_synsets = wordnet.synsets('great', pos='a')

# Imprimir solo los synsets que son adjetivos para 'great'
print("Synsets de adjetivos para 'great':")
for adj_syn in adj_synsets:
    print(f"- {adj_syn.name()}: {adj_syn.definition()}")

# Recuperar e imprimir la etiqueta de parte del discurso (POS) para el primer synset de 'cookbook' (libro de cocina)
cookbook_syn = wordnet.synsets('cookbook')[0]
print(f"La etiqueta POS para el primer synset de 'cookbook': {cookbook_syn.pos()}")
