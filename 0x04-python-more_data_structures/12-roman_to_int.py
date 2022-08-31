#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom_str = roman_string
        number = 0
        for l in range(len(rom_str)):
            if l > 0 and (rom[rom_str[l]] > rom[rom_str[l - 1]]):
                number += rom[rom_str[l]] - (2 * rom[roman_string[l - 1]])
            else:
                number += rom[rom_str[l]]
        return number
    return (0)
