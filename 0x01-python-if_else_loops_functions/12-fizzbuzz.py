#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("FIZZBUZZ", end=' ')
        elif a % 3 == 0:
            print("FIZZ", end=' ')
        elif a % 5 == 0:
            print("BUZZ", end=' ')
        else:
            print(a, end=' ')
