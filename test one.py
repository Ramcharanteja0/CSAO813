#string to integer 
a="45"
b=int (a)
print(a)
#duplicates 
a=[1,2,3,4,3,2]
b=list(set(a))
print(b)
#average 
a=[1,4,6,8]
b=sum(a)/4
print("average: ",b)
#perfect number 
def check(n):
 for i in range(1,n+1):
  if(i*i==n):
    print("perfect square")
  else:
    print("not a perfect square")
a=9
check(a)
#sum of even  numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers in the list:", even_sum)
#divisible by 5 or 3 
n=int (input("enter the number "))
if (n%5==0):
    print ("its divisible by 5")
elif(n%3==0):
        print("its divisible by 3")
else :
     print(" its not divisible by 5 an d 3 ")
#vowel or consonant
x="r"
if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print( "its an vowel")
else :
    print (" its a consonant ")
