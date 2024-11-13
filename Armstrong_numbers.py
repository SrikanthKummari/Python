num = int(input("enter a num\n"))

for i in range(num):
    n = i
    arm = 0
    l = len(str(i))
    while(n>0):
        d = n%10
        arm += d**l
        n = n//10

    if arm == i:
        print(i, "is Armstrong number")
