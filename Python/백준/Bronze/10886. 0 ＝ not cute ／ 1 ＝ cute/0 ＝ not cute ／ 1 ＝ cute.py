n = int(input())
choice = 0

for i in range(n):
    num = int(input())

    if(num==0):
        choice -= 1
    else:
        choice += 1

if choice<0:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")