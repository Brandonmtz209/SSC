# Primero importamos el modulo NLTK
#import nltk

# Ahora podemos llamar la funcion para descargar a wordnet
#(DESCOMENTAR SI ES LA PRIMERA EJECUCION)
#nltk.download('wordnet')

# Importar el modulo wordnet de la libreria NLTK
from nltk.corpus import wordnet

# Buscar los synsets de una palabra especifica en este caso cookbook
syn = wordnet.synsets('cookbook')[0]

# Obtener y mostrar el nombre del primer synset
print(syn.name())  # Output: 'cookbook.n.01'

# Obtener y mostrar la definicion del primer synset
print(syn.definition())  # Output: 'a book of recipes and cooking directions'
