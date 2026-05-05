string1 = "Hello"
string2 = "World"
stringofboth = string1 + " " + string2
print(stringofboth)

# ----------------------------------------
name = "Jeff"  #! THIS IS WRONG AS IT ONLY CONCATENATE STRINGS, NOT INTEGERS. SO add 'str' to the string 'age' to convert the integer to a string
age = 47
nameandage = name + " " + str(age)
print(nameandage)
# ----------------------------------------
# * combining both string concatenation and augmentation (+=)
string3 = "Hello"
string4 = 69
string3and4 = string3 + " "
string3and4 += str(string4)
print(string3and4)
# ----------------------------------------
# * Personal learning for augmentation.
score = 100
print("starting score:", score)
score += 10
print("Additional of 10 scores for completing a side task:", score)
score *= 2
print("Final outcome score:", score)
# ----------------------------------------

# * String interpolation: is a process of inserting a variable and expression into a string.
# * Furthermore, "F" or "f" is an F-string (Formatted strings literal) that starts before the quotes.
parentname = "Baze"
parentage = 93
parentnameandparentage = (
    f"My parent's name is {parentname}, and my parent's age is {parentage}"
)
print(parentnameandparentage)
# ----------------------------------------
# * String Interpolation + String Concatenation with augmentation | Numbers
num1 = 32.2
num1 += 10  # * adds 10 to 32.2 = 42.2
num3 = 10
num3 *= 2  # * Multiplies 2 with 10 = 20
num1andnum3 = f"the number of num1: {num1} and the number of num3: {num3}. Now by multiplying between num1 and num3, the answer is = {num1 * num3}"
print(num1andnum3)
