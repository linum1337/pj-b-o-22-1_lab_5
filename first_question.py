#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    spent_electricity = input("Введите израсходованные кВТ/ч\n")
    print(what_about_money(int(spent_electricity)))


def what_about_money(spent_electricity: int) -> int:
    if spent_electricity < 250:
        return spent_electricity * 7
    elif 250 < spent_electricity < 300:
        return spent_electricity * 17
    else:
        return spent_electricity * 20


if __name__ == "__main__":
    main()
