#!/usr/bin/python3

with open("file.txt", 'r', encoding="utf-8") as f:
    x = f.read()
    print(len(x))

with open("text.txt", 'a', encoding="utf-8") as g:
    g.write(x)
    #g.seek(78)
    print(g.tell())

