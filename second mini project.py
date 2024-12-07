# CTRL + F (for stupides (it's you) ) 

x = "Salam"
y = "Xanlar" 
print(x,end=" ") 
print
# output
# Salam Xanlar

x = "Salam"
y = "Xanlar"
print(x, y,sep="------")
# output
# Salam------Xanlar

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#If else

x = 10 
y = 10

if x>y :
    print ("x is greater then y")
    print ("x ->", x ,"y->", y)
elif x==y:
    print ("x=y")
else :
    print ("y is greater then x")

print ("Test statement")
# output
# x=y
# Test statement

age = 17
if age >18:
    print ("Adult")
elif age == 18:
    print ("=18")
else:
    print ("younger")
# output
# younger

x= True
y= False
print("And",x and y)
print("OR",x or y)
print("NOT",not y)
print("NOT",not x)
# output
# And False
# OR True
# NOT True
# NOT False

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Loop -> for, while

count = 0
while count<5:
    print ("count : ",count)
    count+=1
# output
# count :  0
# count :  1
# count :  2
# count :  3
# count :  4
               
#range (start,end_of_range,increment)
for i in range(5):
    print("Iteration: ",i)
# output
# Iteration:  0
# Iteration:  1
# Iteration:  2
# Iteration:  3
# Iteration:  4

for i in range(2,5):
    print("Iteration: ",i)
# output
# Iteration:  2
# Iteration:  3
# Iteration:  4

for i in range(2,10,2):
    print("Iteration: ",i)
# output
# Iteration:  2
# Iteration:  4
# Iteration:  6
# Iteration:  8

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LIST -> A R R A Y
data = [10,"salam",True,19.99,45,23.3]
print(data)
# output
# [10, 'salam', True, 19.99, 45, 23.3]

print(len(data))
# output
# 6

print(data[-1])
# output
# 23.3

print(data[1:5:2])
# output
# ['salam', 19.99]

print(data[::-1])
# output
# [23.3, 45, 19.99, True, 'salam', 10]

for item in data:
    print(item,end=" ")
# output
# 10 salam True 19.99 45 23.3

for item in data:
    print(item)
# output
# 10
# salam
# True
# 19.99
# 45
# 23.3

for i in range(0,len(data)-1,2): 
    print(data[i])
# output
# 10
# True
# 45

data[0] = False
print(data)
# output
# [False, 'salam', True, 19.99, 45, 23.3]

data.append(500)
print(data)
# output
# [False, 'salam', True, 19.99, 45, 23.3, 500]

data.insert(3,500)
print(data)
# output
# [False, 'salam', True, 500, 19.99, 45, 23.3, 500]

data.remove(19.99)
print(data)
# output
# [False, 'salam', True, 500, 45, 23.3, 500]

data.pop()
print(data)
# output
# [False, 'salam', True, 500, 45, 23.3]

data.pop(3)
print(data)
# output
# [False, 'salam', True, 45, 23.3]

number=[1,2,3,4,5]
names=["John","Bob","Alice"]
student= [1,"john",True,1.7]

for num in number:
    print(num)
# output
# 1
# 2
# 3
# 4
# 5
for range in names:
    print(range)
# output
# John
# Bob
# Alice

for data in student:
    print(data)
# output
# 1
# john
# True
# 1.7

import numpy as np

number_array = np.array([1,2,3,4,5])
print(number_array)

for num in number_array:
    print(num)
# output
# [1 2 3 4 5]
# 1
# 2
# 3
# 4
# 5

size = int(input("Enter the size:"))

import numpy as np

arra_data = np.array([])

print ("Enter values for the numpy array:")

for _ in range(size):
    value = float(input("Enter value:"))
    array_data =np.append(array_data,value)

print("Array_data ->",array_data)
# output
# Enter the size:3
# Enter values for the numpy array:
# Enter value:2.4
# Enter value:5.2
# Enter value:3.6
# Array_data -> [2.4 5.2 3.6]

size = int (input("Enter the size"))
list_data = []

print("Enter the values for the list:")

for _ in range(size):
    value = input()
    list_data.append(value)

print("list_data -",list_data)
# output
# Enter the size3
# Enter the values for the list:
# 24
# 45
# 67
# list_data - ['24', '45', '67']

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# STRING
a = 'salam xanlar'
print(len(a))
# output
# 12

for i in a:
    print(i)
# output
# s
# a
# l
# a
# m
# 
# x
# a
# n
# l
# a
# r

print(a[:])
# output
# salam xanlar

print(a[::3])
# output
# saxl

print(a[-6:-2])
# output
# xanl

print(a.upper())
# output
# SALAM XANLAR

print(a.lower())
# output sozleri balaca edir
# salam xanlar

print(a.swapcase())
# output sozlerin tersi gosterir
# SALAM XANLAR

print(a.isupper())
# output sozlerin hamsinin boyuk herfle olgunu yoxlayir
# False

print(a.islower())
# output sozlerin hamsinin balaca herfle olgunu yoxlayir
# True

print(a.capitalize())
# output sozlerden ilk sozun ilk herfini boyuk edir 
# Salam xanlar

print(a.title())
# output sozlerin her birinin ilk herfini boyuk edir 
# Salam Xanlar

print(a.split(" "))
# output sozlerin her birinin ilk herfini boyuk edir 
# ['salam', 'xanlar']

metn = "Salam XANLAR Necesen piS"

boyukherfler = 0
kicikherfler = 0
bosluqSayi = 0
for herf in metn:
    print("herf: "+ herf)
    if herf == ' ':
        bosluqSayi += 1
    elif herf.isupper():
        boyukherfler += 1
    elif herf.islower():
        kicikherfler += 1
        
print("bosluq sayi: ",bosluqSayi,"boyukherfler: ",boyukherfler,"kicikherfler: ",kicikherfler)
# output 
# bosluq sayi:  3 boyukherfler:  9 kicikherfler:  12

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

password = "computer"
password2 = "computer123"
password3 = "computer123!!!"
password4 = "computer!!!"
password5 = "123"
password6 = "!!!"

# isalpha, isnumeric, isalnum
print(password.isalpha())
print(password2.isalpha())
print(password3.isalpha())
print(password4.isalpha())
print(password5.isalpha())
print(password6.isalpha())
# outputs 
# True
# False
# False
# False
# False
# False

print(password.isnumeric())
print(password2.isnumeric())
print(password3.isnumeric())
print(password4.isnumeric())
print(password5.isnumeric())
print(password6.isnumeric())
# outputs 
# False
# False
# False
# False
# True
# False

print(password.isalnum())
print(password2.isalnum())
print(password3.isalnum())
print(password4.isalnum())
print(password5.isalnum())
print(password6.isalnum())
# outputs 
# True
# True
# False
# False
# True
# False

a = input("soz: ")
if a.startswith("123"):
    print("he")
# output 123 basliyibsa 
# he 
# yoxsa hecne 

if a.endswith("123"):
    print("he")
# output 123 bitibse
# he 
# yoxsa hecne 

password3 = "computer123!!!"
print("!" in password3)
# output 
# True

password3 = "salam xanlar"
print(password3.find("l"))
# output 
# 2

print(password3.index("x"))
# output 
# 6

