#LCM




print("edited for git")
print("edited for git")



#HCF
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)

a=int(input())
b=int(input())
x=hcf(a,b)
print(x)
