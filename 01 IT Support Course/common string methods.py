mystring = "hi guys"
uppercasemystring = mystring.upper()  # * Converts the string to uppercase letters
print(uppercasemystring)

# -------------------

mystring2 = "WHY ARE YOU GUYS hEre?"
lowercasemystring2 = mystring2.lower()
print(lowercasemystring2)

# -------------------

mystring3 = "       nice guys             "
trimmedmystring3 = (
    mystring3.strip()
)  # * "strip" method removes the leading or trailing characters removed.
print(trimmedmystring3)

# -------------------

greeting = "Hello guys"
replacedgreeting = greeting.replace(
    "Hello", "Yo"
)  # * "replace" method returns a new string with all occurances of "OLD" replaced by "NEW"   SYNTAX: replace(OLD, NEW)
print(replacedgreeting)

# -------------------

unknownguest = "Is that the goat?"
split_words = (
    unknownguest.split()
)  # * "split" splits a string on a specific separator into a list of strings.
print(split_words)


# -------------------

mylist = ["hello", "people", "of Tribe1"]
joinedmylist = " ".join(
    mylist
)  # * join(iterable) joins elements of iterable into a string with a seperator  #ONLY strings are permitted
print(joinedmylist)

# -------------------

holidays = "Sunday and Monday"
startswithprefixholidays = holidays.startswith(
    "Sunday"
)  # * startswith(prefix) returns a boolean indicating if a string starts with a specified prefix
print(startswithprefixholidays)

# -------------------

weekdays = "Thursday and Friday"
endswithsuffixweekdays = weekdays.endswith(
    "Wednesday"
)  # * endswith(suffix) returns a boolean indicating if a string ends with a specified suffix NOTE that the outcome is false as it ends with Friday, not Wednesday
print(endswithsuffixweekdays)

# -------------------

months = "April and June"
findmonths = months.find(
    "June"
)  # * find(substring) returns an index of the occurence of the first "substring" or "-1" if it cannot find the specified string.
print(findmonths)

asaying = "Old is Gold"
countasaying = asaying.count("O") + asaying.count(
    "l"
)  # * count(substring) returns the number of times a substring appears in a string NOTE that I added both "O" and "l"
print(countasaying)
# -------------------

ideology = "communisM"
capitilized_idealogy = (
    ideology.capitalize()
)  # * capitilized() returns a new string a the first character capitilized and the last character lowercased.
print(capitilized_idealogy)

# -------------------

fun = "YEPPI"
isupperfun = (
    fun.isupper()
)  # * isupper() Returns "True" if all characters in the string are uppercased/capitilized
print(isupperfun)

notfun = "noo"
islowerfun = (
    notfun.islower()
)  # * islower() Returns "true" if all characters in the string are lowercased
print(islowerfun)

# -------------------

author = "docter murphy junior"
tittleauthor = (
    author.title()
)  # * Returns a new string were all first words are capitilized/uppercase
print(tittleauthor)
