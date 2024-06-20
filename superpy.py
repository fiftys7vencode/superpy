import math as ma
def math_PI():
    return 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067

def math_PI_low():
    return 3.14

def math_E():
    return 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427

def math_E_low():
    return 2.71

def math_tetration(num1, num2):
    return pow(num1, num2) * 2

def math_add(a, b):
    return a + b

def math_subtract(a, b):
    return a - b

def math_multiply(a, b):
    return a * b

def math_divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Division by zero'

def math_power(base, exp):
    return pow(base, exp)

def math_sqrt(num):
    if num >= 0:
        return ma.sqrt(num)
    else:
        return 'Error: Square root of negative number'

def math_log(num, base=ma.e):
    if num > 0:
        return ma.log(num, base)
    else:
        return 'Error: Logarithm of non-positive number'

def math_sin(x):
    return ma.sin(x)

def math_cos(x):
    return ma.cos(x)

def math_tan(x):
    return ma.tan(x)

def math_factorial(n):
    if n >= 0:
        return ma.factorial(n)
    else:
        return 'Error: Factorial of negative number'

def math_combinations(n, k):
    if 0 <= k <= n:
        return ma.comb(n, k)
    else:
        return 'Error: Invalid values for combinations'
    
def math_stringequation(expression):
    expression = expression.replace('x', '*')
    expression = expression.replace('÷', '/')
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error evaluating expression '{expression}': {e}")
        return None


def string_reversestring(string):
     return string[::-1]

def string_uppercase(string):
    return string.upper()

def string_lowercase(string):
    return string.lower()

def string_count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
    return count

def string_count_consonants(string):
    count = 0
    for char in string:
        if char.isalpha() and char not in 'aeiouAEIOU':
            count += 1
    return count

def string_is_palindrome(string):
    return string == string[::-1]

def string_alternate_case(string):
    result = ''
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

def string_title_case(string):
    return string.title()

def string_remove_spaces(string):
    return string.replace(' ', '')

def string_replace_spaces_with_underscore(string):
    return string.replace(' ', '_')

def string_count_words(string):
    return len(string.split())

def string_reverse_words(string):
    words = string.split()
    return ' '.join(words[::-1])

def string_add_prefix(string, prefix):
    return prefix + string

def string_add_suffix(string, suffix):
    return string + suffix

def string_remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in string if char not in vowels])

def string_remove_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return ''.join([char for char in string if char not in consonants])

def string_add_frame(string):
    lines = string.splitlines()
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'

    framed_string = [border]
    for line in lines:
        framed_string.append('| ' + line.ljust(max_length) + ' |')
    framed_string.append(border)

    return '\n'.join(framed_string)

def conversion_kilometerstomiles(kilometers):
     return kilometers * 0.621371
def conversion_milestokilometers(miles):
     return miles / 0.621371
def conversion_kilogramstodekagrams(kilograms):
    return kilograms * 100
def conversion_dekagramstokilograms(dekagrams):
    return dekagrams / 100
def conversion_dekagramstograms(dekagrams):
    return dekagrams * 10
def conversion_gramstodekagrams(grams):
    return grams / 10
def conversion_kilogramstograms(kilograms):
    return kilograms * 1000
def conversion_gramstokilograms(grams):
    return grams / 1000
def conversion_kilometerstometers(kilometers):
    return kilometers * 1000
def conversion_meterstokilometers(meters):
    return meters / 1000
def conversion_meterstocentimeters(meters):
    return meters * 100
def conversion_centimeterstometers(centimeters):
    return centimeters / 100
def conversion_meterstomillimeters(meters):
    return meters * 1000
def conversion_millimeterstometers(millimeters):
    return millimeters / 1000
def conversion_kilometerstocentimeters(kilometers):
    return kilometers * 100000
def conversion_centimeterstokilometers(centimeters):
    return centimeters / 100000
def conversion_kilometerstomillimeters(kilometers):
    return kilometers * 1000000
def conversion_millimeterstokilometers(millimeters):
    return millimeters / 1000000
# Delete this part if you want
# Delete part start
def documentation():
    print("Documentation: https://github.com/fiftys7vencode/superpy/blob/main/documentation.md")
# Delete part end
