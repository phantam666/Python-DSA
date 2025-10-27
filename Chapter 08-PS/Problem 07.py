def rem(n, word):
    l = []
    for item in n:
        if not(item == word):
           l.append(item.strip(word))
    return l


n = ["Vivek", "aditya", "ram", "amit"]

print(rem(n, "ktam"))
