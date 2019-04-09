"""word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
       " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
       " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

wordList = list(word)
wordLength = len(word)
progress = 0
newWordList = []

for x in range(208):
    char = wordList[progress]
    xIndex = wordList.index(char)
    if char == "a":
        newWordList.insert(xIndex, "c")
    if char == "b":
        newWordList.insert(xIndex, "d")
    if char == "c":
        newWordList.insert(xIndex, "e")
    if char == "d":
        newWordList.insert(xIndex, "f")
    if char == "e":
        newWordList.insert(xIndex, "g")
    if char == "f":
        newWordList.insert(xIndex, "h")
    if char == "g":
        newWordList.insert(xIndex, "i")
    if char == "h":
        newWordList.insert(xIndex, "j")
    if char == "i":
        newWordList.insert(xIndex, "k")
    if char == "j":
        newWordList.insert(xIndex, "l")
    if char == "k":
        newWordList.insert(xIndex, "m")
    if char == "l":
        newWordList.insert(xIndex, "n")
    if char == "m":
        newWordList.insert(xIndex, "o")
    if char == "n":
        newWordList.insert(xIndex, "p")
    if char == "o":
        newWordList.insert(xIndex, "q")
    if char == "p":
        newWordList.insert(xIndex, "r")
    if char == "q":
        newWordList.insert(xIndex, "s")
    if char == "r":
        newWordList.insert(xIndex, "t")
    if char == "s":
        newWordList.insert(xIndex, "u")
    if char == "t":
        newWordList.insert(xIndex, "v")
    if char == "u":
        newWordList.insert(xIndex, "w")
    if char == "v":
        newWordList.insert(xIndex, "x")
    if char == "w":
        newWordList.insert(xIndex, "y")
    if char == "x":
        newWordList.insert(xIndex, "z")
    if char == "y":
        newWordList.insert(xIndex, "a")
    if char == "z":
        newWordList.insert(xIndex, "b")
    wordList.insert(xIndex, "0")
    if char == " ":
        newWordList.insert(xIndex, " ")

    progress += 1
    print(progress)
    if progress == wordLength:
        break


print(newWordList)"""


word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
       " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
       " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

wordList = list(word)
newWordList = []

for x in range(210):
    newWordList.append(" ")

for n, i in enumerate(wordList):
    if i == "a":
        newWordList[n] = "c"

for n, i in enumerate(wordList):
    if i == "b":
        newWordList[n] = "d"

for n, i in enumerate(wordList):
    if i == "c":
        newWordList[n] = "e"

for n, i in enumerate(wordList):
    if i == "d":
        newWordList[n] = "f"

for n, i in enumerate(wordList):
    if i == "e":
        newWordList[n] = "g"

for n, i in enumerate(wordList):
    if i == "f":
        newWordList[n] = "h"

for n, i in enumerate(wordList):
    if i == "g":
        newWordList[n] = "i"

for n, i in enumerate(wordList):
    if i == "h":
        newWordList[n] = "j"

for n, i in enumerate(wordList):
    if i == "i":
        newWordList[n] = "k"

for n, i in enumerate(wordList):
    if i == "j":
        newWordList[n] = "l"

for n, i in enumerate(wordList):
    if i == "k":
        newWordList[n] = "m"

for n, i in enumerate(wordList):
    if i == "l":
        newWordList[n] = "n"

for n, i in enumerate(wordList):
    if i == "m":
        newWordList[n] = "o"

for n, i in enumerate(wordList):
    if i == "n":
        newWordList[n] = "p"

for n, i in enumerate(wordList):
    if i == "o":
        newWordList[n] = "q"

for n, i in enumerate(wordList):
    if i == "p":
        newWordList[n] = "r"

for n, i in enumerate(wordList):
    if i == "q":
        newWordList[n] = "s"

for n, i in enumerate(wordList):
    if i == "r":
        newWordList[n] = "t"

for n, i in enumerate(wordList):
    if i == "s":
        newWordList[n] = "u"

for n, i in enumerate(wordList):
    if i == "t":
        newWordList[n] = "v"

for n, i in enumerate(wordList):
    if i == "u":
        newWordList[n] = "w"

for n, i in enumerate(wordList):
    if i == "v":
        newWordList[n] = "x"

for n, i in enumerate(wordList):
    if i == "w":
        newWordList[n] = "y"

for n, i in enumerate(wordList):
    if i == "x":
        newWordList[n] = "z"

for n, i in enumerate(wordList):
    if i == "y":
        newWordList[n] = "a"

for n, i in enumerate(wordList):
    if i == "z":
        newWordList[n] = "b"

newWord = "".join(newWordList)

print(newWord)