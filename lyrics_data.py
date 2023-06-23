import string
import textstat;
from nltk import FreqDist,tokenize
import nltk
import re
from collections import defaultdict



stopwords = nltk.corpus.stopwords.words('english')

def words(text):
    text_new = "".join([i for i in text if i not in string.punctuation])
    words = tokenize.word_tokenize(text_new.lower())
    words_new = [i for i in words if i not in stopwords]
    return words_new

def common_words(words):
    return FreqDist(words).most_common()

def group_text(texte):
    regex = r'\[(.*?)\]'
    resultats = list(filter(lambda x: x != "", re.split(regex, texte)))
    dictionnaire = defaultdict(list)
    for i in range(0, len(resultats)-1, 2):
        dictionnaire[remove_digit(clean_title(resultats[i]))].append(resultats[i+1])
    return dictionnaire

def clean_title(title):
    if(":" in title):
        return title.split(":")[0].strip()
    return title
def remove_digit(title):
    if(title[-1].isdigit()):
        return title.rstrip(title[-1]).strip()
    return title;

def statistics(titre,groupe):
    grouped_text = "".join(groupe)
    all_words = words(grouped_text)
    
    return {titre :{
        "count" : len(groupe),
        "sentences" : len(list(filter(lambda x: x != "",grouped_text.split("\n")))),
        "words"  : len(all_words),
        "words_distinct" : len(common_words(all_words)),
        "mono" : textstat.monosyllabcount(grouped_text),
        "poly" : textstat.polysyllabcount(grouped_text),
        "vocabulary" : common_words(all_words)}
    }
def stat_by_part(lyrics):
    titres_groupes = group_text(lyrics)
    return list(map(statistics,titres_groupes.keys(),titres_groupes.values()));

def state_global(lyrics):
    regex = r"\[.*?\]"
    texte_sans_crochets = re.sub(regex, "", lyrics)
    texte_sans_crochets
    return statistics("global",texte_sans_crochets)
