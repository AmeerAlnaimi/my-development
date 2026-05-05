my_integer_var = 4.21
print("float:", my_integer_var)

# * Just testing different data types

boolean_var = False
print("Boolean", boolean_var)


set_var = {67, "joke relax", 67.67}
print("set variable", set_var)

dictionary_var = {"name": "John", "age": 25}
print("dictionary variable:", dictionary_var)

tuple_var = (67, "hello", 91.5)
print("tuple variable", tuple_var)


range_var = range(7)
print("range:", range_var)

my_list = [22, "Just programming:)", 22.344, False]
print("List:", my_list)

none_var = None
print("None variable:", none_var)


print(type(range_var))  # * The type feature identify the data type of
print(type(dictionary_var))  # * the variable

isinstance("hello world", str)

my_string_2 = "Welcome people!"
print(
    "Welcome" in my_string_2
)  # * "IN" is an operator that returns a boolean (True or False) whteher the character or characters exist in the string.
print(
    isinstance(my_string_2, str)
)  # * 'Isinstance' checks the type of function you place for a variable.

print(
    len(my_string_2)
)  # * "len" fuction shows the enitre length of a string  (e.g. 15 total characters in this case)
print(
    my_string_2[0]
)  # * the '[]' selects a specific character of a string    NOTE that it starts from 0, not 1. (e.g. [0] is W, [1] is e)