print(password3.replace("l","a"))
# output 
# saaam xanaar

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary 

student = {
    "name":"Xanlar",
    "surname":"Kerimli",
    "age":2,
    "course":["frontend","backend"]
}
print(student)
# output 
# {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 2, 'course': ['frontend', 'backend']}

print(student["course"][1][3:])
# output 
# kend

print(student.get("name","melumat tapilmadi"))
# output 
# Xanlar 
# eger name olmasaydi melumat tapilmadi cixacakdi

student["age"] = 10
student.update({"age":10,"course":["frontend"]})
print(student)
# output 
# {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 10, 'course': ['frontend']}

ad = input("ad daxil edin: ")
soyad = input("soyad daxil edin: ")
yas = int(input("yas daxil edin: "))
telebe= dict(name = ad,surname = soyad,age= yas)
print(telebe)
# output 
# ad daxil edin: Xanlar (for exampla)
# soyad daxil edin: Kerimli (for exampla)
# yas daxil edin: 20 (for exampla)
# {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 20}

student = {
    "name":"Xanlar",
    "surname":"Kerimli",
    "age":2,
    "course":["frontend","backend"]
}

for i in student.keys():
    print(i)
# output 
# name
# surname
# age
# course
for i in student.values():
    print(i)
# output 
# 2
# ['frontend', 'backend']
    
for i in student.items():
    print(i)
# output
# ('name', 'Xanlar')
# ('surname', 'Kerimli')
# ('age', 2)
# ('course', ['frontend', 'backend'])

del student["course"]
print(student)
# output
# {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 2}

student.clear()
print(student)
# output
# {}

student.pop("age")
print(student)
# output
# {'name': 'Xanlar', 'surname': 'Kerimli', 'course': ['frontend', 'backend']}

student.popitem()
print(student)
# output
# {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 2}

print("name" in student)
# output
# True

print("Name" in student)
# output
# False

n = int(input("eded daxil edin: "))
myDictionary = {
    'a': 100, 
    'b': 200, 
    'c': 300
}

if n in myDictionary.values():
    print("eded var")
else:
    print("eded yoxdur")

# 1 output
# eded daxil edin: 200 (for example)
# eded var

# 2 coutput
# eded daxil edin: 12 (for example)
# eded yoxdur

adlar = ['Anar', 'Arzu']
qruplar = {
    "qrup1": ["Naile","Ramiz"], 
    "qrup2": ["Leman","Pervin"]
}
qruplar["qrup1"].append(adlar[0])
qruplar["qrup2"].append(adlar[1])
print(qruplar)
# output
# {'qrup1': ['Naile', 'Ramiz', 'Anar'], 'qrup2': ['Leman', 'Pervin', 'Arzu']}


person = {"name":"john",
          "age":28,
          "city":"Berlin"}

print("Dictionary ->",person)

for key in person :
    print (key,"->",person[key])
# output
# Dictionary -> {'name': 'john', 'age': 28, 'city': 'Berlin'}
# name -> john
# age -> 28
# city -> Berlin


size = int(input("Enter the size : "))
person = {}
print("Enter key value pairs for the dictionary")

for _ in range(size):
    key = input ("Enter key :")
    if key == 'age':
        value = int (input("Enter age: "))
    else:
        value = input ("Enter value :")
    
    person[key]= value

print("person ->",person)
# output
# Enter the size : 3
# Enter key value pairs for the dictionary
# Enter key :name
# Enter value :Xanlar
# Enter key :surname
# Enter value :Kerimli
# Enter key :age
# Enter age: 20
# person -> {'name': 'Xanlar', 'surname': 'Kerimli', 'age': 20}


people =[]

size = int (input("Enter the size of the people list"))

for i in range (1,size + 1):
    print("Enter details for person",i,":")
    name= input("Enter name:")
    age= int(input("Enter age : "))
    city = input("Enter city:")

    person_info={"name": name,
                 "age":age,
                 "city": city}
    people.append(person_info)

print("Info ->")

for person in people :
    print("Name :",person['name'],"age :",person['age'],"city",person['city'])

# output
# Enter the size of the people list2
# Enter details for person 1 :
# Enter name:Xanlar
# Enter age : 20
# Enter city:Baku
# Enter details for person 2 :
# Enter name:wqweqw
# Enter age : 20
# Enter city:Baku
# Info ->
# Name : Xanlar age : 20 city Baku
# Name : wqweqw age : 20 city Baku

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Functions
def x():
    print("Xanlar")
    
x()
# output
# Xanlar

def x():
    return "Xanlar"

print(x())
# output
# Xanlar

def showNumber(a):
    print(a)

showNumber(100)
# output
# 100

def showNumber(a,b):
    return a+b

print(showNumber(100,700))
# output
# 800

def func():
    print("Hello World")
    print("test ")

func()    
# output
# Hello World
# test 

def add(x,y):
    sum=x+y
    return sum

a = 10
b = 20
result = add(a,b)                 
#for a return in a func you should have a var
print (" Result :", result)  
# output
# Result : 30

def greet():
    print("Hello")
    print("World")

print ("test statement 1")
greet ()                          
#for a func with no return it can be directly written
print ("test statement 2")
# output
# test statement 1
# Hello
# World
# test statement 2

def toplama(eded2,eded1):
    return eded1+eded2

eded1 = int(input("Birinci eded: "))

eded2 = int(input("Ikinci eded: "))

print(toplama(eded2,eded1))
# output
# Birinci eded: 12 (for example)
# Ikinci eded: 102 (for example)
# 114
 
def showList(a):
    for i in a:
        print(i.upper())

a = ["white","black","red","green","blue"]

showList(a)
# output
# WHITE
# BLACK
# RED
# GREEN
# BLUE

def factorial(x):
     c = 1
     for i in range(1,x+1):
         c *= i
     print(c)

factorial(5)
# output
# 120

s=int(input("give a starting number:"))
e=int(input("give a end number:"))
i=int(input("give a how many numbers you want to increment:"))

def func(start,end,increment):
    add=0
    for i in range (start,end,increment):
        add=add+i
    
    return add

result = func(s,e,i)
print ("",result)
# output
# give a starting number:5
# give a end number:10
# give a how many numbers you want to increment:2
#  21

s=0
e=1
i=1

int(input("give a starting number:",s))
int(input("give a end number:",e))
int(input("give a how many numbers you want to increment:",i))
result = sum(s,e,i)
print ("",result)

def sum(start,end,increment):
    for i in range (start,end,increment):
        sum(start,increment)
    
    return sum
# output
# Give a starting number: 3
# Give an end number: 10
# How many numbers do you want to increment: 2
# Result: 24

def find_max(arr):              
    max_element = arr[0]                 
    for num in arr:                  
        if num > max_element:  
            max_element = num  

    return max_element                  

a = [3,4,5,6,7] 
print(find_max(a))
# output
# 7

def fibonacci(n):                          
    fib = [0]* (n+1)  #[0,0,0,0,0,0]                       
    fib [1] = 1                               

    for i in range (2 , n+1):              
        fib[i] = fib [i-1] + fib [i-2]      

    return fib[n]                         
# 0 1 1 2 3 5 8 13 21
print(fibonacci(8)) #burada fibonacci sirasinin 8ci ededini gosterir
# output
# 21 


