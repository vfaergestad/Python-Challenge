"""alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

progress = 0

for x in alphabetList:
    orgIndex = alphabetList.index(x)
    if orgIndex < 24:
        newIndex = orgIndex + 2
    if orgIndex > 23:
        diff = orgIndex - 24
        newIndex = alphabetList[diff]
    alphabetList.remove(x)
    alphabetList.insert(newIndex, x)

    progress += 1
    print(progress)
    if progress == 26:
        break

print(alphabetList)"""

word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
       " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
       " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

wordList = list(word)
wordLength = len(word)
progress = 0

for x in wordList:
    xIndex = wordList.index(x)
    if x == "a":
        wordList[xIndex] = "c"
    if x == "b":
        wordList[xIndex] = "d"
    if x == "c":
        wordList[xIndex] = "e"
    if x == "d":
        wordList[xIndex] = "f"
    if x == "e":
        wordList[xIndex] = "g"
    if x == "f":
        wordList[xIndex] = "h"
    if x == "g":
        wordList[xIndex] = "i"
    if x == "h":
        wordList[xIndex] = "j"
    if x == "i":
        wordList[xIndex] = "k"
    if x == "j":
        wordList[xIndex] = "l"
    if x == "k":
        wordList[xIndex] = "m"
    if x == "l":
        wordList[xIndex] = "n"
    if x == "m":
        wordList[xIndex] = "o"
    if x == "n":
        wordList[xIndex] = "p"
    if x == "o":
        wordList[xIndex] = "q"
    if x == "p":
        wordList[xIndex] = "r"
    if x == "q":
        wordList[xIndex] = "s"
    if x == "r":
        wordList[xIndex] = "t"
    if x == "s":
        wordList[xIndex] = "u"
    if x == "t":
        wordList[xIndex] = "v"
    if x == "u":
        wordList[xIndex] = "w"
    if x == "v":
        wordList[xIndex] = "x"
    if x == "w":
        wordList[xIndex] = "y"
    if x == "x":
        wordList[xIndex] = "z"
    if x == "y":
        wordList[xIndex] = "a"
    if x == "z":
        wordList[xIndex] = "b"

    progress += 1
    print(progress)
    if progress == wordLength:
        break


print(wordList)
