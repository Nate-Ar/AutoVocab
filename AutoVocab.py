from PyDictionary import PyDictionary
dic = PyDictionary()
try:
    with open('vocab.txt', 'r') as words:
        for word in words:
            print(dic.meaning(word))
except():
    print('All Done')
