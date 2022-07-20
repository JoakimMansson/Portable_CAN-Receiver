import math
import re


def IEEE754(hex_value) -> float:
    hex_value = re.sub("b", "", str(bin(hex_value)))

    exponent_bits = hex_value[1:9]
    mantissa_bits = hex_value[9:]
    print("num: " + hex_value)
    print("exponent: " + exponent_bits)
    print("mantissa: " + mantissa_bits)

    mantissa_decimal = 0
    exponent_decimal = 0

    #Calculating mantissa
    for i in range(len(mantissa_bits)):
        if int(mantissa_bits[i]) != 0:
            mantissa_decimal = mantissa_decimal + math.pow(2, -(i+1))

    #Calculating exponent
    exponent_counter = 0
    for i in range(len(exponent_bits)-1, -1, -1):

        if int(exponent_bits[i]) != 0:
            print(i)
            exponent_decimal = exponent_decimal + math.pow(2, exponent_counter)
            print(exponent_decimal)

        exponent_counter = exponent_counter + 1

    print("Final exponent: " + str(exponent_decimal))
    print("Final mantissa: " + str(mantissa_decimal))

    return (1 + mantissa_decimal) * math.pow(2, exponent_decimal - 127)

if __name__ == "__main__":
    print(IEEE754(0x41b4cda0))