def anagram(a,b):
    n=sorted(a)
    m=sorted(b)
    if(m==n):
        return "it is anagram"
    else:
        return "not anagram"
a=str(input("enter the first  word "))
b=str(input("enter the second word "))
print(anagram(a,b))
