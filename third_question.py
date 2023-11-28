#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print_table()


def print_table():
    for x in range(1, 10):
        print("")
        for y in range(1, 10):
            print(f"|{x} * {y} = {x * y}|", end=" ")


if __name__ == "__main__":
    main()

