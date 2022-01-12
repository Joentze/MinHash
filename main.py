import random
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
TEST_STRING_1 = """"""

TEST_STRING_2 = """"""

TEST_STRING_3 = """"""

def shingle(text:str, k:int):
    shingle_list = []
    for i in range(len(text.strip().replace('\n',''))-k+1):
        shingle_list.append(text[i:i+k])
    return set(shingle_list)

a = shingle(TEST_STRING_1,2)
b = shingle(TEST_STRING_2,2)
c = shingle(TEST_STRING_3,2)

vocab = list(a.union(b).union(c))
"""makes all of them the same length"""
a_1hot = [1 if x in a else 0 for x in vocab]
b_1hot = [1 if x in b else 0 for x in vocab]
c_1hot = [1 if x in c else 0 for x in vocab]

def get_signature(hot_list:list, iteration:int):
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

a_hash = get_signature(a_1hot, 1000)
b_hash = get_signature(b_1hot, 1000)
c_hash = get_signature(c_1hot, 1000)

def jaccard(x, y):
    return len(x.intersection(y))/len(x.union(y))

print(jaccard(c_hash, b_hash))