one, two = input().split(' ')
one  = int(one)
two = int(two)
if one % two == 0:
    print("yes %i" %(one/two))
else:
    for i in range(two, one+1):
        if one % i == 0:
            print("no %i" %(i - two))
            break