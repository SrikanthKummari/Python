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


'''
#input
enter a num
1000

#output
0 is Armstrong number
1 is Armstrong number
2 is Armstrong number
3 is Armstrong number
4 is Armstrong number
5 is Armstrong number
6 is Armstrong number
7 is Armstrong number
8 is Armstrong number
9 is Armstrong number
153 is Armstrong number
370 is Armstrong number
371 is Armstrong number
407 is Armstrong number
'''
