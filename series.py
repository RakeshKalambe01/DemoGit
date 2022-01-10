#series
#2 [0] 3 [1] 5 [1] 7 [2] 11 [3] 13 [5] 17 [8] 19 [13] 23 [21]...
def fun1(n):
    if n<0:
        print("enter valid number")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fun1(n-1)+fun1(n-2)
def fun2(n):
    prime_numbers = [2,3]
    i=3

    if(0<n<3):
        print(prime_numbers[n-1])
    elif(n>2):
        while (True):
            i+=1
            status = True
            for j in range(2,int(i/2)+1):
                if(i%j==0):
                    status = False
                    break
            if(status==True):
                prime_numbers.append(i)
            if(len(prime_numbers)==n):
                break
        print(prime_numbers[n-1])


n=int(input())

if n%2==0:
    print(fun1(n//2))

else:
    fun2(n//2+1)
