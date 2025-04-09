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

if __name__ == '__main__':

    part = 'A'

    match part:
        case 'A':

            input = read_full_input(3,False)

            tuples = extract_tuples_from_string(input)
            products = multiply_tuples(tuples)
            sum = sum_products(products)

            print(f"Final sum: {sum}")