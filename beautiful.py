#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    print "Программа вычисления индекса женской красоты:"
    print "-------------------------------------------------"
    breast = int(input("Введите обхват бюста: "))
    hips = int(input("Введите обхват по бедрам: "))
    waist = int(input("Введите обхват по талии: "))
    growth = int(input("Введите рост: "))
    weight = int(input("Введите вес: "))
    print"--------------------------------------------------"
    print"Индекс женской красоты равен: " +  str(beauti(breast, hips, waist, growth, weight))


def beauti(breast, hips, waist, growth, weight):
    x = breast * hips * growth
    y = (waist**2) * weight
    return x/y

if __name__ == "__main__":
        main()