def three_dimensional_sum(arr,len_i,len_j,len_k):
    total = 0                             
    
    for i in range(len_i):                      
        for j in range(len_j):                   
            for k in range(len_k):             
                total = total + arr[i][j][k]                           

    return total                                              

a = []


len_i = int(input("len i: "))
len_j = int(input("len j: "))
len_k = int(input("len k: "))
x = 0
for i in range(len_i):     
    j_arr = []                 
    for j in range(len_j):    
        k_arr = []                
        for k in range(len_k):       
            print(x,"ci eded: ")
            # a[i][j][k] = int(input())
            eded =  int(input())
            k_arr.append(eded)
            x+=1
        j_arr.append(k_arr)        
    a.append(j_arr)         

print(a)
print(three_dimensional_sum(a,len_i,len_j,len_k))
# output
# len i: 2
# len j: 3
# len k: 2
# 0 ci eded: 
# 43
# 1 ci eded: 
# 56
# 2 ci eded: 
# 45
# 3 ci eded: 
# 67
# 4 ci eded: 
# 45
# 5 ci eded: 
# 68
# 6 ci eded: 
# 4
# 7 ci eded: 
# 798
# 8 ci eded: 
# 43
# 9 ci eded: 
# 768
# 10 ci eded: 
# 23
# 11 ci eded: 
# 43
# [[[43, 56], [45, 67], [45, 68]], [[4, 798], [43, 768], [23, 43]]]
# 2003 

def linear_search(arr , target):               
    for num in arr:                               
        if num == target:                                               
            return True                                               
        
    return False                                                     

a = [3,4,5,6,7]  
search = int(input()) 
print(linear_search(a,search))
# output
# 5
# True

# [] - > list
# {} - > dictionary

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tuple

point=(10, 20)
for i in point:
    print(i)

print ("2nd Element : ",point [1])
# output
# 10
# 20
# 2nd Element :  20

coordinates = (10000,20000)
print ("coordinates - ",coordinates)
# this changing in tuples are gonna show errors 
coordinates[1]=22222        
# output
# error, tuple tipinde melumatlarin elementleri deyisdirilmir

tuple_data = tuple()

size = int(input("Enter the size:"))

for _ in range(size):
    value = int(input ())
    tuple_data += (value,)

print("Tuples -> ",tuple_data)
# output
# Enter the size:3
# 23
# 53
# 54
# Tuples ->  (23, 53, 54)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SET
# {} - > set

numbers = [1, 2, 3,5,2,4,1,7, 4, 5, 6, 7, 8, 9, 10]
print("evvelki: ",numbers)
# output
# evvelki:  [1, 2, 3, 5, 2, 4, 1, 7, 4, 5, 6, 7, 8, 9, 10]

numbers = list(set(numbers))
print("sonraki: ",numbers)
# output
# sonraki:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = {1, 2, 3,5,2,4,1,7, 4, 5, 6, 7, 8, 9, 10}
print(5 in numbers)
# output
# True

text = "PYTHON"
text = list(text)
print(text)
# output
# ['P', 'Y', 'T', 'H', 'O', 'N']

text = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
text = set(text)
x = "".join(list(text))
print(x)
# output
# KLZWXOSVHDTACPGIUQBNRYFEM

a = {"white","black","red","blue","green","yellow"}

print(a)
# output
# {'black', 'blue', 'yellow', 'green', 'white', 'red'}
a.add("purple")
a.add("pink")
print(a)

# {'black', 'purple', 'pink', 'blue', 'yellow', 'green', 'white', 'red'}

a.update(["purple","pink","black","orange",3547,83246,274856])
print(a)
# output
# {'red', 3547, 'green', 'purple', 274856, 83246, 'blue', 'yellow', 'white', 'black', 'orange', 'pink'}

a = {"white","black","red","blue","green","ieuryu","yellow"}
a.remove("ieuryu")
print(a)
# output eger setde "ieuryu" yoxdursa kod islemir
# eger setde "ieuryu" yoxdursa kod islemir
# {'green', 'yellow', 'red', 'white', 'blue', 'black'}

a = {"white","black","red","blue","green","ieuryu","yellow"}
a.discard("tqwr")
print(a)
# output
# eger setde "tqwr" yoxdursa kod yenede isleyir
# {'yellow', 'red', 'black', 'ieuryu', 'green', 'white', 'blue'}

a.clear()
print(a)
# output
# set()

unique_numbers={1,2,3,4,5,6,7}
print("unique numbers - ",unique_numbers)
for num in unique_numbers:
    print(num)
# output
# unique numbers -  {1, 2, 3, 4, 5, 6, 7}
# 1
# 2
# 3
# 4
# 5
# 6
# 7

size = int(input("Enter the size : "))
set_data = set()
for _ in range(size):
    value = input()
    set_data.add(value)
print ("set ->",set_data)
# output
# Enter the size : 3
# 2
# 3
# 4
# set -> {'3', '4', '2'}

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Classes

class Product:
    def __init__(self,title,count):
        self.title = title
        self.count = count
    
product1 = Product("Alma",100)
product2 = Product("Nar",400)

print(product1.title,product1.count)
print(product2.title,product2.count)
# output
# Alma 100
# Nar 400

class Isci:
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.tamAd = self.ad + " " + self.soyad
        self.gmail = self.ad+self.soyad+"@gmail.com"
    
    def melumatGostermek(self):
         print(self.ad,self.soyad,self.maas)
    
    def melumatGostermek(self):
        return f"AD: {self.ad.upper()}, SOYAD: {self.soyad.upper()}"
        return self.ad.upper(),self.soyad.upper(),self.tamAd,self.gmail
        
    def maasArtirmaq(self,x):
        print(f"{self.ad} adli iscinin maasi {self.maas} idi. Indi ise {self.maas * x}")
        
        
isci1 = Isci("Xanlar","Kerimli",9999)
isci2 = Isci("twet","eryeryery",241214)
print(isci2.maas)
print(isci2.tamAd)
print(isci2.gmail)
# output
# 241214
# twet eryeryery
# tweteryeryery@gmail.com

isci1.melumatGostermek()
isci2.melumatGostermek()

print(isci1.melumatGostermek())
print(isci2.melumatGostermek())
# output
# AD: XANLAR, SOYAD: KERIMLI
# AD: TWET, SOYAD: ERYERYERY

# a = 10
# b = 20
# print(f"a ededi: {a}, b ededi: {b}, bu iki ededin cemi: {a+b}")

isci1.maasArtirmaq(5)
# output
# Xanlar adli iscinin maasi 9999 idi. Indi ise 49995

class Student:
    def __init__(self,ad,soyad,ortalama_bal,xercler, yalanlar,kesirler,fenler):
        self.ad = ad
        self.soyad = soyad
        self.ortalama_bal = ortalama_bal
        self.xercler = xercler
        self.yalanlar = yalanlar
        self.kesirler = kesirler
        self.fenler = fenler
    def showstudentinformation(self):
        print(self.ad,self.xercler,self.fenler)
    
    def a(self):
        print(self.ad +" : ")
        for i in self.fenler:
            
            print(i.upper())
    
student1 =Student("nezrin","ehmedova",60,1000,9000,20,["hecne","allah cezani verib"])
student2 =Student("Aida","Isayeva",1000,55,0,0,["python","c","html","css","jc","java"])

