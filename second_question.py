#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    nums_list = []
    for i in range(1, 4):
        nums_list.append(int(input(f"{i}. Введите число: \n")))
    is_even_in_list(nums_list)


def is_even_in_list(nums: list):
    for number in nums:
        if number % 2 == 0:
            print("В списке присутствует четное число!")
            return
    print("В списке отсутствуют четные числа!")


if __name__ == "__main__":
    main()
