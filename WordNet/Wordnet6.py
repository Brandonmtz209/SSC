from nltk.corpus import wordnet

# Define the synsets for 'cookbook' and 'instruction_book'
cb = wordnet.synset('cookbook.n.01')
ib = wordnet.synset('instruction_book.n.01')

# Calculate and print the Wu-Palmer Similarity
print(cb.wup_similarity(ib))

# Get the common hypernym
ref = cb.hypernyms()[0]

# Calculate and print the shortest path distances
print(cb.shortest_path_distance(ref))
print(ib.shortest_path_distance(ref))
print(cb.shortest_path_distance(ib))

# Define the synset for 'dog'
dog = wordnet.synsets('dog')[0]

# Calculate and print the Wu-Palmer Similarity with 'dog'
print(dog.wup_similarity(cb))

# Print the common hypernyms with 'dog'
print(sorted(dog.common_hypernyms(cb)))

# Define the synsets for 'cook' and 'bake'
cook = wordnet.synset('cook.v.01')
bake = wordnet.synset('bake.v.02')

# Calculate and print the Wu-Palmer Similarity between 'cook' and 'bake'
print(cook.wup_similarity(bake))

# Calculate and print the path similarity and LCH similarity
print(cb.path_similarity(ib))
print(cb.path_similarity(dog))
print(cb.lch_similarity(ib))
print(cb.lch_similarity(dog))
