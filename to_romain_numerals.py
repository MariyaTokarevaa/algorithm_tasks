''' напишите функцию,
которая на вход принимает любое целое число и
возвращает его в римском представлении (как строку).'''
num_dict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

def convert(data):
    result = ""
    for i in num_dict.keys():
        b, data = divmod(data, i)
        result += num_dict[i] * b
    return result
