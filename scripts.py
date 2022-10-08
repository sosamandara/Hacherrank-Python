#Say "Hello, World!" With Python

print("Hello, World!")

#Python If-Else
n = input()
n=int(n)
if (n%2==1):
    print("Weird")
elif (n%2==0) and (2<=n<=5):
    print("Not Weird")
elif (n%2==0) and (6<=n<=20):
    print("Weird")
else:
    print("Not Weird")


#Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)


#Python: Division
a=int(input())
b=int(input())
print(a//b)
print(a/b)


#Loops
n=int(input())
i=0
while i<n:
    print(i*i)
    i+=1




#Write a function
def is_leap(year):
    leap=False
    if (year%4==0):
        if (year%100==0):
            if(year%400==0):
                leap=True
            else:
                leap=False
        else:    
            leap=True  
    else:
        leap=False
    return leap        



#Print Function
n=int(input())
s=""
i=1
while i<=n:
    s1=str(i)
    s=s+s1
    i+=1
print(s)


#List Comprehensions
x=int(input())
y=int(input())
z=int(input())
n=int(input())

all_perm = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(all_perm)



#Find the Runner-Up Score!  
n = int(input())
A =list([int(i) for i in input().split(" ")])

A1=[]
for elem in A:
    if elem not in A1:
        A1.append(elem)
A1.sort()
print(A1[-2])




#Nested Lists
N = int(input())
records = []
students = []
for i in range(N):
    students.append(input())
    students.append(float(input()))
    records.append(students)
    students=[]

grades = []
for i in range(N):
    if records[i][1] not in grades:
        grades.append(records[i][1])
grades.sort()
seconds = []
for i in range(N):
    if (records[i][1]==grades[1]):
        seconds.append(records[i][0])
seconds.sort()
for elem in seconds:
    print(elem)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
elem = student_marks[query_name]
print("{:.2f}".format(sum(elem)/(len(elem))))

#Lists
if __name__ == '__main__':
    N = int(input())
list1 = []
for _ in range(N):
    function_name, *line=input().split(" ")
    if function_name=="insert":
        i=int(line[0])
        e=int(line[1])
        list1.insert(i,e)
    elif function_name=="print":
        print(list1)
    elif function_name=="remove":
        e=int(line[0])
        list1.remove(e)
    elif function_name=="append":
        e=int(line[0])
        list1.append(e)
    elif function_name=="sort":
        list1.sort()
    elif function_name=="pop":
        list1.pop()
    elif function_name=="reverse":
        list1.reverse()


#Tuples 
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

#sWAP cASE
def swap_case(s):
    new_s=[]
    for i in range(len(s)):
        if s[i].isupper():
            new_s.append(s[i].lower())
        else:
            new_s.append(s[i].upper())
    s1 = "".join(new_s)
            
    return s1



#String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    result = "-".join(line)
    return result



#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first_name,last_name))



#Mutations
def mutate_string(string, position, character):
    new_s = string[:position]+character+string[(position+1):]
    #l = list(string)
    #l[position] = character
    #new_s = "".join(l)
    return new_s


#Find a string
def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    count_sub = 0
    for i in range(n-m+1):
        if sub_string==string[i:i+m]:
            count_sub+=1
    return count_sub


#String Validators
if __name__ == '__main__':
    s = input()

control = False
alnum = False
alpha = False
digit = False
low = False
upp = False
m = False
for l in s:
    if l.isalnum():
            control = True
    if l.isalpha():
            alpha = True
    if l.isdigit():
            digit = True
    if l.islower():
            low = True
    if l.isupper():
            upp = True 
print(control)
print(alpha)
print(digit)
print(low)
print(upp)





#Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap


def wrap(string, max_width):
    if (len(string)//max_width==0):
        lines = len(string)//max_width
    else:
        lines = len(string)//max_width + 1
    i=0
    final = ""
    current = max_width
    for j in range(lines):
        final += string[i:current]+"\n"
        i += max_width
        current += max_width
    
    return final




#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT

line =input().split(" ")
c=".|."
N=int(line[0])
M=int(line[1])
for i in range(1,N,2):
    print((c*i).center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,0,-2):
    print((c*i).center(M,"-"))




#String Formatting
def print_formatted(number):
    # your code goes here
    lun = len(str(bin(number))) - 2
    for i in range(1,number+1):
        dec=str(i)
        octal=oct(i)
        hexa=hex(i).upper()
        bina=bin(i)
        print(dec.rjust(lun," "),octal[2:].rjust(lun," "),hexa[2:].rjust(lun," "),bina[2:].rjust(lun," "))
    
    
    




#Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    final = ""
    alphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    left=""
    for i in range(size,1,-1):
        new_central = left+"-"+alphabet[i]+"-"+left[::-1]
        left = left+"-"+alphabet[i]
        final += new_central.center(4*size-3,"-")+"\n"
    left1=left[1:]
    if size==1:
        print("a")
    else:
        central=left[1:]+"-a-"+left1[::-1]
        final+=(central+final[::-1]).center(4*size-3,"-")+"\n"      
    print(final)
    return 
    
    






#Capitalize!


# Complete the solve function below.
def solve(s):
    t = s.split()
    result=[]
    for i in range(len(t)):
        if t[i][0].isdigit()==False:
            result.append(t[i][0].upper()+t[i][1:])
        else:
            result.append(t[i])
        s = s.replace(t[i],result[i])
    return s
        



#The Minion Game
def minion_game(s):
    t = s.lower()
    vowel = ['a','e','i','o','u']
    count_kevin = 0 
    count_stuart = 0 
    length = len(t)


    for i in t:
        if i in vowel:
            count_kevin += length
        else:
            count_stuart += length
        length -= 1

    if(count_kevin > count_stuart):
        print("Kevin", count_kevin)
    elif(count_kevin < count_stuart):
        print("Stuart", count_stuart)
    else:
        print("Draw")

    

#Merge the Tools!
def merge_the_tools(string, k):

    final=""
    for i in range(0,len(string),k):
        sing=[]
        for elem in string[i:i+k]:
            if elem not in sing:
                final+=elem
                sing+=elem
        final+="\n"
    print(final)
    return
    
    
    



#Introduction to Sets
def average(array):
    # your code goes here
    somma = sum(set(arr))/len(set(arr))
    return somma



#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split(" ")
arr = input().split(" ")
A = set(input().split(" "))
B = set(input().split(" "))
count = 0
for elem in arr:
    if elem in A:
        count+=1
    if elem in B:
        count-=1

print(count)

#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
a = set(map(int,input().split()))
M = int(input())
b = set(map(int,input().split()))
elem = list(set(a.difference(b).union(b.difference(a))))
elem.sort()
print(*elem,sep='\n')

#Set .add() 
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()
for _ in range(N):
    countries.add(input())
print(len(countries)) 


#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    name_f, *line=input().split()
    if name_f=='pop':
        s.pop()
    elif name_f=='remove':
        s.remove(int(line[0]))
    elif name_f=='discard':
        s.discard(int(line[0]))
print(sum(s))  

#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
linen = input().split()
rolln = set(map(int,linen))
m = int(input())
linem = input().split()
rollm = set(map(int,linem))
print(len(rolln.union(rollm)))

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
linen = input().split()
rolln = set(map(int,linen))
m = int(input())
linem = input().split()
rollm = set(map(int,linem))
print(len(rolln.intersection(rollm)))

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
linen = input().split()
rolln = set(map(int,linen))
m = int(input())
linem = input().split()
rollm = set(map(int,linem))
print(len(rolln.difference(rollm)))

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
linen = input().split()
rolln = set(map(int,linen))
m = int(input())
linem = input().split()
rollm = set(map(int,linem))
print(len(rollm.symmetric_difference(rolln)))

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    name_f, n_elem= input().split()
    B=set(map(int,input().split()))
    if name_f=='intersection_update':
        A.intersection_update(B)
    elif name_f=='update':
        A.update(B)
    elif name_f=='symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif name_f=='difference_update':
        A.difference_update(B)
print(sum(A))







#The Captain's Room 
# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
group_rooms = list(map(int,input().split()))

capt_room = (k*sum(set(group_rooms))-(sum(group_rooms)))/(k-1)
print(int(capt_room))


#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
for _ in range(N):
    n, A = int(input()),set(map(int,input().split()))
    m, B = int(input()),set(map(int,input().split()))
    if A.difference(B)==set():
        print(True)
    else:
        print(False)


#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
super_set = True
for _ in range(n):
    B=set(map(int,input().split()))
    if B.difference(A)!=set() or len(B)==len(A):
        super_set = False
        break
print(super_set)

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_shoes = int(input())
shoe_sizes = Counter(list(map(int,input().split())))
num_clients = int(input())
guadagno = 0
for i in range(num_clients):
    size,money = map(int,input().split())
    if shoe_sizes[size]>0:
        guadagno+=money
        shoe_sizes[size]-=1
print(guadagno)
        

#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
   
for j in range(m):
    elemB = input()
    if elemB in d:
        print(*d[elemB])
    else:
        print(-1)

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
student = namedtuple('student', input().split())
students=[]
for i in range(N):
    a, b, c, d = input().split()
    students.append(student(a,b,c,d))

somma=0
for i in range(len(students)):
    somma+=int(students[i].MARKS)
print(somma/len(students))

#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
ord_dict = OrderedDict()
for _ in range(N):
    line = input().split()
    item_name = " ".join(line[:-1])
    if item_name in ord_dict:
        ord_dict[item_name]+=int(line[-1])
    else:
        ord_dict[item_name]=int(line[-1])
for elem in ord_dict:
    print(elem,ord_dict[elem])

#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict 
N,ord_dict = int(input()),OrderedDict()
for _ in range(N):
    word = input()
    if word in ord_dict:
        ord_dict[word] += 1
    else:
        ord_dict[word] = 1
print(len(ord_dict))
final = [str(ord_dict[elem]) for elem in ord_dict]
print(" ".join(final))
    

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    fun_name, *line= input().split()
    if fun_name == "append":
        d.append(line[0])
    elif fun_name == "appendleft":
        d.appendleft(line[0])
    elif fun_name == "pop":
        d.pop()
    elif fun_name == "popleft":
        d.popleft()
print(*d)

#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())
final = ""
for _ in range(T):
    d = deque()
    last = 2**31
    n, line = int(input()), map(int, input().split())
    d.extend(line)
    for i in range(n):
        M=max(d[0],d[-1])
        if M<=last and M==d[0]:
            d.popleft()
        elif M<=last and M==d[-1]:
            d.pop()
        else:
            final+="No\n"
            break
        last = M
    if len(d)==0:
            final+="Yes\n"
print(final)      


     
        
    

#Company Logo
#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys
s=input()
count_letters =Counter(s).most_common()
sort_count_letter =  sorted(count_letters,key=lambda item: (-item[1], item[0]))
for elem in sort_count_letter[:3]:
    print(elem[0],elem[1])



#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
line = list(map(int,input().split()))
week_day = calendar.weekday(line[2], line[0], line[1])
print((calendar.day_name[week_day]).upper())

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    a, b = input().split()
    try :
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except  ValueError as v:
        print("Error Code:",v)


#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int, input().split())
Sub = []
for i in range(X):
    Sub.append(list(map(float, input().split())))

a = list(zip(*[Sub[i] for i in range(X)]))
for i in range(N):
         print(sum(a[i])/X)

#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sort_arr = sorted(arr, key = lambda x:x[k])
    
    for elem in sort_arr:
        print(*elem)

#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lower=""
upper=""
even=[]
odd=[]
for letter in s:
    if letter.islower():
        lower+=letter
    elif letter.isdigit():
        if ((int(letter))%2)==0:
            even.append(letter)
        else:
            odd.append(letter)
    elif letter.isupper():
        upper+=(letter)
print("".join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)))







#Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib=[0,1]
    if n==0:
        fib=[]
    if n==1:
        fib=[0]
    if n>=2:
        for i in range(2,n):
            fib.append(fib[-2]+fib[-1])
            
    return fib
    
    
    

#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    s = input()
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$',s)))


#Re.split()
regex_pattern = r"[,\.]"	# Do not delete 'r'.



#Group(), Groups() & Groupdict()
import re
s = input()
m = re.search(r'([a-z A-Z 0-9])\1+',s)
if m:
    print(m.groups()[0])
else:
    print(-1)


#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
world = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
m = re.findall(world,s)
if m:
    print(*m,sep="\n")
else:
    print(-1)

#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
sub_s = input()
pattern = re.compile(sub_s)
match = pattern.search(string)
if not match:
    print("(-1, -1)")
else:
    while match:
        print("({}, {})".format(match.start(),match.end()-1))
        match = pattern.search(string,match.start()+1)





#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())




for i in range(N):
    s = input()
    new = re.sub(r' && ', ' and ', s)
    new = re.sub(r'\ \|\|\ ', ' or ', new)
    new = re.sub(r' && ', ' and ', new)
    new = re.sub(r'\ \|\|\ ', ' or ', new)
    print(new)
    




#Validating Roman Numerals
regex_pattern = r"^M{0,3}(D?C{0,3}|C(D|M))(L?X{0,3}|X(L|C))(V?I{0,3}|I(V|X))$"	# Do not delete 'r'.


#Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
pattern = r'^[7|8|9][0-9]{9}$'
for _ in range(N):
    print('YES' if bool(re.search(pattern,input())) else 'NO')
    









#Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
pattern = re.compile(r'^<[a-z A-Z](\w|-|\.|_)+@[a-z A-Z]+\.[a-z A-Z]{1,3}>')
for i in range(n):
    line = input().split()
    m= pattern.search(line[1])
    if m:
        print(line[0]+" "+line[1])















#Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUTT
import re
n = int(input())

pattern = re.compile(r'#[a-fA-F0-9]{3,6}')
for _ in range(n):
    s = input()
    x=s.split()
    if len(x)>1  and  '{' not in x:
        m = re.findall(pattern, s)
        if m:
            [print(i) for i in m]



#HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT 
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            print('->',attr[0],'>',attr[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attr in attrs:
            print('->',attr[0],'>',attr[1])
s=""
n = int(input())
for _ in range(n):
    s += input()
parser = MyHTMLParser()
parser.feed(''.join(s))

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        if data != "\n":
            print(">>> Data")
            print(data)
    def handle_comment(self,data):
        if "\n" not in data:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            print(data)                        
    
    

  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
  
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->",attr[0],">",attr[1])
    
        
        
s=""
N = int(input())
for _ in range(N):
    s += input()
parser = MyHTMLParser()
parser.feed(''.join(s))

#Validating UID 
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


n = int(input())
for _ in range(n):
    s = input()
    pattern = r'(.*[A-Z].*){2,}'
    pattern1 = r'(.*\d.*){3,}'
    if (len(s)==10 and s.isalnum()) and bool(re.match(pattern,s)) and bool(re.match(pattern1,s)) and len(set(s))==10:
        print("Valid")
    else:
        print("Invalid")









#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
pattern = r'^[4|5|6](\d){3}([ |-]?(\d){4}){3}$'
t=[]
diff=True
for _ in range(n):
    t=[]
    diff=True
    s = input()
    m = re.search(pattern,s)
    for i in range(len(s)):
        if (s[i]!="-" and s[i]!=" "):
            t.append(s[i])
    #print(t)
    for i in range(0,len(t)-3):
        #print(t)
        #print(set(t[i:i+4]))
        if len(set(t[i:i+4]))==1:
               diff=False
  
    if m and diff:
        print("Valid")
    else:
        print("Invalid")

#Arrays


def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    a = numpy.array(arr,float)
    return a

    



#Shape and Reshape
import numpy

line = list(map(int,input().split()))
arr = numpy.array(line)
arr.shape = (3,3)
print(arr)



#Transpose and Flatten
import numpy
N, M = input().split()
arr = [list(map(int, input().split())) for _ in range(int(N))]
matrix = numpy.array(arr)
print(numpy.transpose(matrix))
print(matrix.flatten())
    



#Concatenate
import numpy
N,M,P=input().split()
arr1 = [list(map(int, input().split())) for _ in range(int(N))]
matrix1 = numpy.array(arr1)
arr2 = [list(map(int, input().split())) for _ in range(int(M))]
matrix2 = numpy.array(arr2)
print(numpy.concatenate((matrix1,matrix2),))

#Zeros and Ones
import numpy
dim = tuple(map(int,input().split()))
print(numpy.zeros((dim),dtype=numpy.int))
print(numpy.ones((dim),dtype=numpy.int))



#Eye and Identity
import numpy
numpy.set_printoptions(legacy="1.13")
N,M = input().split()
print(numpy.eye(int(N),int(M)))


#Array Mathematics
import numpy
N,M = map(int, input().split())
matrix1 =  numpy.array([list(map(int,input().split())) for _ in range(N)])
matrix2 = numpy.array([list(map(int,input().split())) for _ in range(N)])
print(matrix1+matrix2)
print(matrix1-matrix2)
print(matrix1*matrix2)
print(matrix1//matrix2)
print(matrix1%matrix2)
print(matrix1**matrix2)

#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')
arr = list(map(float,input().split()))
A = numpy.array(arr)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

#Sum and Prod
import numpy
N,M = map(int,input().split())
arr = [list(map(float,input().split())) for _ in range(N)]
A = numpy.array(arr)
somma = numpy.sum(A,axis=0)
B = numpy.array(somma)
prodotto = numpy.prod(B,axis=None)
print(int(prodotto))


#Min and Max
import numpy
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
A = numpy.array(arr)
min0 = numpy.min(A,axis=1)
B = numpy.array(min0)
print(numpy.max(B))


#Mean, Var, and Std
import numpy
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
A = numpy.array(arr)
print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A,axis=None),11))



