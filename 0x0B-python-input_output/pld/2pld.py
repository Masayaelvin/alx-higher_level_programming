#!/usr/bin/python3
with open("text.txt", 'r', encoding="utf-8") as g:
    data = g.read()

    count = 0
    for i in data:
        print(i, end='')
        if i == "\n":
            count += 1
            print(f"line:{count} ", end='')
            if count == 7:
                break
