import spacy
from newspaper import Article
import os
from gingerit.gingerit import GingerIt
import nltk

from reWriter import replace_synonyms
nltk.download('averaged_perceptron_tagger')


# Checking the system the user is on to clear the console.
def clearSystem():
    # if the os is windows use cls instead of clear
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#Clearing the console.
clearSystem()



nlp = spacy.load("en_core_web_sm")

### Greabs the article to download it and parse
def grabbingArticle():
    print("""Please paste the URL to your article. :) """)
    url = input("URL: ")
    print("""How many sentences would you like to have in your final summary?""")
    paper = Article(url)
    # Downloading the article and parsring it.
    try:
        paper.download()
        paper.parse()
    except :
        print("URL FORBIDDEN")
        exit()

    summarizeArticle(paper.text)



### Giving a brief summarization of the article.
def summarizeArticle(article):
    doc = nlp(article)

    #Creatinging a dictionary
    word_dict = {}
    #Looping through every thing 
    for word in doc:
        #setting every single word to lower case
        word = word.text.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    ### Creating a list of Tuples
    sents = []
    sent_score = 0

    for index, sent in enumerate(doc.sents):
        for word in sent:
            word = word.text.lower()
            sent_score += word_dict[word]
        sents.append((sent.text.replace("\n", " "), sent_score/len(sent), index))
    ### Getting the most important text for the summary
    sents = sorted(sents, key=lambda x: -x[1])
    # Returning the top 3 results
    print(f"Max amount of sentences: {len(sents)}")
    sentences = int(input("How man sentences?   : "))

    ### Simple check if they are asking for more sentences than what is available.
    if sentences > len(sents):
        print("To many sentences")
    else:
        sents = sorted(sents[:sentences], key=lambda x: x[2])

        ### Putting together all the sentences
        
        summary_text = ""
        for sent in sents:
            summary_text += sent[0] + " "
        replace_synonyms(summary_text)
        
    

    input("Press any key to continue.")
    clearSystem()
    grabbingArticle()




    


### Application ###
if __name__ == "__main__":
    grabbingArticle()