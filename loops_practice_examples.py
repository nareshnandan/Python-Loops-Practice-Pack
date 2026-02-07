# 1) Print "Hello" 5 times (for loop)
for i in range(5):
    print("Hello!")

# 2) Print numbers 1 to 10 (for loop)
for i in range(1, 11):
    print(i)

# 3) Print even numbers between 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 4) Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)

# 5) Print multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
