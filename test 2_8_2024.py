#anagram

def ana(a ,b):
    a=sorted(a)
    b=sorted(b)
    if(a==b):
        print("it's an anagram")
    else:
        print("its not a anagram")
a=str(input("enter the first word : "))
b=str(input("enter the second word : "))
ana(a,b)

#multiplication
def mul(n):
 for i in range(1,11):
     print(n,"x",i ,"=" ,n*i)
n=3
mul(n)

#reverse an string
def reverse(x):
   y =x[::-1]
   return y
x = str(input(" enter the string"))
print (reverse(x))

#ascending
def ased(c):
  d=sorted(c)
  return d
c=[9,7,5,3,1]
print(" ascending order :", ased(c))

#descending
def des(e):
 f=sorted(e)
 g=reverse(f)
 return g
e=[6,7,8,9,10]
print(" descending order :",des(e))






