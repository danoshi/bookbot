import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'books/frankenstein.txt')


def readBooks(path):
    with open(path) as f:
        content = f.read()
        return content


def countWords(content):
    counter = 0
    words = content.split()
    for _ in words:
        counter = counter + 1
    res = f"{counter} words found in the document"
    return res

def countChars(content):
    chars = {}
    lowercase = content.lower()
    for w in lowercase:
        if w in chars:
            chars[w] += 1
        else:
            chars[w] = 1 
    return chars

def convertDictToList(charsDict):
    sortedDict = []
    for key, value in charsDict.items():
        if key.isalpha():
            sortedDict.append({"char": key, "num": value})
    return sortedDict

def sort_on(dict):
    return dict["num"]

def sortList(charsList):
    charsList.sort(reverse=True, key=sort_on)

def output():
    print("--- Begin report of books/frankenstein.txt ---")
    content = readBooks(filename)
    print(countWords(content) + "\n")
    countChar = countChars(content)
    convert = convertDictToList(countChar)
    sortList(convert)
    for w in convert:
        print(f"The '{w['char']}' char was found {w['num']} times")
    print("\n"+"--- End report ---")

   
if __name__ == '__main__':
    output()