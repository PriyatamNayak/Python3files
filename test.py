for i in range(2,15):
  print(i)





"""
x=3;
y=2;
print("sum is:", x+y);
print("diff is:",x-y);
print("mul is:",x*y);
print("div is:",x/y);
print("quotient is:",x//y);
print("rem is:",x%y);
print("power is:",x**y);

"""

"""
while True:
    x ,y= int(input("Enter 1st number:")), int(input("Enter 2nd number:"));
    print("sum is:",x+y);
    print("diff is:",x-y);
    print("mul is:",x*y);
    print("div is:",x/y);
    print("quotient is:",x//y);
    print("rem is:",x%y);
    print("power is:",x**y);
    z = input("continue or stop: 'y' / 'n' : ");
    if z == 'n' or z != 'y':
        break;
"""

"""
while True:
     print ("Options:");
     print (" 1. Add           2. Subtract  \n 3. Multiply     4. Divide\n 5. Power       6.Remainder");
     z = int(input(":"))
     try:
               if z == 1:
                    a ,b = float (input("enter 1st no.:")) , float (input("enter 2nd no.:"))
                    print ("sum is: ", a+b)
                    
               elif z == 2:
                     a ,b = float (input("enter 1st no.:")) , float (input("enter 2nd no.:"))
                     print ("difference is: ", a-b)

               elif z == 3:
                     a ,b = float (input("enter 1st no.:")) , float (input("enter 2nd no.:"))
                     print ("product is: ", a*b)

               elif z == 4:
                     a ,b = float (input("enter 1st no.:")) , float (input("enter 2nd no.:"))
                     print ("division is: ", a/b)

               elif z == 5:
                     a ,b = int (input("enter 1st no.:")) , int (input("enter 2nd no.:"))
                     print ("power is: ", a**b)

               elif z == 6:
                     a ,b = float (input("enter 1st no.:")) , float (input("enter 2nd no.:"))
                     print ("remainder is: ", a%b)

               elif z == 'n':
                     break;
                     
               else:
                     print ("option not available")

     except:
               print("invalid input!!")
"""
          
          
"""
def fact(x):
     factorial  = 1 
     for i in range(1,x+1):
          factorial = factorial * i
     print("factorial is:",factorial)

val = int (input ("enter a number:"))
fact(val)
"""          


"""
try:
     #filename = input ("enter a filename:")
    # f = open(filename+".text","a")
     f = open("fileh.text","a")
     data = input ("\nwhat u want to enter in the file:")
     f.write(data)                                                                                  #writes the data into the file
     print ("file is created.")                                                      

     f = open("fileh.text","r") 
     print ("reading data:")
     print(f.read())                                                                                #reads the data from the file
     f.close()
except:
     raise
"""



"""
#swapping values without third variable
def swap(x,y):
     x = x/y        #x+y   or   x*y    or     abs(x-y) 
     y = x*y        #x-y   or   x/y    or     x+y
     x = y/x        #x-y   or   x/y    or     abs(x-y)
     print("after swapping-")
     print ("x=",x), print ("y=",y)

x,y = int(input("enter 1st no.: ")), int(input("enter 2nd no.:"))
print("before swapping-")
print ("x=",x),print ("y=",y)
swap(x,y)
"""


"""
#counting characters and percentage of characters in sentence
def count_char(text,char):
     count=0
     for c in text:
          if c == char:
               count+=1
     return count
z = input("enter a string:")
c = input("enter the character u want to count:")
a = count_char(z,c)
print(a)
for char in "abcdefghijklmnopqrstuvwxyz":
     perc = 100 * a/ len(z)
print("{0}-{1}%".format(c,round(perc,2)))
"""


"""
def fact(x):
     if x == 1 :
          return 1
     else:
          return (x * fact(x-1))

a = int(input("enter a no.:"))
print(fact(a))
"""


"""
class animal:
     def __init__(self,name,color):
          self.name = name
          self.color = color

class  dog(animal):
     def sound(self,value):
          self.value = value

s = animal("rocky","green")
print(s.name)
a = dog("tuffy","brown","bark")
print(a.name)
print(a.sound)
"""