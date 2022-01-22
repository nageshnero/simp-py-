def maxnumbers(n):
    list= []
    for i in range(0,n):
        list.append(n)
    print(list)
    print("first max number in the array", max(list))

    print("second max number in the array", min(list))

userinput=int(input("enter number of the elements:"))
maxnumbers(userinput)