#Dot and Cross
import numpy
N = int(input())
arr1 = [list(map(int,input().split())) for _ in range(N)]
arr2 = [list(map(int,input().split())) for _ in range(N)]
A = numpy.array(arr1)
B = numpy.array(arr2)
Bt = numpy.transpose(B)
product=numpy.zeros((N,N),dtype=int)
for i in range(N):
    for j in range(N):
        product[i][j]=numpy.dot(A[i],Bt[j])
        
print(product)

#Inner and Outer
import numpy
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(numpy.inner(A,B))
print(numpy.outer(A,B))


#Polynomials
import numpy
coeff = list(map(float,input().split()))
P = float(input())
print(numpy.polyval(coeff,P))




#Linear Algebra
import numpy
N = int(input())
arr = [list(map(float,input().split())) for _ in range(N)]
print(round(numpy.linalg.det(arr),2))



#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        lista=[]
        for elem in l:
            number = '+91 '+elem[-10:-5]+' '+elem[-5:]
            lista.append(number)
        lista=f(lista)
        return lista
            
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


#Birthday Cake Candles
#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    #maxi = max(candles)
    #numb=0
    '''for elem in candles:
        if elem==maxi:
            numb+=1
    return numb'''
    c = Counter(candles)
    maxi=max(candles)
    numb =c[maxi]
    return numb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    result=''
    if v1>v2 and (x2-x1)%(v2-v1)==0:
        result='YES'
    else:
        result='NO'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()




