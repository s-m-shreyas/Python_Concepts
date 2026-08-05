"""
A while loop is an iterative control flow statement 
that repeatedly executes a block of code as long as a 
specified condition evaluates to True. 
The loop terminates when the condition becomes False.

Why Do We Need a While Loop?

Suppose you want to print numbers from 1 to 5.

Without a loop:

print(1)
print(2)
print(3)
print(4)
print(5)

This works, but what if you want to print 1 to 10,000?

Writing 10,000 print() statements is impossible.

A loop solves this problem.
"""
# Ex->

num = 1

while num <= 5:
    print(num)
    num += 1


"""
o/p->

1
2
3
4
5
"""

# How it worked internally ->

"""
num = 1

      │
      ▼
Is num <= 5 ?

      │
   True
      │
Print num
      │
num = num + 1
      │
Go back and check condition again


num = 6

6 <= 5

↓

False

↓

Loop Ends

Flow diagram ->


          Start
             │
             ▼
     Check Condition
             │
      ┌──────┴──────┐
      │             │
    True         False
      │             │
 Execute Block    Exit Loop
      │
      └───────▲
              │
      Check Condition Again
"""

"""
Use Cases of While Loop

A while loop is used when the number of iterations is unknown and execution should continue until a condition changes.

1. User Input Validation

Keep asking until the user enters the correct value.
"""
# Ex->

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted")