student1.showstudentinformation()
# output
# nezrin 1000 ['hecne', 'allah cezani verib']

student2.a()
# output
# Aida :
# PYTHON
# c
# HTML
# CSS
# JC
# JAVA

class Student:
    a = 5
    def __init__(self, ad, soyad, bal):
        self.ad = ad
        self.soyad = soyad
        self.bal = bal
    
    def balArtimi(self):
        self.bal *= self.a
        print(self.ad, self.bal)
        
    @classmethod
    def baliGuncellemek(cls, x):
        cls.a = x
        
        
student1 = Student("Xanlar","Kerimli",100)
student2 = Student("twet","eryeryery",2414)
student3=Student("qe6twe","wuyer",24)

print(student3.bal)
# output
# 24

student3.balArtimi()
# output
# qe6twe 600

student1.a = 10
print("evvelki bal: ",student1.bal)
# output
# evvelki bal:  100

print("Sonraki bal: ")
student1.balArtimi()
# output
# Sonraki bal:
# Xanlar 10000

student1 = Student("Xanlar", "Kerimli", 100)
yeniEded = int(input("Bayramdi, haminin balini artiraq!!!, EZIZ REKTORRRRRR nece defe artsin? : "))
# output
# Bayramdi, haminin balini artiraq!!!, EZIZ REKTORRRRRR nece defe artsin? : 2 (for example)

Student.baliGuncellemek(yeniEded)

print("Bayramdan sonraki bal: ")
student1.balArtimi()
# output
# Bayramdan sonraki bal:
# Xanlar 200

# -------

class Isci:
    faiz = 1.1
    def _init_(self,name,surname,age,salary):
        self.name= name
        self.surname= surname
        self.age= age
        self.salary= salary
    
    @classmethod
    def faizDeyisme(cls,x):
        cls.faiz =x 
        
    @classmethod
    def yeniIsciElaveEtmek(cls,info):
        name,surname,age,salary = info.split(" ")
        return cls(name,surname,age,salary)
 
class Mudur(Isci):
    def _init_(self,name,surname,age,salary,isciler):
        super()._init_(name,surname,age,salary)
        self.isciler = isciler
    def melumatlargoster(self):
        for i in self.isciler:
            print(i.name)
    def encoxmaas(self):
        max=0
        f=""

        for i in self.isciler:
            if i.salary>max:
                max=i.salary
                f=i.name
        print(f)



class Developer(Isci):
    def _init_(self,name,surname,age,salary,computer_dilleri):
        super()._init_(name,surname,age,salary)
        self.computer_dilleri = computer_dilleri 
    def yenidil(self):
        w=input("yeni dili daxil edin")
        self.computer_dilleri.append(w)
        print(self.computer_dilleri)
class Reception(Isci):
    def _init_(self,name,surname,age,salary,bezdilenler):
        super()._init_(name,surname,age,salary)
        self.bezdilenler = bezdilenler 
    @classmethod
    def yeniqurban(cls,info):
        name,surname,age,salary,bezdilenler=info.split(" ")
        return cls(name,surname,age,salary,bezdilenler)
    
butunisciler = []

isci1 = Isci("Kimse","Nese",123,3456)
isci2 = Isci("Filankes","Bilmirem",678,7890)

yeni_isci = input("Melumatlari daxil edin: ")
isci3 = Isci.yeniIsciElaveEtmek(yeni_isci)
butunisciler.append(isci1)
butunisciler.append(isci2)
butunisciler.append(isci3)
print("Butun isciler: ")
for a in butunisciler:
    print(a.name)
# output
# Melumatlari daxil edin: Xanlar Kerimli 20 1000
# Butun isciler: 
# Kimse
# Filankes
# Xanlar

yeniqurbanmelumatlari= input("yeni qurbanin melumatlarini verin")
yeniqurban1= Reception.yeniqurban(yeniqurbanmelumatlari)
print(yeniqurban1.name)
# output
# yeni qurbanin melumatlarini verinXanlar Kerimli 20 1000 qwqwq
# Xanlar

isci1 = Isci("Kimse","Nese",123,3456)
isci2 = Isci("Filankes","Bilmirem",678,7890)
isci_dev = Developer("qrew","tqwre",56,1224,["python","c","javascript"])
isci_dev.yenidil()
# output
# yeni dili daxil edinhtml
# ['python', 'c', 'javascript', 'html']

mudur1 = Mudur("yuoprt","wepq",78,6597,[isci1,isci2,isci_dev])
mudur1.melumatlargoster()
# output
# Kimse
# Filankes
# qrew

mudur1.encoxmaas()
# output
# Filankes

# -----

class Isci:
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        
    def __str__(self):
        return f"{self.ad} - {self.soyad} - {self.maas}"   
        # return self.ad+" - "+self.soyad+" - "+str(self.maas)
    
    def __repr__(self):
        return f"{self.soyad} {self.ad} bu iscinin maasi: {self.maas}" 
    
    def __add__(self,other):
        return self.maas + other.maas
        
isci1 = Isci("Nigar","Eliyeva",1000)
isci2 = Isci("Emil","Musayev",800)

print(isci1)
# output
# Nigar - Eliyeva - 1000

print(isci2)
# output
# Emil - Musayev - 800

print(isci1.__repr__())
# output
# Eliyeva Nigar bu iscinin maasi: 1000

print(repr(isci1))
# output
# Eliyeva Nigar bu iscinin maasi: 1000

print(isci1.__str__())
# output
# Nigar - Eliyeva - 1000

print(str(isci1))
# output
# Nigar - Eliyeva - 1000

print(isci1 + isci2)
# output
# 1800

# -----

class Isci:
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        
    @property    
    def email(self):
        self.mail = self.ad + self.soyad + "@gmail.com"    
        return self.mail
    
    @property
    def tamAd(self):
        return f"{self.ad} {self.soyad} "
        # return f"{self.ad.upper()} {self.soyad.upper()} "
    
    @tamAd.setter
    def tamAd(self,yeniAd):
        self.ad,self.soyad = yeniAd.split(" ")#["Gullu","Mustafazade"]
        # self.ad = ad
        # self.soyad = soyad
        
    @tamAd.deleter
    def tamAd(self):
        self.ad = None
        self.soyad = None
        print("melumat silindi")
        
isci1 = Isci("Nigar","Eliyeva",1000)
isci2 = Isci("Emil","Musayev",800)

print(isci1.email)
# output
# NigarEliyeva@gmail.com

print(isci1.ad)
# output
# Nigar

print(isci1.tamAd)
# output
# Nigar Eliyeva 

isci1.tamAd = "Gullu Mustafazade" 
print("deyisenden sonraki melumat")
print(isci1.ad)
# output
# deyisenden sonraki melumat
# Gullu

print(isci1.soyad)
# output
# Mustafazade

print(isci1.tamAd)
# output
# Gullu Mustafazade 

del isci1.tamAd
# output
# melumat silindi

print("deyisenden sonraki melumat")
print(isci1.ad)
# output
# deyisenden sonraki melumat
# None

print(isci1.soyad)
# output
# None

print(isci1.tamAd)
# output
# None None 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Linked list