#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    people_shared=5
    people_like=0
    for i in range(n):
        recipient = (people_shared)//2
        people_shared = recipient*3
        people_like += recipient
    return people_like
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    #I see part this code on the discussions of Hackerrank because mine was correct but gives Runtime Error
    if(len(n)==1 and k==1):
        return int(n)
    else:
        somma = sum(list(map(int,n)))
        return superDigit(str(somma*k),1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    old=arr[-1]
    for i in range(n-1,-1,-1):
        if old>arr[i-1]:
            arr[i]=old
            print(*arr)
            return arr
        else:
            if i==0:
                arr[i]=old
            else:
                arr[i]=arr[i-1]
            print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    #I see this code on the discussions of Hackerrank
    for i in range(1,n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Validating Postal Codes
regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"	# Do not delete 'r'.



#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


string1=''
for j in range(m):
    for i in matrix:
        string1+=(i[j])

pattern = r'[$!@#%& ]{0,}[A-Za-z0-9]{,}[$!@#%& ]{0,}?'
pattern1 = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
m = re.findall(pattern,string1)
string = ''.join(m)
print(re.sub(pattern1,' ',string))
        
    
    


#XML 1 - Find the Score


def get_attr_number(node):
    count=0
    for child in node.iter():
        count+=len(child.attrib)
    
    return count


#XML2 - Find the Maximum Depth


maxdepth = 0
def depth(root, level):
    global maxdepth
    # your code goes here
    if len(root)>0:
        level+=1
        if(maxdepth<=level):
            maxdepth=level+1
        for elem in root:
            depth(elem,level)
    return maxdepth



