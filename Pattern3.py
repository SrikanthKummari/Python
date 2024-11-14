n = int(input("enter number of rows\n"))

for row in range(n):
    for col in range(n):
        if col == 0 or row == (n-1) or col == row :
            print("*",end="")
        else:
            print(end=" ")
    print()

'''
#input
enter number of rows
5

#output
*    
**   
* *  
*  * 
*****
