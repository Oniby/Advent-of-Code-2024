import re
from utils import *

def extract_tuples_from_string(string):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    tuples = pattern.findall(string)
    tuples = [(int(a),int(b)) for a,b in tuples]
    return tuples

def multiply_tuples(tuples):
    products = [a*b for a,b in tuples]
    return products

def sum_products(products):
    sum = 0
    for product in products:
        sum += product
    return sum

def extract_tokens(string):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")
    items = pattern.finditer(string)
    tokens = []
    for m in items:
        if m.lastindex:
            x = m.group(1)
            y = m.group(2)
            tokens.append((int(x), int(y)))
        else:
            tokens.append(m.group(0))
    return tokens

def process_tokens(tokens):
    do = True
    sum = 0
    for t in tokens:
        if t == "do()":
            do = True
        elif t == "don't()":
            do = False
        else:
            sum += (t[0]*t[1])*(1 if do else 0)
    return sum

if __name__ == '__main__':

    part = 'B'

    match part:
        case 'A':

            input = read_full_input(3,False)

            tuples = extract_tuples_from_string(input)
            products = multiply_tuples(tuples)
            sum = sum_products(products)

            print(f"Final sum: {sum}")

        case 'B':

            input = read_full_input(3,False)
            tokens = extract_tokens(input)
            sum = process_tokens(tokens)
            print(f"Final sum: {sum}")