# Single Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next 
            
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print("Data ->", current.data , "Next ->", current.next , end = "->")
            current = current.next 

        print("None")

sll = SinglyLinkedList()

size = int(input("Enter size of the linked list"))

for _ in range(size):
    value = int(input("Enter input for the value"))
    sll.append(value)

sll.display()
# output
# Enter size of the linked list2
# Enter input for the value4
# Enter input for the value5
# Data -> 4 Next -> <__main__.Node object at 0x7ba8dcce3390>->Data -> 5 Next -> None->None

# Double linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def display_reverse(self):
        current = self.tail
        while current:
            print("prev-> ", current.prev,"Data->",current.data,"Next->",current.next,end= "<->")
            current= current.prev
        
        print("None")

dll = DoublyLinkedList()

size = int(input("Enter the size of the Doubly Linked list"))

for _ in range(size):
    value = int(input("Enter the value"))
    dll.append(value)

dll.display_reverse()
# output
# Enter the size of the Doubly Linked list2
# Enter the value1
# Enter the value2
# prev->  <__main__.Node object at 0x78c7efa0b0d0> Data-> 2 Next-> None<->prev-> 
# None Data-> 1 Next-> <__main__.Node object at 0x78c7efa0b250><->None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Math

import math
a = int(input("eded: "))
# kokalti
print(math.sqrt(a))
# faktorial
print(math.factorial(a))
# yuvarlaqlasdirma
print(round(6.15765))
# yuxari mertebeye yuvarlaqlasdirma
print(math.ceil(6.15765))
print(math.ceil(-6.15765))
# asagi mertebeye yuvarlaqlasdirma
print(math.floor(6.95765))
print(math.floor(-6.95765))
# kesir hisseni silme
print(math.trunc(6.95765))
print(math.trunc(-6.95765))
# modulun tapilmasi, menfidirse musbet edir
print(math.fabs(-100))
print(math.pi)
# quvvet
print(math.pow(3,5))
print(243 ** (1/5))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Random

import random

print(random.random())
# output
# Between(0 to 1 (for example 0.5167673327151359))
print(random.randint(50,90))
# output
# Between(50 to 90 Only Whole Numbers(for example (65))
print(random.uniform(50,90))
# output
# Between(50 to 90 doesn't matter if it's whole or not(for example (52.71007279119084))

data = ["red","green","blue","qweqw","weqre","riteo","origtr","oirdjgfov"]
print("evvelki : ",data)
# output
# evvelki :  ['red', 'green', 'blue', 'qweqw', 'weqre', 'riteo', 'origtr', 'oirdjgfov']

print(random.choice(data))
# output
# randomply choose one of element from data (for example (weqre))

print(random.sample(data,3))
# output
# randomply choose 3 of element from data (for example ['qweqw', 'blue', 'oirdjgfov'])

random.shuffle(data)
print("sonraki : ",data)
# output
# sonraki :  ['red', 'weqre', 'riteo', 'green', 'oirdjgfov', 'qweqw', 'origtr', 'blue']

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Time 

import time
import random
import datetime
d = datetime.datetime
print(2024 - time.time() / 86400 / 365)
# output
# 1969.5075473096626

print(time.ctime(100000000))
# output
# Sat Mar  3 09:46:40 1973

print(time.localtime().tm_year)
# output
# 2024

print(time.localtime().tm_mday)
# output
# 15

print(time.localtime().tm_hour)
# output
# 17

print(time.localtime().tm_wday+1)
# output
# 6

print(time.localtime(100000000))
# output
# time.struct_time(tm_year=1973, tm_mon=3, tm_mday=3, tm_hour=9, tm_min=46, tm_sec=40, tm_wday=5, tm_yday=62, tm_isdst=0)

x = time.localtime()
print(time.asctime(x))
# output
# Sat Jun 15 17:54:15 2024

print(time.strftime("%d.%m.%y --- %H:%M:%S"))
# output
# 15.06.24 --- 17:54:15
print("start")
time.sleep(3)
print("end")

startTime = time.time()
a = [1,3,354,7,86,97,566,345,463,657]
cem = 0
for i in a:
    cem+=i
print(cem)
# output
# 2579

endTime = time.time()
print(endTime - startTime)
# output
# 2.9563903

colors = ["\033[31m","\033[32m","\033[34m","\033[35m", "\033[36m"]
print(random.choice(colors))
# random.choice array icerisinden herhansi bir element secmek ucundur

while True:
    time.sleep(1)
    print(f"{random.choice(colors)} { time.localtime().tm_hour} : { time.localtime().tm_min} : {time.localtime().tm_sec} \033[0m")
    print(f"{random.choice(colors)} {time.strftime('%H:%M:%S')} \033[0m")

# output
# 18 : 4 : 1 
# 18:04:01 
# 18 : 4 : 2 
# 18:04:02 
# 18 : 4 : 3 
# 18:04:03 
# 18 : 4 : 4 
# 18:04:04 
# 18 : 4 : 5

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Datetime

d = datetime.datetime
print(d.now())
print(d.today())
print(d.today().year)
print(d.today().day)
print(d.today().date)
print(d.today().hour)
print(type(d.now()))
print(d.ctime(d.now()))
print(d.strftime(d.now(),"%d %m %y"))
print((d(2024,5,25) - d(2002,7,24)) - (d(2024,5,25) - d(2004,2,4)))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sorting Styles 

# counting sort 

def counting_sort(arr):
    max_val = max(arr)                          # O(1)
    counts = [0] * (max_val+1)                  # O(M)
    output = [0] * len (arr)                    # O(N)

    # Count Occurences of each element          # Total -> O(M)+O(N) -> O(M+N)
    for num in arr:                             # O(N)
        counts [num] += 1                       

    for i in range(1, max_val+1):               # O(M)
        counts [i] += counts [i-1]

    # build the sorted array 
    for num in reversed(arr):                   # O(N)
        output[counts[num]-1] = num
        counts [num] -= 1                       # Total -> O(M)+O(N)+O(N)+O(M)+O(N)
                                                # Total -> O(2M + 3N) -> O(M+N)
    return output

# Example usage
arr = [2, 5, 3, 0, 2, 3, 0, 3]
print ("Unsorted array: ",arr)
sorted_arr = counting_sort(arr)
print ("Sorted array: ", sorted_arr)

# insertion sorting 

def insertion_sort(arr):
    for i in range(1, len(arr)):            # Time : O(n)
        key = arr[i]                        # Time : O(1)
        j = i-1                             # Time : O(1)
        
        while j >= 0 and key < arr[j]:      # Time : O(n)
            arr[j+1] = arr[j]               # Time : O(1)
            j -= 1                          # Time : O(1)

        arr[j+1] = key                      # Time : O(1)
                                            # Total : O(n)*O(1)*O(n)*O(1)
                                            # Total : O(n^2)
# Example 

arr = [64,35,100,39,93,20]
print ("Unsorted array :",arr,arr[0])
insertion_sort(arr)
print("So array : ", arr,arr[0])

# Bubble sort

def bubble_sort(arr):                                      # Time complexity
    n = len (arr)                                           # O(1)
    for i in range (n):                                     # O(n)
        for j in range (0 , n-i-1):                         # O(n)
            if arr[j]>arr[j+1]:                             # O(1)
                arr[j] , arr[j+1]= arr[j+1] , arr[j]        # O(1)
                                                            # Total -> O(n^2)
