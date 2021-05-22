import random

from PyDictionary import PyDictionary
dictionary= PyDictionary()

fh= open("words.txt")
words= fh.read().split("\n")
#print(len(words))

#print(words)
def rand_word():
    valid_word= False
    while(not valid_word):
        word_index= random.randint(0,466551)

        word=words[word_index]
        if(word[0].islower() and len(word)>2):
            valid_word= True
            return word     

def word_defination():
    valid_word=False
    while (not valid_word):
        word= rand_word()
        if(dictionary.meaning(word, disable_errors=True)):
            print(word.upper())
            print(dictionary.meaning(word))
            

            print("Synonyms : ",dictionary.synonym(word))
            
            print("Antonyms : ",dictionary.antonym(word))
            valid_word= True
              # if(dictionary.translate(word,'es')):
              #     print("Translation : ", dictionary.translate(word,'es'))
        else:
             pass
            
word_defination()


"""
Generates a random word from file words.txt and prints its defination including meaning, antonyms, synonyms
-import random to generate random words
-import PyDictionary module for extracting defination of the words
-Prints only those definations which exists in PyDictionary


https://pypi.org/project/PyDictionary/
"""