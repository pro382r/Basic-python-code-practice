x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

for num in numbers:
    if num == 3:
        continue
    print(num)
