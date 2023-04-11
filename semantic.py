# L3T12 Semantic Similarity(NLP)
# Task1 Check sentence similarity using spacy.

import spacy

#1 -Checking for similarities between words below:
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("similarity between cat and monkey : ", word1.similarity(word2))
print("similarity between banana and monkey : ", word3.similarity(word2))
print("similarity between banana and cat : ", word3.similarity(word1))

print("")
#2a - Working with vectors - automatically comparing a number of words.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("")
#2b - my own list.
tokens = nlp('horse sheep male female car bicycle man woman house dog human baby')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("")
#3 - Working with sentences.
print("Sentence to compare: Why is my cat on the car")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
