myinteger = 20
my_integer_2 = -293
print(type(myinteger))
print(type(my_integer_2))  # * this is to verify that these whole numbers are integers

sum_of_both_integers = (
    myinteger + my_integer_2
)  # * A simple arithmetic equation using concatenation with integers
print(sum_of_both_integers)

difference_of_both_integers = (
    myinteger - my_integer_2
)  # * A simple arithmetic equation by subtracting both variables (20 - -293) = 313
print(difference_of_both_integers)


multiplication_of_both_integers = (
    myinteger * my_integer_2
)  # * Using (*) to multiply both integers
print(multiplication_of_both_integers)


division_of_both_integers = (
    myinteger / my_integer_2
)  # * Using (/) to divide both integers to produce = ~ -0.068
print(division_of_both_integers)

myfloat = 282.31
my_float_2 = 17.69
sum_of_both_floats = (
    myfloat + my_float_2
)  # * Simple arithmetic equation using concatenation with floats
print(sum_of_both_floats)

difference_of_both_floats = myfloat - my_float_2  # * Using (-) to subtract both floats
print(difference_of_both_floats)

product_of_both_floats = myfloat * my_float_2  # * Using (*) to muliply both floats
print(product_of_both_floats)

division_of_both_floats = (
    myfloat / my_float_2
)  # * Using (/) to divide both floats to find ~15.959
print(division_of_both_floats)

# * RULE: If you add am integer with a float, the result is automatically converted to float

float1 = 35.5
integer1 = 10
sum_of_both_float_and_integer = float1 + integer1
print(sum_of_both_float_and_integer)
print(
    type(sum_of_both_float_and_integer)
)  # * This shows that the classification of the result is "Float"

# ---------------------------------->
# * complex arithmetic calculations

myint1 = 10
myint2 = 35

mod_int = (
    myint1 % myint2
)  # * The "Modulo Operator (%)" finds the remainder of both integers
print("Integer Modulo operator:", mod_int)

floordiv_ints = (
    myint2 // myint1
)  # * The "Floor Division (//)" divides the two numbers and returns the greatest integer less than or equal to the result.
print("Integer Floor Division:", floordiv_ints)

exp_ints = (
    myint1**myint2
)  # * The "Exponentiation (**)" raises a number to to the power of another
print("Integer Exponentiation:", exp_ints)

myfloat1 = 10.5
myfloat2 = 11.5
mod_float = (
    myfloat1 % myfloat2
)  # * The "Modulo Operator (%)" finds the remainder of both floats
print("Float Modulo Operator:", mod_float)

floordiv_floats = (
    myfloat2 // myfloat1
)  # * The "The Floor Division (//)" divides the two numbers (in this case, floats) and returns the greatest integer less than or equal to the result.
print("Float Floor Divison:", floordiv_floats)

exp_floats = (
    myfloat1**myfloat2
)  # * The "Exponentiation (**)" raises a number to to the power of another
print("Float Exponentiation:", exp_floats)


float_spam = (
    0.1 + 0.2
)  # * By adding both float variables, the answer is extensive (0.30000000000000004) instead of (0.3)
print(type(float_spam))
print(float_spam)

testint = 4003
converted_testint_to_float = float(
    testint
)  # * Float() function returns a floating-number constructed from a given number
print(type(converted_testint_to_float))
print(converted_testint_to_float)

testfloat = 428.837
converted_testfloat_to_int = int(
    testfloat
)  # * Int() function returns an integer-number constucted from a given number
print(type(converted_testfloat_to_int))
print(converted_testfloat_to_int)

# * You can also convert a string to an integer or float:
dummyfloat = "102"
dummyint = "4782"

converted_float = float(dummyfloat)
converted_int = int(dummyint)
print(converted_float, "    ", converted_int)

# * Now, round() rounds a number to the specified number of decimal points

score = 43.21
APscore = 4.9573

rounded_score = round(
    score
)  # * No appointed decimal will automatically round to the nearest integer
rounded_APscore = round(APscore, 2)  # * The "2" rounds to the nearest tenth
both_rounded = (
    f"rounded score is {rounded_score}, and rounded Apscore is {rounded_APscore}"
)
print(both_rounded)

# * Simple absolute values:
num = -762
abs_num = abs(num)
print(abs_num)

# * Simple power
result1 = pow(8, 3)  # * Which is equavilent to 2 ** 3
print("power: ", result1)

just_a_variable = pow(12, 2)
print(just_a_variable)
