import random
from data import TEST_DATA
def jaccard(x, y):
    return len(x.intersection(y))/len(x.union(y))

class MinHash:

    def __init__(self, texts:list, k:int):
        self.texts = texts
        self.k = k
        self.shing_k = 2
        self.vocab = self.get_vocab()

    def shingle(self, text:str):
        shingle_list = []
        for i in range(len(text.strip().replace('\n',''))-self.shing_k+1):
            shingle_list.append(text[i:i+self.shing_k])
        return shingle_list

    def get_one_hot(self, shingle_text:list):
        return [1 if i in shingle_text else 0 for i in self.vocab]

    def get_vocab(self):
        this_set = set()
        for text in self.texts:
            shingle = self.shingle(text)
            this_set.union(shingle)
        return list(this_set)

    def get_sig(self, hot_list:list, iteration:int):
        signature_list = []
        hash_ex = list(range(1,len(vocab)+1))
        for i in range(0,iteration):
            random.shuffle(hash_ex)
            for cnt in range(1,len(hash_ex)+1):
                get_index = hash_ex.index(cnt)
                if hot_list[get_index] == 1:
                    signature_list.append(get_index)
                    break
                else:
                    continue
        return set(signature_list)

#min_hash =  MinHash(TEST_DATA['articles'], 100)
#print(min_hash.shingle(min_hash.texts[0]))