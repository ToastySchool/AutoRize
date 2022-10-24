import nltk
from nltk.corpus import wordnet
from gingerit.gingerit import GingerIt

nltk.download('stopwords')




#function that will replace the words with synonyms
def replace_words(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    if len(synonyms) > 0:
        return synonyms[0]
    else:
        parser = GingerIt()
        checked = parser.parse(word)['result']
        checked.replace("_", " ")
        return checked
 
 
#function that will replace the words with synonyms
def replace_synonyms(text):
    words = text.split()
    new_words = []
    for word in words:
        new_word = replace_words(word)
        new_words.append(new_word)
    new_text = " ".join(new_words)
    #print the new text with \n after every .
    print(" ".join(new_text.split(". ")))


