import nltk
import ssl

#try:
#    _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
#    pass
#else:
#    ssl._create_default_https_context = _create_unverified_https_context
#
#nltk.download('punkt')
import re
from data import TEST_DATA

sample_text = """"""

class LangSet:

    def __init__(self, texts:list):
        self.texts = texts
        
    def get_noun_tags(self, text:str):
        print('lol',text)
        text = re.sub(r'[^\w]', ' ', text).strip().lower()
        tag_obj = {}
        tokens = nltk.word_tokenize(text) 
        for word, tag in nltk.pos_tag(tokens):
          if tag not in tag_obj.keys():
            tag_obj[tag] = {word}
          else:
            tag_obj[tag].add(word)
        return tag_obj["NN"].union(tag_obj["JJ"])

    def highest_match_noun(self, text_input:str):
        input_NN_tags = self.get_noun_tags(text_input)
        last_most = 0
        matched_text = ""
        matched_nn = set()
        for i in range(len(self.texts)):
            text_NN_tags = self.get_noun_tags(self.texts[i])
            intersect = input_NN_tags.intersection(text_NN_tags)
            get_num_match = len(intersect)
            print("last most:", get_num_match)
            if get_num_match>last_most:
                last_most = get_num_match
                matched_text = self.texts[i]
                matched_nn = intersect
        return matched_text, matched_nn, last_most

lang = LangSet(TEST_DATA['articles'])
#print(lang.get_noun_tags(lang.texts[0]))
print(lang.highest_match_noun(sample_text))