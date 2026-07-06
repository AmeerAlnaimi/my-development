print(
    3 > 5
)  # * This operator ">" shows that 3 is greater than 5, which is certianly not the case; shows a "False" Boolean

print(
    5 == 5
)  # * This operator "==" tells us that 5 is equal to 5, which will show a "True" boolean
print(
    5 > 3
)  # * Shows that the operator ">" shows the 5 is greater than 5, which is true and hence show a "True" boolean

print(
    5 != 5
)  # * The operator "!=" shows that 5 is NOT equal to 5, which is not the case and hence wil show an outcome of a "False" boolean

print(
    6 >= 6
)  # * The operator ">=" shows that 6 is GREATER OR EQUAL to 6, which is the correct and will give an output of a "True" boolean
print(
    6 <= 5
)  # * The operator "<=" shows that 6 is LESS OR EQUAL to 5, which is incorrect and will show an output of a "False" boolean

print(5 <= 4)


robot = 20 == 20
if robot is True:
    print("CORRECT!")
else:
    print("No, you are incorrect")


age = 78  # * Change this to practice the conditionals!
if age > 34:
    print("The age of that individual is older than 34.")
else:
    print("This individual is NOT older than 34")

leaderboard = "In progress"
if leaderboard:
    pass  # Focus on attributing this on my open-source game later. (recommended time 11 PM tomorrow, 3/2/2026 GMT+ 8)

robux = 1800
if robux >= 10000:
    print("You are Rich")
else:  # * The "else" clause only activates when a conditional returns and FALSE boolean.
    print("You are not Rich enough, hence please leave this server immediately")

status_rank = 7
if status_rank >= 10:
    print("You are an elite individual")
elif (
    status_rank >= 7
):  # *  the "elif" keyword adds another condition for variety and access for multiple conditionals if needed. Furthermore you can add an unlimited amount of "elif"
    print("You are a pro individual")
elif status_rank >= 4:
    print("You are an intermediate player")
else:
    print("You are a noob")
