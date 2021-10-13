# Basics of Python


# types of data in python3
def types_of_data():
    # _____________Types of data in python3____________________

    # strings-anything between "________" or this '_____________' is known as string
    a = ""
    print(type(a))

    # Lists-anything between [_________] is called list
    l = []
    print(type(l))

    # Tuple-anything between (__________) is called tuple
    t = ()
    print(type(t))

    # Dictenory-Anything between {__________} is called dictenory
    d = {}
    print(type(d))

# more about strings


def string_indexing():
    # so strings can edited in many ways
    # lets first learn about how to count strings
    #  012345
    # "Sample"
    # here index position of S is 0 , a is 1 and so on
    # For example
    s = "sample"
    print(s.index('s'))


def string_slicing():
    # lets learn how to manupulate strings
    # for example
    s = "sample"
    print(s[4])
    print(s[0:4])
    print(s[5])
    print(s[-1:-5])
    print(s[1:])
    print(s[::-1])  # to reverse a string

def string_substituion():
    # strings can be modified by index
    s = 'sample'
    s[3] = 'r'
    print(s)
def ways_to_make_anything_string():
    #method one
    #direct assignment
    a='sample'
    
    #method two 
    #using str()
    a=1234
    a=str(a)
    
#basic calculations and logic
def equalsto_aur_double_equals_ka_difference():
    #0=True
    #1=False
    # == is for comparing two values
    # = is for adding a value to a variable 
    a=100 
    b=200
    print(a==b)
    print('a is: ',a,'b is: ',b)
    b=a
    print(a==b)
    print('a is: ',a,'b is: ',b)
def variable_management():
    #variable management
    a=100
    b=200
    a=b
    print('a: ',a , 'b: ', b )
    c=a+b
    print('a: ',a , 'b: ', b ,'c; ',c)
    b=c+a
    print('a: ',a , 'b: ', b ,'c; ',c)
    b=a
    print('a: ',a , 'b: ', b ,'c; ',c)
    a=b+c
    print('a: ',a , 'b: ', b ,'c; ',c)
    print(a)

#basic Functions and user input and output 
def basic_funtions():
    
    #print() funtion- used to output a value to the user 
    print('hello world')
    a="bye world"
    print(a)
    
    #input() funtion- used to take input from a user 
    #syntax a=input('enter a number: ')
    #       |           |
    #    a variable     |
    #               the line it will show to the user 
    #output<<
    #>>>enter a number: 
    b=input('a number:')
    

#more about lists
def list_indexing():
    #list can do everything string can and a little bit more 
    # so lists can be edited in many ways
    # lets first learn about how to count lists
    #  0 1 2 3 4 5
    # [S,a,m,p,l,e]
    # here index position of S is 0 , a is 1 and so on
    # For example
    l = ['s','a','m','p','l','e']
    print(l.index('s'))

def nested_lists():
    l=['1','2','3','4',['1','2','3','4'],'5']
    print(l[4])
    print(l.index([1,2,3,4]))
def list_slicing():
    # lets learn how to manupulate lists
    # for example
    l = ['s','a','m','p','l','e']
    print(l[4])
    print(l[0:4])
    print(l[5])
    print(l[-1:-5])
    print(l[1:])
    print(l[::-1])  # to reverse a list
def nested_list_slicing():
    l=['1','2','3','4',['1','2','3','4'],'5']
    print(l[4][3])
    print(l[4][0])

def list_substituion():
    # lists can be modified by index
    l = ['s','a','m','p','l','e']
    l[3] = 'r'
    print(l)
def ways_to_make_anything_list():
    #method one
    #direct assignment
    l = ['s', 'a', 'm', 'p', 'l', 'e']
    
    #method two 
    #using str()
    a='lists' 
    a=list(a)
    print(a)
    
def list_funtions():
    #to add stuff to the list
    
    
    #the list.append() funtion- adds the given value to the end of list
    l=['1','2']
    l.append('dum')
    print(l) 
    
    #the slicing way
    l[0]='13'
    print(l)
    
    #the list.extend() function- adds the given value to the last 
    l.extend('hello world')
    print(l)
    
    #the list.insert()  function- inserts value to a given index
    l.insert(0,'hello')
    print(l)
    
    
    #to delete stuff from list
    
    #the list.pop(the thing you wanna delete) function- deletes the given digit from list and prints it out
    l.pop(1)
    print(l)
    
    #the list.remove(the thing you wanna delete) funtion- delets given digit from list
    l.remove('2')    
    print(l)
    
    
    
    #code written by Eeman Majumder