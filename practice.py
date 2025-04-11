
#Q1

a=10
b=10.6
c="hello"
d=True
e=[1,2,3,4,5]
f=(1,2,3,4,5)
g=True
h={'a':1,'b':2,'c':3,'d':4,'e':5}
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)
print(type(g),g)
print(type(h),h)
#Q2
list1=[1,2,3,4,5]
list1[2]=100
list1.append(200)
list1.pop(0)
print(list1)

#Q3
d1={'name':'John','age':25,'city':'New York'}
d1['gender']=('male')
del d1['city']
print(d1)

#Q4
'''
t=(1,2,3,4)
t[2]=100 # This will raise an error because tuples are immutable
print(t)
'''
#Q5
string='Python Programming'
print(string[0:6])
print(string[-6:])
print(string[::2])

#Q6

a= int(input("Enter a number: "))
if a<0:
    print("Negative")
elif a==0:
    print("Zero")   
else:
    print("Positive")
    
#Q7

b= int(input("Enter a number: "))
if b%2==0:
    print("Even")
else:
    print("Odd")    

#Q8


marks= int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=89 and marks>=75:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade C")
elif marks<50:
    print("Grade D")
else:
    print("enter the correct marks. it should be between 1-100")

#Q9

age= int(input("Enter your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
#Q10

p=int(input("Enter the number for p: "))
r=int(input("Enter the number for q: "))
t=int(input("Enter the number for t: "))
if p>r and p>t:
    print("p is greater than r and t")
elif r>p and r>t:
    print("r is greater than p and t")
elif t>p and t>r:
    print("t is greater than p and r")
else:
    print("all are equal")

#Q11

n=int(input("Enter the number: "))
for i in range(0,n+1):
    print(i)

#Q12

j=int(input("Enter the number: "))
total=0
for i in range(1,j+1):
    total+=i
print("sum",total)

#Q13

number=int(input("Enter the number: "))
for i in range(1,11):
    print(number,"*",i,"=",number*i)


#Q14

num1=int(input("Enter the number: "))
factorial=1
for i in range(1,num1+1):
    factorial*=i
print("Factorial of",num1,"is",factorial)


#Q15


text=str(input("Enter the string: "))
reversed_text=text[::-1]
print("Reversed string is",reversed_text)