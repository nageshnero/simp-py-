
upper_limit = 45
n3 = 0
a = 2
print("printing the pythagorean triplets till the upper limit", upper_limit, ":")
while(n3 < upper_limit):
    for b in range(1, a+1):
        n1 = a*a-b*b
        n2 = 2*a*b
        n3 = a*a+b*b
        if(n3 > upper_limit):
            break
        if(n1 == 0 or n2 == 0 or n3 == 0):
            break
        print(n1, n2, n3)
    a = a+1