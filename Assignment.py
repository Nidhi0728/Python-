import sys
from array import *

'''
Quetion-1
program to add,sub ,ultiple,divide two numbers
'''

a= int(input("enter first number="))
b= int(input("enter second number="))
print("addition of two number is=",(a+b))
print("addition of two number is=",(a-b))
print("addition of two number is=",(a*b))
print("addition of two number is=",(a/b))
'''
Question-2
uese if condition to find biggest of 3 numbers
'''

a=input("fisrt number=")
b=input("second number=")
c=input("third number=")
if a>b and a>c:
    print("Biggest no is="+a)

elif b>c:
    print("biggest no is="+b)
else:
    print("biggest no is="+c)
'''
Question-3
'''
num=int(input("enter a number="))
if num%2==0:
    print("even number")
else:
    print("odd one")
'''
Question-5
How to take input from command line
" argv" is a array basically which is uesd to take
 input from command line
'''
a=sys.argv[1]
b=(sys.argv[2])
c=sys.argv[3]
d=sys.argv[4]
e=sys.argv[5]
print("five values are="+a+"\t"+b+"\t"+c+"\t"+d+"\t"+e+"\t")
if a>b and a>c:
    print(" %s is biggest number"%a)

elif b>c:
    print("%s is Biggest number"%b)
else:
    print("%s is Biggest one"%c)'''

'''
Question-6
String Realted Question '''
'''
name="nidhi"
for i in name[:]:
    print("value="+i+"\n")

name1=name[1:4]
print(name1)
print(type(name1))
result=name+name1
print(result)
'''
using repeatition operator "*"
'''
print(name * 100)
print("nidhi \t" *100)
'''
Question-7,8
'''
List Regarding Question 

list1=[2,4,5,6,7,8,9,12,13,14]
print(list1)
print(list1[0:5])
list2=['nidhi','khushi','pappu']
final=[list1,list2]
print(final)
print(list1*4)
tup=('nidhi','nidss','nidh')
print(tup*7)
'''
Question-10
Assignment Operator regarding question
'''

a=10
a+=3
print(a)
b=40
b-=20
print(b)
c=12
c*=3
print(c)
d=45
d/=7
print(d)
e=46
e%=3
print(e)
f=4
f**=2

print(f)
'''
floor Division gives only integer part
'''

h=45
h//=7
print(h)

'''
Question-12
'''
arr=array('i',[])
n=10
for i in range(10):
    x=int(input("enter values"))
    arr.append(x)
    
avge=(arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9])/10
print(avge)
for i in arr[:]:
    if i<avge:
        print("value is=",i)
    elif i>avge:
        print("greater value is=",i)
    else:
        print("equal=",i)
'''
Question-13
'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
else:
    if b>c:
        if b>d:
            print(b)
        else:
            print(d)
           
    else:
        if c>d:
            print(c)
        else:
            print(d)
'''
Question-14
'''
listA=[1,2,3,4,5,6,7,8,9,10]
listB=['nid','nidhi','n','a','khusi','c','s','p','q','neha']
for i in listB:
    print(i)
r=int(input("give index value"))
i=0
while i<10:
    if i==r:
       a =listA.pop(i)
       print("Employee id on given index=",a)
    i=i+1
i=0
while i<10:
    if i==r:
       a =listB.pop(i)
       print("Employee Name on given index=",a)
    i=i+1
for i in listB[4:10]:
    print(i)
for i in listB[3:]:
    print(i)
n=int(input("enter a value for repeat the list"))
print(listB*n)
listfinal=[listA,listB]
print(listfinal)
'''
question no-15
'''
lista=['mango','apple','nidhi','fruit','nano']
if 'mango' in lista:
    print("yes mango is in list")
else:
    print("not present in list")
for i in lista[::-1]:
    print(i)
i=0
a='mango'
while i<5:
    if lista[i]==a:
        print("yes it is")
        break
    else:
        print("not yet")
    
    i=i+1
'''
Question-16
'''
num=5
i=1
count=0
while i<=6:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
        print("prime number")

        
num=int(input("give a value"))
i=1
total=0

while i<=num:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        total=total+1
    i=i+1
print(total)
'''
Question number 18
'''

i=1
while i<=100:
    print(i)
    i+=1
i=100
while i>=1:
    print(i)
    i-=1
for i in range(1,101,1):
    print(i)

mystring="hello world"
for i in mystring:
    print(i)

'''
question no 19-a,b
'''
for i in range(1,101,1):
    if i%2==0:
        print("even nu=",i)
    else:
        break
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in range(1,101,1):
    if i%2!=0:
        continue
    else:
        print(i)
print("#################################")
for i in range(1,101,1):
    if i%2==0:
        pass
    else:
        print("odd5 nu=",i)
for i in range(1,101,1):
    if i==50:
        break
print("bye")
for i in range(1,101,1):
    if i==10 or i==20 or i==30 or i==40 or i==50:
        continue
    else:
        print(i)
print("last")
for i in range(100,0,-1):
    print(i)
        
        
        
        
        
        
    
    



    


        
            

    
    

    
        
    

    
    
    
        
    

        
        
    

    
        
        
       
            

        









