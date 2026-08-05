"""
Conditional statements are control flow statements
that execute different blocks of code based on
whether a specified condition evaluates to True or False.
"""

# Why are Conditional Statements Needed?
'''A program always executes every line sequentially.'''

age = 15

print("Welcome")
print("You can vote")
print("Program Ended")

# output
'''
Welcome
You can vote
Program Ended

note: This is incorrect because a 15-year-old cannot vote.
'''

# Instead, we use a conditional statement.

age = 15

if age >= 18:
    print("You can vote")

print("Program Ended")

# output
'''
Program Ended

note: The program now makes a decision based on the value of age.
'''

# Example:

marks = 82
attendance = 90
sports = True

# ---------- Independent if Statements ----------

if attendance >= 75:
    print("Attendance Requirement Met")

if sports:
    print("Eligible for Sports Certificate")

# ---------- if-elif-else Chain ----------

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")


# output

'''
Attendance Requirement Met
Eligible for Sports Certificate
Grade B
'''

# Note:
'''
| Multiple `if` Statements                           | `if-elif-else` Chain                                                         |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| Every condition is checked independently.          | Conditions are checked one by one until the first `True` condition is found. |
| Multiple blocks can execute.                       | Only one block executes.                                                     |
| Python does **not** stop after a `True` condition. | Python stops after the first `True` condition.                               |
| Used when multiple conditions may all be true.     | Used when only one outcome should be selected.                               |
'''