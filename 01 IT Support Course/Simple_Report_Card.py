name = "John"
print(name, type(name))

age = 19
print(isinstance(age, int))

score = 24.1
print(score, type(score))

print(name, "and is", age, "and has the score of", score)

print(
    "John" in name
)  # * The "in" operator returns the boolean (True of False condition) that specifies whether the character or characters exist in the string

mylenth = "My name is Ameer"
print(len(mylenth))
print(
    mylenth[1]
)  # * This is to find a specific character in the string. NOTE that it starts from 0 (e.g. M rather than y)
