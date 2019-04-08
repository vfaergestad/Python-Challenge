alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


for x in alphabetList:
    orgIndex = alphabetList.index(x)
    if orgIndex > 24:
        newIndex = orgIndex + 2
        x = alphabetList[newIndex]
    if orgIndex < 23:
        diff = len(alphabetList) - orgIndex - 1
        newIndex = alphabetList[diff]