# Example

arr = [64 , 34 , 25 , 12 , 22 , 11 , 90]
print ("Unsorted list ->", arr)
bubble_sort(arr)
print ("Sorted list ->", arr)

# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2                                   # // -> Integer division 
        left_half = arr [:mid]                              # :mid = [:3] -> 0 , 1 , 2 (indexes)
        right_half = arr [mid:]                             # mid: = [3:] -> 3 , 4 , 5 , 6 (indexes)
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0                                       # i is for the left half and j is for right half and k is for the original array 
                                                            # k is to keep the track of the original array 
        while i < len (left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:                  # l-h -> 64 , 34 , 25 , 12   r-h -> 22 , 11 , 90
                arr[k] = left_half[i]                        
                i += 1                                      # l-h -> 64 , 34             r-h -> 25 , 12
            else:                                            
                arr [k] = right_half[j]                     # l-h -> 64     r-h -> 34
                j += 1                                      #        25            12
                                                            #        22            11 and 90 
            k += 1                                          # comparing 0 indexs first and then so on and so on 
                                                            # so with  each number adding up i, j and k will be added up 
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j<len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example Usage
arr = [64 , 34 , 25 , 12 , 22 , 11 , 90] 
print ("Unsorted array : ",arr)
merge_sort(arr)
print ("Sorted array :",arr)

# Quick sort

def quick_sort( arr , low , high):                      # Time complexity
    if low < high :                                     # O(1)
        pivot_index = partition (arr , low , high)      # O(1)
        quick_sort(arr , low , pivot_index - 1)         # O(n)
        quick_sort(arr, pivot_index + 1 , high)         # O(n)
                                                        # Total -> O(n^2)
def partition (arr , low , high):                       
    pivot = arr [high]                                  # O(1)
    i = low - 1                                         # O(1)
    for j in range (low , high):                        # O(n)
        if arr[j]< pivot:                               # O(1)
            i += 1                                      # O(1)
            arr[i] , arr[j] = arr [j] , arr[i]          # O(1)
    arr[i+1] , arr [high] = arr[high] , arr[i+1]        # O(1)
    return i+1                                          # O(1)
                                                        # Total -> O(n)    Best case : O(n log n)      Worst case: O(n^2)
# Example
arr = [64 , 34 , 25 , 12 , 22 , 11 , 90]
print ("Unsorted array :", arr)
quick_sort(arr , 0 , len(arr)-1 )
print("Sorted array :", arr)

# Selection sort

def selection_sort(arr):                                    # Time complexity 
    n = len (arr)                                           # O(1)
    for i in range (n):                                     # O(n)
        min_idx = i                                         # O(1)
        for j in range (i+1, n):                            # O(n)
            if arr[j] < arr[min_idx]:                       # O(1)
                min_idx= j                                  # O(1)
        arr [i] , arr [min_idx] = arr[min_idx], arr[i]      # O(1)
                                                            # Total -> O(1) + O(n)*O(n)*O(1)
                                                            # Total -> O(n^2)
#Example 
 
arr = [64, 25 , 12 , 22 , 11]
print ("Unsorted array ->" , arr)

selection_sort(arr)
print ("Sorted array ->", arr)

# Bucket Sort 

def bucket_sort(arr):                                               #Time complexity 
    if len(arr) == 0:                                               
        return arr
    #Step 1 : Create empty buckets

    bucket_count = len (arr)
    buckets = [[]for _ in range(bucket_count)]                          # O(n)

    #Step 2 : Insert elements into their respective buckets
    min_value = min (arr)
    max_value = max (arr)
    range_of_bucket = (max_value - min_value) / bucket_count            # O(1)

    for num in arr:                                                     # O(n)
        index = int((num - min_value) / range_of_bucket)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)                                  

    #Step 3 : Sort each bucket
    for bucket in buckets:                                              # O(n)
        bucket.sort()               # You can use any sort algorithm    # O(n)
                                                                        # Total O(n^2)
    #Step 4 : Concatenate all sorted buckets
    sorted_array = []
    for bucket in buckets:                                              # O(n)
        sorted_array.extend(bucket)                                     

    return sorted_array

# Example Usage

arr = [0.78 , 0.17 , 0.39 , 0.26 , 0.72 , 0.94 , 0.21 , 0.23 , 0.68 ]
print ("unsorted array :", arr)
sorted_array = bucket_sort(arr)
print ("Sorted array :", sorted_array)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Binary Tree

# Simple Tree

class TreeNode :
    def __init__(self, value):
        self.value = value
        self.childern = []
    
    def add_child(self , child_node) :
        self.childern.append(child_node)

    def display_tree (self, level = 0):
        indent = " " * (level*4)
        print (indent + str (self.value))
        for child in self.childern:
            child.display_tree(level+1)
            
root = TreeNode("Root")

child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

child1_1 = TreeNode("child 1.1")
child1_2 = TreeNode("child 1.2")

child2_1 = TreeNode("child 2.1")
child2_2 = TreeNode("child 2.2")

child3_1 = TreeNode("child 3.1")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(child1_1)
child1.add_child(child1_2)

child2.add_child(child2_1)
child2.add_child(child2_2)

child3.add_child(child3_1)

root.display_tree()
# output
# Root
#     Child 1
#         child 1.1
#         child 1.2
#     Child 2
#         child 2.1
#         child 2.2
#     Child 3
#         child 3.1

# Binary Tree operation

class TreeNode:
   def __init__(self,value):
     self.value = value
     self.left = None
     self.right = None 

def insert(root,value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
        return root

root = TreeNode(10)
values = [5,15,3,7,12,18]
for value in values:
    root = insert(root, value)
#output  -

# DFS
from collections import deque
class TreeNode:
    def __init__(self, value) :
        self.value = value
        self.childern = []

    def add_child(self , child_node) :
        self.childern.append(child_node)

    def dfs(self):
        print(self.value, end = ' ')
        for child in self.childern:
            child.dfs()

    def bfs (self):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            print(node.value , end = ' ')
            for child in node.childern:
                queue.append(child)
            
root = TreeNode("Root")

child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

child1_1 = TreeNode("child 1.1")
child1_2 = TreeNode("child 1.2")

child2_1 = TreeNode("child 2.1")
child2_2 = TreeNode("child 2.2")

child3_1 = TreeNode("child 3.1")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(child1_1)
child1.add_child(child1_2)

child2.add_child(child2_1)
child2.add_child(child2_2)

child3.add_child(child3_1)

print("DFS Tranversal :")
root.dfs ()

print("BFS Tranversal :")
root.bfs ()
# output
# DFS Tranversal :
# Root Child 1 child 1.1 child 1.2 Child 2 child 2.1 child 2.2 Child 3 child 3.1 BFS Tranversal :
# Root Child 1 Child 2 Child 3 child 1.1 child 1.2 child 2.1 child 2.2 child 3.1 

# Type of binary Trees

from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_complete_binary_tree(root):
    if not root:
        return True
    queue = deque([root])
    reached_end =False
    while queue:
        node = queue.popleft()
        if node:
            if reached_end:
                return False
            queue.append(node.left) 
            queue.append(node.right)
        else:
            reached_end= True

    return True

def is_perfect_binary_tree(node, depth, level =0):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return depth == level+1
    if node.left is None or node.right is None:
        return False
    return is_perfect_binary_tree(node.left, depth,level+1) and is_perfect_binary_tree(node.right,depth,level+1)  

def find_depth(node):
    d=0
    while node is not None:
        d+= 1
        node = node.left
        return d
      
root = TreeNode(1)  
root.left = TreeNode(2)        
root.right = TreeNode(3)        
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)        
root.right.left = TreeNode(6)    
root.right.right = TreeNode(7)    

