---

# `superpy.py` Module Documentation

This module provides a collection of mathematical operations, string manipulations, and unit conversions.

## Mathematical Functions

### `math_PI()`

Returns the value of mathematical constant π (pi).

- **Returns:**
  - `float`: Value of π (pi).

### `math_PI_low()`

Returns a lower-precision approximation of π (pi).

- **Returns:**
  - `float`: Lower-precision approximation of π.

### `ma_E()`

Returns the value of mathematical constant e (Euler's number).

- **Returns:**
  - `float`: Value of e (Euler's number).

### `math_E_low()`

Returns a lower-precision approximation of e (Euler's number).

- **Returns:**
  - `float`: Lower-precision approximation of e.

### `math_tetration(num1, num2)`

Performs tetration of `num1` to the power of `num2` multiplied by 2.

- **Parameters:**
  - `num1` (float): Base number.
  - `num2` (float): Exponent number.

- **Returns:**
  - `float`: Result of tetration operation.

## Basic Mathematical Operations

### Arithmetic Operations

- `math_add(a, b)`: Adds two numbers `a` and `b`.
- `math_subtract(a, b)`: Subtracts number `b` from `a`.
- `math_multiply(a, b)`: Multiplies two numbers `a` and `b`.
- `math_divide(a, b)`: Divides number `a` by `b`.
- `math_power(base, exp)`: Raises `base` to the power of `exp`.

### Advanced Mathematical Functions

- `math_sqrt(num)`: Computes the square root of `num`.
- `math_log(num, base=ma.e)`: Computes the logarithm of `num` with optional base `base`.

### Trigonometric Functions

- `math_sin(x)`: Computes the sine of angle `x`.
- `math_cos(x)`: Computes the cosine of angle `x`.
- `math_tan(x)`: Computes the tangent of angle `x`.

### Factorial and Combinatorial Functions

- `math_factorial(n)`: Computes the factorial of integer `n`.
- `math_combinations(n, k)`: Computes the number of combinations of `n` items taken `k` at a time.

## String Manipulation Functions

### Basic String Operations

- `string_reversestring(string)`: Reverses the input string.
- `string_uppercase(string)`: Converts the input string to uppercase.
- `string_lowercase(string)`: Converts the input string to lowercase.

### String Analysis and Modification

- `string_count_vowels(string)`: Counts the number of vowels in the input string.
- `string_count_consonants(string)`: Counts the number of consonants in the input string.
- `string_is_palindrome(string)`: Checks if the input string is a palindrome.
- `string_alternate_case(string)`: Converts characters in the input string to alternate case.
- `string_title_case(string)`: Converts the input string to title case.

### String Utilities

- `string_remove_spaces(string)`: Removes spaces from the input string.
- `string_replace_spaces_with_underscore(string)`: Replaces spaces in the input string with underscores.
- `string_count_words(string)`: Counts the number of words in the input string.
- `string_reverse_words(string)`: Reverses the order of words in the input string.
- `string_add_prefix(string, prefix)`: Adds a prefix to the input string.
- `string_add_suffix(string, suffix)`: Adds a suffix to the input string.
- `string_remove_vowels(string)`: Removes vowels from the input string.
- `string_remove_consonants(string)`: Removes consonants from the input string.
- `string_add_frame(string)`: Adds a frame around the input string.

## Unit Conversion Functions

### Distance Conversion

- `conversion_kilometerstomiles(kilometers)`: Converts kilometers to miles.
- `conversion_milestokilometers(miles)`: Converts miles to kilometers.

### Weight Conversion

- `conversion_kilogramstodekagrams(kilograms)`: Converts kilograms to dekagrams.
- `conversion_dekagramstokilograms(dekagrams)`: Converts dekagrams to kilograms.
- `conversion_dekagramstograms(dekagrams)`: Converts dekagrams to grams.
- `conversion_gramstodekagrams(grams)`: Converts grams to dekagrams.
- `conversion_kilogramstograms(kilograms)`: Converts kilograms to grams.
- `conversion_gramstokilograms(grams)`: Converts grams to kilograms.

### Length Conversion

- `conversion_kilometerstometers(kilometers)`: Converts kilometers to meters.
- `conversion_meterstokilometers(meters)`: Converts meters to kilometers.
- `conversion_meterstocentimeters(meters)`: Converts meters to centimeters.
- `conversion_centimeterstometers(centimeters)`: Converts centimeters to meters.
- `conversion_meterstomillimeters(meters)`: Converts meters to millimeters.
- `conversion_millimeterstometers(millimeters)`: Converts millimeters to meters.
- `conversion_kilometerstocentimeters(kilometers)`: Converts kilometers to centimeters.
- `conversion_centimeterstokilometers(centimeters)`: Converts centimeters to kilometers.
- `conversion_kilometerstomillimeters(kilometers)`: Converts kilometers to millimeters.
- `conversion_millimeterstokilometers(millimeters)`: Converts millimeters to kilometers.

### Misc
- `documentation()`: Prints you the link for the documentation of Superpy. This function doesn't return anything, it instead prints.
---
