
# coding: utf-8

# Task 1.1.1: Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[1]:


import operator
def myreduce(function, Data, initial=None):
    #function: function(x,y) ; Data    : [a1,a2,a3,...,an] ; initial : Start the Calculation from this Value
    
    #iterator function can be used to take next values because it provides next functionality
    it = iter(Data) 

    #First Value can be taken from initial parameter or next as mentioned below
    if initial is None:
        try:
            initial = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
            
    #Step 1: function(a1,a2): a1 is always calculated value        
    calculated_value = initial
    for new_value in it:
        #Step 2: Loop for Taking always Calculated Value and passing new Value as x
        # function(calculated_value, a2): Here a2 will be replaced by new_value.
        calculated_value = function(calculated_value, new_value)
    return calculated_value
print(myreduce(lambda a,b : a+b,[1,2,3,4,5,]))
print(myreduce(operator.add,(1,2,3,4,5)))


# Task 1.1.2:Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[2]:


def myfilter(functionOrNone, iterable): #filter(function or None, iterable) --> filter object
    if functionOrNone is None:
        functionOrNone = bool           #If function is None, return the items that are true.
    for check_value in iterable:        #Check for each value in Iterable one by one for passing into function 
        if functionOrNone(check_value): #If condition satify, function returns true 
            yield check_value           #Yield suspends function’s execution and sends a value back to caller
                                    #If the body of a def contains yield, the function automatically becomes a generator function

print(list(myfilter(None,[1,2,3,4,5,6])))
print(list(myfilter(lambda x:x%2==0,(1,2,3,4,5,6))))


# Task 1.2: Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[3]:


lst1=[' {0}'.format(row) if row=='D' else row for row in 'ACADGILD']
print(lst1)
lst2=[i*j for i in 'xyz' for j in range(1,5)] #first xyz loop will do string multiplication with range inner loop numbers
print(lst2)
lst3=[i*j for j in range(1,5) for i in 'xyz'] #first range loop numbers will do string multiply with xyz inner loop string
print(lst3)
lst4=[[i+j] for j in range(1,4) for i in range(1,4)]  #outer and inner loop with same range with output of [i+j]
print(lst4)
lst5=[list(range(i, i+4)) for i in range(2,6)]        #loop 2 to 5 and generate list with i+4
print(lst5)
lst6=[(i,j) for j in range(1,4) for i in range(1,4)]  #inner and outer loop with (i (inner),j (outer))
print(lst6)


# Task 1.3: Implement a function longestWord() that takes a list of words and returns the longest one.

# In[4]:


def longestWord(list_of_words):
    k=list(map(lambda x:len(x),list_of_words)) #map returns equivalent words' length in the list format
    j=k.index(max(k))                          #getting maximum value from list and also getting index of it
    return list_of_words[j]                    #based on index finding the word and returning it
    
print(longestWord(['a','ab','abc','abcd']))
print(longestWord(['wxyz','wxy','wx','w']))
print(longestWord(['my','name','is','Mayur','Pethani']))
print(longestWord(['This','assignment','is','from','AcadGild']))


# Task 2.1.1: Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

# In[5]:


class Triangle:
    def __init__(self):
        self.a = float(input('Enter first side of Triangle : '))
        self.b = float(input('Enter second side of Triangle : '))
        self.c = float(input('Enter third side of Triangle : '))
    def __str__(self):
        return  ('\nTriangle:\tFirst Side: ' + str(self.a) + '\n\t\tSecond Side :' + str(self.b) + '\n\t\tThird Side : ' + str(self.c))
class Area(Triangle):
    def __init__(self,param):
        self.param=param
    def __str__(self):
        s = (self.param.a+self.param.b+self.param.c)/2
        area = (s*(s-self.param.a)*(s-self.param.b)*(s-self.param.c)) ** 0.5
        return "\nArea of Triangle is : %0.2f" %area
t=Triangle()
print(t)
a=Area(t)
print(a)


# Task 2.1.2: Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n

# In[6]:


def filter_long_words(list_of_words,n):
    l=list()
    for words in list_of_words:
        if len(words) > n:
            l.append(words)
    return l
print(filter_long_words(['abc','dadfasdf','a','aa'],2))
print(filter_long_words(['a','ab','abc','abcd'],3))
print(filter_long_words(['wxyz','wxy','wx','w'],4))
print(filter_long_words(['my','name','is','Mayur','Pethani'],5))
print(filter_long_words(['This','assignment','is','from','AcadGild'],6))


# Task 2.2.1 : Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[7]:


def giveLen(lst):
    return [len(row) for row in lst] #Example of list comprehension
lst=['ab','cde','erty']
Final_lst=giveLen(lst)
Final_lst


# Task 2.2.2 : Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise.

# In[8]:


def IsVowel(char):
    if(len(char)==1):
        if(char.lower() in 'aeiou'):
            return True
        else:
            return False
    else:
        return False
    
    
    
    
    
    
    


# In[9]:


IsVowel('a')

