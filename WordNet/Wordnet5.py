# Primero importamos el modulo NLTK
import nltk

# Ahora podemos llamar la funcion para descargar a wordnet
#(DESCOMENTAR SI ES LA PRIMERA EJECUCION)
#nltk.download('wordnet')
# Importar el módulo wordnet de la biblioteca NLTK
from nltk.corpus import wordnet

# Buscar el segundo synset para la palabra 'good' como sustantivo
gn2 = wordnet.synset('good.n.02')

# Imprimir el nombre y la definición de este synset
print(gn2.name())  # Devuelve: 'evil'
print(gn2.definition())  # Devuelve: 'moral excellence or admirableness'

# Obtener el primer antónimo del primer lema de este synset
evil = gn2.lemmas()[0].antonyms()[0]

# Imprimir el nombre y la definición de este antónimo
print(evil.name())  # Devuelve: 'evil'
print(evil.synset().definition())  # Devuelve: 'the quality of being morally wrong in principle or practice'

# Buscar el primer synset para la palabra 'good' como adjetivo
ga1 = wordnet.synset('good.a.01')

# Imprimir la definición de este synset
print(ga1.definition())  # Devuelve: 'having desirable or positive qualities especially those suitable for a thing specified'

# Obtener el primer antónimo del primer lema de este synset
bad = ga1.lemmas()[0].antonyms()[0]

# Imprimir el nombre y la definición de este antónimo
print(bad.name())  # Devuelve: 'bad'
print(bad.synset().definition())  # Devuelve: 'having undesirable or negative qualities'
