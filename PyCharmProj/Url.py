import urllib.request
#python module for retrieving url pages

#url with the vocabulary of interest
req = urllib.request.Request('https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt')
#open the url
response = urllib.request.urlopen(req)
#read the html file: Decode using utf-8
the_page = response.read().decode("utf-8")

glossary = the_page.lower().split()
for w in glossary:
    if '<pre' in w:
        start = glossary.index(w)
        print(start)
    if '</pre' in w:
        finish = glossary.index(w)
        print(finish)

narnia = glossary[start:finish]

#count unique word
def countWord(word, lwidth, rwidth):
    '''
    print the words and their respective frequency
    :param word: string
    :param lwidth: int
    :param rwidth: int
    :return: None
    '''
    print("The Chronicles of Narnia".center(lwidth + rwidth,'-'))
    for k, v in word.items():
        print(k.ljust(lwidth, '.'),  str(v).rjust(rwidth))

count = {}
punctuations = ["~","!","%","^","&","*","(",")","_","-","{","}","[","]","\\","|",";",":","'","\"",",",".","/","<",">","/","?"]
for index, word in enumerate(narnia):
    for letter in narnia[index]:
        if letter in punctuations:
            narnia[index] = word.replace(letter,"")

filteredNarnia = []

for x in narnia[1:100]:
    if len(x) == 5:
        filteredNarnia.append(x)

for x in filteredNarnia[1:100]:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

countWord(count, 25, 7)

