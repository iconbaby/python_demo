# a = (x for x in range(10))
# for b in a:
#     print(b)
#     print


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# for n in fib(6):
#     print(n)
def triangles():
    L = [1]
    n = 0
    while n < 0:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n += 1


for x in triangles():
    print(x)

print(list(range(2)))