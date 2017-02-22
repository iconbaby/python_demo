for x in list(range(101)):
    print(x)

sum = 0

for y in list(range(101)):
    sum += y

print(sum)

sam = 0
n = 99
while n > 0:
    sam += n
    n -= 2
print(sam)

s = 0
while s <= 10:
    s = s + 1
    if s % 2 == 0:
        continue
    print(s)
