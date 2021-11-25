import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    lisattavat = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for luku in lisattavat:
        joukko.lisaa(luku)

    joukko.mahtavuus()
    joukko.kuuluu(11)
    joukko.poista(11)
    joukko.kuuluu(11)
    joukko.mahtavuus()

    joukko.to_int_list()


if __name__ == "__main__":
    main()
