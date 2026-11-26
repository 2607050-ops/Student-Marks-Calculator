a=int(input("enter the mark of python"))
b=int(input("enter the mark of physics"))
c=int(input("enter the mark of maths"))
T=a+b+c
print ("total mark is", T)
av=T//3
print ("average mark is", av)
if av >=80:
  print("grade A")
elif av <80 and av>=60:
  print("grade B")
else :
  print ("grade C")
