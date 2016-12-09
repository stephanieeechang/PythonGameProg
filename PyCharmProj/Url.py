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
    for ele in word:
        print(ele[0].ljust(lwidth, '.'),  str(ele[1]).rjust(rwidth))


def bubbleSort(items):
    '''
    implementation of bubble sort
    :param items: list
    :return: list
    '''
    index = list(range(len(items)))
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if(items[j] < items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                index[j], index[j+1] = index[j+1], index[j]
    return items, index

def prebubble(wordbanklist):
    '''
    return the sorted list of words
    :param wordbanklist: list of unsorted tuples
    :return: list of tuples
    '''
    items = [element[1] for element in wordbanklist]
    items_sort, index = bubbleSort(items)
    sortwordbank = [wordbanklist[i] for i in index]
    return sortwordbank


def preinsertion(wordbanklist):
    '''
    return the sorted list of words
    :param wordbanklist: list of unsorted tuples
    :return: list of tuples
    '''
    items = [element[1] for element in wordbanklist]
    items_sort, index = insertionSort(items)
    sortwordbank = [wordbanklist[i] for i in index]
    return sortwordbank

def insertionSort(items):
    index = list(range(len(items)))
    for i in range(1, len(items)):
        j = i
        while(j>0 and items[j]>items[j-1]):
            items[j],items[j-1] = items[j-1], items[j]
            index[j], index[j-1] = index[j- 1], index[j]
            j -= 1
    return items, index

count = {}
punctuations = "~!@#$%^&*()_+?><,./\"{}[]|\\;':-"

newNarnia = []
for index, word in enumerate(narnia):
    for letter in word:
        if letter in punctuations:
            word = word.replace(letter, "")
    newNarnia.append(word)

filteredNarnia = []

for x in newNarnia:
    if len(x) == 5:
        filteredNarnia.append(x)

for x in filteredNarnia:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

#countWord(count, 25, 7)

wbList = [(k,v) for k,v in count.items()]
print('BUBBLE SORT')
bsList = prebubble(wbList)
countWord(bsList, 25, 7)
print('\n\n')

print('INSERTION SORT')
isList = preinsertion(wbList)
countWord(isList, 25, 7)
