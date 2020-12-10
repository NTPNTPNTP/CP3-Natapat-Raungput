number = int(input())
space = number-1
for i in range(1, number+1):
    print(' ' * space + '*' * (2*i - 1))
    space -= 1
