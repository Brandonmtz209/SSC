# Primero importamos el modulo NLTK
import nltk

# Ahora podemos llamar la funcion para descargar a wordnet
#(DESCOMENTAR SI ES LA PRIMERA EJECUCION)
nltk.download('wordnet')
# Importamos el corpus de WordNet de la biblioteca nltk
from nltk.corpus import wordnet

# Buscamos los synsets (grupos de sinónimos) de la palabra 'cookbook'
syn = wordnet.synsets('cookbook')[0]

# Obtenemos las formas canónicas o lemas de este synset
lemmas = syn.lemmas()

# Imprimimos el número de lemas
print(len(lemmas))  # Devuelve: 2

# Imprimimos el nombre del primer lema
print(lemmas[0].name())  # Devuelve: 'cookbook'

# Imprimimos el nombre del segundo lema
print(lemmas[1].name())  # Devuelve: 'cookery_book'

# Comprobamos si ambos lemas pertenecen al mismo synset
print(lemmas[0].synset() == lemmas[1].synset())  # Devuelve: True
