#write an programm to print an difference between the two lists
def differ (p , o ):
  i=sorted(p)
  j=sorted(o)
  s=list[set(i)-set(j)]
  return s
p =[1,2,3,4]
o=[3,4,5,6]
print(" difference :",differ(p,o))