print("is it a complete binary tree?", is_complete_binary_tree(root))

depth = find_depth(root)
print("is it perfect binary tree?", is_perfect_binary_tree(root,depth))
# output
# is it a complete binary tree? True
# is it perfect binary tree? False

# Tyoes of Binary Trees

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_full_binary_tree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False

#Example 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print (" Is this a full binary tree -> ", is_full_binary_tree(root))
# output
# is it a complete binary tree? True
# is it perfect binary tree? False
# Is this a full binary tree ->  True

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Time complexity

def prefix_average(X):             
    n = len (X)                     # 1 + 1 -> O(1)
    A = [0] * n                     # 1 + n -> O(n)

    total = 0                       # 1 -> O(1)
    for i in range(n):              # for(i=0; i<n; i++) -> 1 + n + n ->O(n)
        total += X[i]               # 1 + 1 + 1 -> O(1)
        A[i] = total/ (i+1)         # 1 + 1 + 1 + 1 -> O(1)

    return A                        # 1 -> O(1)

X = [1,2,3,4,5]                     # Total -> O(1)+ O(n)+ O(1)+ {O(n)* O(1)* O(1)} + O(1)
                                    # Total -> O(n)
print ("A ->",prefix_average(X))
# output
# A -> [1.0, 1.5, 2.0, 2.5, 3.0]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Assignments

# Python Programming - Dictionaries and Lists

# Tasks: 
# Write a Python program to store information about students(size of the students to be taken from the user).
# Each student's information should include their name, age, roll number, and grade. 
# Implement a loop to input the information for each student and store it in a dictionary. 
# After storing the information, print the details of all students.

# Instructions:
# Implement a loop to input the information for each student. The information to be entered includes:

# Name
# Age
# Roll Number
# Grade
# Store the information of each student in a dictionary with keys for name, age, roll number, and grade.

# Append each student's dictionary to a list to store information for all students.

# After storing the information for all students, print the details of each student
# including their name, age, roll number, and grade.

# Note:

# Ensure that the input is validated appropriately (e.g., age should be an integer).
# Use appropriate data structures and loops to implement the solution.

print("Students Information Program".center(50,"-"))
students=[]
students_number=int(input("how many students "))
for i in range (students_number):
    print(i+1, ".student:")
    name = input("\tgive a student name ")
    age = int(input("\tgive a student age ")) 
    roll_number= input("\tgive a student roll number ")
    grade= input("\tgive a student grade ")
    print("\n")
    student=dict(name=name,age=age,roll_number=roll_number,grade=grade)
    students.append(student) 

x = 1 
for student in students:
    print(x, ".student: ", student)
    x+=1
    
# Analyzing Time Complexities for Python Code

# Instructions:

# Review the provided Python code snippets below.
# For each code snippet, calculate the Big O notation representing its time complexity.
# Provide a brief explanation of how you arrived at your Big O notation for each code.
# Submit your analysis along with the calculated Big O notation for each code snippet.
# The codes are compiled in the file (time_complexity_codes.py) which is attached with the assignment
#-------- Code 1 -----------#
def linear_sum(arr):            #1
    total = 0                   #1
    for num in arr:             #n
        total += num            #1
    return total                #1

#1+1+n+1+1 = n+4

#-------- Code 2 -----------#
def linear_search(arr, target):         #1
    for num in arr:                     #n
        if num == target:               #1
            return True                 #1
    return False                        #1

#1+n+1+1+1 = n+4

#-------- Code 3 -----------#
def three_dimensional_sum(arr):                 #1
    total = 0                                   #1
    n = len(arr)                                #1                  
    for i in range(n):                          #n
        for j in range(n):                      #n
            for k in range(n):                  #n
                total += arr[i][j][k]           #1
    return total                                #1

#1+1+1+(n*n*n)+1+1 = 5+n^3

#-------- Code 4 -----------#

def print_matrix(matrix):                                       #1
    for row in matrix:                                          #3
        for elem in row:                                        #3
            # Print each cell with space separation
            print(elem, end=" ")                                #1
        # Move to the next line after printing each row
        print()                                                 #1

#1+3*(3*1+1) = 13

example_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

#-------- Code 5 -----------#
# Function to print all pairs of elements in an array
def print_all_pairs(arr):                                             #1
    # Traverse the array
    for i in range(len(arr)):                                         #n
        for j in range(len(arr)):                                     #n
            # Print each pair of elements
            print("(", arr[i], ",", arr[j], ")", end=" ")             #1

#1+(n*n)+1 = 2+n^2

#-------- Code 6 -----------#
def three_dimensional_sum(arr):                 #1
    total = 0                                   #1
    n = len(arr)                                #1
    for i in range(n):                          #n
        for j in range(n):                      #n
            for k in range(n):                  #n
                total += arr[i][j][k]           #1
    return total                                #1

#1+1+1+(n*n*n)+1+1 = 5+n^3

#-------- Code 7 -----------#
def matrix_multiplication(A, B):                            #1
    m, n = len(A), len(A[0])                                #1
    p, q = len(B), len(B[0])                                #1
    if n != p:                                              #1
        return "Invalid matrices for multiplication"        #1
    result = [[0] * q for _ in range(m)]                    #m*q
    for i in range(m):                                      #m
        for j in range(q):                                  #q
            for k in range(n):                              #n
                result[i][j] += A[i][k] * B[k][j]           #1
    return result                                           #1

#1+1+1+1+1+(m*q)+(m*q*n)+1+1 = 7+(m*q)+(m*q*n)

#-------- Code 8 -----------#
def fibonacci(n):                                    #1
    if n <= 1:                                       #1
        return n                                     #1
    return fibonacci(n-1) + fibonacci(n-2)           #2^n

#1+1+1+2^n = 3+2^n

# Sorting with Custom Comparators

# Task:
# Implement a custom sorting function that can sort a list of dictionaries based
# on multiple keys using the bubble sort algorithm.

# Requirements:
# Create a function named custom_bubble_sort.
# The function should take a list of dictionaries and a key to sort by.
# Use the bubble sort algorithm to sort the list based on the given key in the specified order.

def custom_bubble_sort(arr, keys):
    n = len(arr)
    for i in range(n):
        for j in range (0 , n-i-1):
            for key in keys:
                if arr[j][key]>arr[j+1][key]:
                    arr[j] , arr[j+1]= arr[j+1] , arr[j]
                    break
                elif  arr[j][key]<arr[j+1][key]:
                    break

students = [
    {'name': 'Alice', 'age': 25, 'grade': 'A'},
    {'name': 'Bob', 'age': 20, 'grade': 'B'},
    {'name': 'Charlie', 'age': 25, 'grade': 'B'},
    {'name': 'Dave', 'age': 20, 'grade': 'A'}]
