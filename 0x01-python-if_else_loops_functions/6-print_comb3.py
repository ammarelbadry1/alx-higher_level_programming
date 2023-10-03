#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == j:
            continue
        if i == 8:
            print(f"{i}{j}")
            continue
        print(f"{i}{j} ,", end="")
