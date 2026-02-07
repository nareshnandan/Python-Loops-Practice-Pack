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

# 6) Print numbers using while loop (1 to 5)
i = 1
while i <= 5:
    print(i)
    i += 1

# 7) Countdown from 10 to 1 (while loop)
i = 10
while i >= 1:
    print(i)
    i -= 1

# 8) break example (stop loop when number is 7)
for i in range(1, 20):
    if i == 7:
        break
    print(i)

# 9) continue example (skip number 5)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 10) pass example (placeholder)
for i in range(3):
    pass

print("Loop finished (pass did nothing)")