keys = ['age', 'grade']
custom_bubble_sort(students, keys)
print(students)

# Sorting Strings with Different Lengths

# Task:
# Implement the counting sort algorithm to sort an array of
# strings of varying lengths based on their lexicographical order.

# Requirements:
# Create a function named counting_sort_strings.
# The function should take a list of strings.
# Use the counting sort algorithm to sort the strings.

def counting_sort_strings(arr):
    n = len (arr)                                           
    for i in range (n):                                    
        for j in range (0 , n-i-1):                         
            if arr[j]>arr[j+1]:                            
                arr[j] , arr[j+1]= arr[j+1] , arr[j]           


arr = ["banana","apple", "grape", "kiwi", "mango", "peach"]
counting_sort_strings(arr)
print(arr)  

# Sorting a Linked List

# Task:
# Implement the merge sort algorithm to sort a singly linked list.

# Requirements:
# Create a Node class and a LinkedList class.
# Implement a function named merge_sort_linked_list to sort the linked list.
# Use the merge sort algorithm to sort the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        # print("None")

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head
# optimallasdirma!!!
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def sorted_merge(a, b):
    result = None

    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)

    return result

ll = LinkedList()
values = [38, 27, 43, 3, 9, 82, 10]
for val in values:
    ll.append(val)
print("ll.head  : ",ll.head)
ll.head = merge_sort_linked_list(ll.head)
ll.display() 

# Depth Calculation

# Description: Calculate the depth of a binary tree.

# Tasks:

# Implement a method to calculate the depth of the binary tree.
# Sample Input:

# values = [1, 2, 3, 4, 5, 6, 7]
# The tree should look like this:
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7

# Expected Output:
# Depth = 3

# Simple Tree

class TreeNode :
    def __init__(self, value):
        self.value = value
        self.childern = []
    
    def add_child(self , child_node) :
        self.childern.append(child_node)

    def display_tree (self, level = 0):
        indent = " " * (level*4)
        print (indent + str (self.value))
        count = level
        for child in self.childern:
            count =  child.display_tree(level+1)
        return count 

root = TreeNode("Root")

child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

child1_1 = TreeNode("child 1.1")
child1_2 = TreeNode("child 1.2")

child2_1 = TreeNode("child 2.1")
child2_2 = TreeNode("child 2.2")

child3_1 = TreeNode("child 3.1")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(child1_1)
child1.add_child(child1_2)

child2.add_child(child2_1)
child2.add_child(child2_2)

child3.add_child(child3_1)

a = root.display_tree() + 1
print(a)

# Binary Tree Creation and Traversal

# Description: Create a binary tree and implement the following traversal methods:

# Preorder Traversal
# Inorder Traversal
# Postorder Traversal
# Tasks:

# Implement a class TreeNode for the tree nodes.
# Implement methods for tree creation and traversal.
# Sample Input:
# values = [1, 2, 3, 4, 5, 6, 7]
# The tree should look like this:
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7

# Output:
# Preorder: 1 2 4 5 3 6 7
# Inorder: 4 2 5 1 6 3 7
# Postorder: 4 5 2 6 7 3 1

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    i = 1

    while i < len(values):
        current_node = nodes.pop(0)

        if values[i] is not None:
            current_node.left = TreeNode(values[i])
            nodes.append(current_node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            nodes.append(current_node.right)
        i += 1

    return root

def preorder_traversal(root):
    if root is None:
        return []

    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return []

    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return []

    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

values = [1, 2, 3, 4, 5, 6, 7]
root = create_tree(values)

print("Preorder:", preorder_traversal(root))
print("Inorder:", inorder_traversal(root))
print("Postorder:", postorder_traversal(root))

# Min-Heap Creation, Insertion, peek and extraction of min

# Heap DS

class MinHeap:
    
    def __init__ (self , array = None ):
        if array is None:
            self.heap = []
        else:
            self.heap = array 
            self.heapify ()

    def heapify (self):
        for i in range (len(self.heap) // 2 -1, -1 , -1):
            self._bubble_down(i)
   
    def insert(self , value):
        self.heap.append(value)
        self._bubble_up(len(self.heap)-1)

    def tranverse(self):
        return self.heap
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_value
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def delete(self , value):
        try :
            index = self.heap.index(value)
            if index == len(self.heap) - 1:
                self.heap.pop()
            else:
                self.heap[index] = self.heap.pop()
                if index < len (self.heap):
                    self._bubble_down(index)
                    self._bubble_up(index)

        except ValueError:
            print("Value ", value , "not found in the heap")


    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index],self.heap [parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index 

        if left_child < len (self.heap) and self.heap[left_child] < self.heap [largest]:
            largest = left_child
        if right_child < len (self.heap) and self.heap[right_child] < self.heap [largest]:
            largest = right_child

        if largest != index:
            self.heap [index], self.heap [largest] = self.heap [largest], self.heap[index]

    def __str__(self):
        return str(self.heap)
    

heap = MinHeap()
values =[40, 20, 15, 5, 30, 10]
for value in values:
    heap.insert(value)

print(f"Heap after insertion{heap}")

print(f"Heap Transversal: {heap.tranverse()}")

print ("peek min ->",heap.peek())

heap.delete(8)

print(f"Heap traversal after deleting element 8:{heap.tranverse()}")

# Description: Create a binary search tree and implement insertion, deletion and search operations.

# Tasks:

# Implement a class BSTNode for the tree nodes.
# Implement methods for insertion and search.
# Sample Input:

# values = [10, 5, 15, 3, 7, 12, 18]
# Insert these values into the BST.


# delete_value = 15

# Expected Output:
# After insertion, the BST should look like:
#       10
#      /  \
#     5   15
#    / \  / \
#   3  7 12 18

# Searching for 7 should return True.
# Searching for 20 should return False.

# After deleting 15, the BST should look like:
#       10
#      /  \
#     5   18
#    / \  /
#   3  7 12


# BST Insertion, Searching and Deletion

# Description: Create a binary search tree and implement insertion, deletion and search operations.

# Tasks:

# Implement a class BSTNode for the tree nodes.
# Implement methods for insertion and search.
# Sample Input:

# values = [10, 5, 15, 3, 7, 12, 18]
# Insert these values into the BST.


# delete_value = 15

# Expected Output:
# After insertion, the BST should look like:
#       10
#      /  \
#     5   15
#    / \  / \
#   3  7 12 18

# Searching for 7 should return True.
# Searching for 20 should return False.

# After deleting 15, the BST should look like:
#       10
#      /  \
#     5   18
#    / \  /
#   3  7 12

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    i = 1

    while i < len(values):
        current_node = nodes.pop(0)

        if values[i] is not None:
            current_node.left = TreeNode(values[i])
            nodes.append(current_node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            nodes.append(current_node.right)
        i += 1

    return root

def show(root):
    if root:
     print(root.value,end=" ")
     show(root.left)
     show(root.right) 


values =[10, 5, 15, 3, 7, 12, 18]
root = create_tree(values)

print("before: \n")
show(root)
number = int(input())
values.remove(number)
root = create_tree(values)
print("after: ")
show(root)