"""
# Some Theory:
    Types of data used for I/O:
        Text - '12345' as a sequence of unicode chars.
        Binary - 12345 as a sequence of bytes of its binary equivalent.

# Hence there are 2 file types to deal with
    Text files - All program files are text files.
    Binary Files - Images,music,video,exe files.

# How File I/O is done in most programming languages
    Open a file
    Read/Write data
    Close the file
"""

# Writting to the file. 
# case 1: if the file is not present. 
f = open('sample.txt','w')
f.write("Hello World")
f.close()
# since file is closed hence this will not works. 
# f.write("helloword")

# write multiline strings. 
f = open('sample1.txt','w')
f.write("hellow world")
f.write("\nhow are you ?")
f.close()

# Case 2: If the file is already present. 
f = open('sample.txt','w')
f.write('salman khan')
f.close()

# open() --> load the file into the RAM(buffer memory). 

# Problem with w mode. 
# introducing append mode. 
f = open('sample1.txt','a')
f.write('\nI am fine.')
f.close()

# write lines. 
L = ['Hello\n','Hii\n','How are you ?\n','I am fine.\n']
f = open('sample1.txt','w')
f.writelines(L)
f.close()

# reading from files. 
# -> using read()
f = open('sample.txt','r')
s = f.read()
print(s)
f.close()

# reading up to n chars.
f = open('sample.txt','r')
s = f.read(10) # reading up to 10 chars. 
print(s)
f.close()

# readline() -> to read the content line by line.
f = open('sample1.txt','r')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

# Note: 
# read -> reading the whole documents. 
# readline -> when we have large files and we don't want to load large files into the RAM. 

# reading entire using readline. 
print('\n---------------------------------')
print('reading entire using readline')
f = open('sample1.txt','r')

while f.readline() != '':
    print(f.readline(), end='')

f.close()
print('---------------------------------\n')

# Using context manager(With):
# if we don't close file, garbage collector would close it. 
# with keyword closes the file as soon as the usage is over. 
print('\n---------------------------------\n')
print("Use of 'with' keyword" )

with open('sample1.txt','w') as f:
    f.write("Hello salman Bhaii, When your next movie will release ...... !")

# try f.read() now. 
with open('sample1.txt', 'r') as f:
    print(f.read())
print('---------------------------------\n')

# Moving within a file -> 10 char then 10 char. 
print('\n---------------------------------')
print('Moving within a file -> 10 char then 10 char. ')
with open('sample1.txt','r') as f:
    print(f.read(10)) # print first 10 character. 
    print(f.read(10)) # print next 10 character. 

    # buffer memory track the location of the cursor. 

# benefits -> to load a big file in memory. 
print('\n---------------------------------')
print('benefits -> to load a big file in memory. ')
big_L = ['hello world' for i in range(1000)]

with open('big.txt','w') as f:
    f.writelines(big_L)

with open('big.txt','r') as f:
    chunk_size = 10

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size))
        f.read(chunk_size)

print('---------------------------------\n')

# seek and tell function. 
print('---------------------------------\n')
print('seek and tell function.')
with open('sample1.txt','r') as f:
    print(f.read(10))
    print(f.tell()) # mechanism to tell which next character will process. 
    f.seek(0) # move the cursor to the zero. 
print('---------------------------------\n')

# seek during write time. 
print('---------------------------------\n')
print('seek during write time.')
with open('sample1.txt','w') as f:
    f.write('hello')
    f.seek(0)
    f.write('X')

print('---------------------------------\n')

# Problems with working in text mode. 
# -> can't work with binary files like images. 
# -> not good for other data types like int/float/list/tuples. 
# working with binary files
print('\n---------------------------------')
print('# working with binary files')
print("Below code will not works since this is an image which is in binary format. ")
# with open('GAN in Practice.png','r') as f:
#     f.read()

with open('GAN in Practice.png','rb') as f:
    with open('gan_copy.jpg','wb') as wf:
        wf.write(f.read())
print('---------------------------------\n')

# not good for other data types like int/float/list/tuples.
# working with other data types. 
print('\n---------------------------------')
print('working with other data types.')
with open('sample.txt','w') as f:
    f.write('5')

# more complex data type. 
d = {
    'name':'netra',
    'age':23,
    'gender':'male'
}

with open('sample.txt','w') as f:
    f.write(str(d))

with open('sample.txt','r') as f:   
    f.read() # string can't be converted into the dictionary. 
    print(type(f.read()))
print('---------------------------------\n')

# Serialization and Deserialization. 
print('\n---------------------------------')
print("Serialization and Deserialization. ")
print("Serilization: process of converting python data types to JSON format.")
print("Deserilization: process of converting JSON to python data types.")

# serilization using json module 
# list 
import json 
L = [1,2,3,4]
with open('demo.json','w') as f:
    json.dump(L,f)
# f -> file handler Object.

# dict 
d = {
    'name':'netra',
    'age':23,
    'gender':'male'
}
with open('demo.json','w') as f:
    json.dump(d,f, indent=4)

# Deserialization
import json 
with open('demo.json','r') as f:
    print(json.load(f))
    print(type(d))

# serialize and deserialize tuple:
import json 
t = (1,2,3,4,5)

with open('demo1.json','w') as f:
    json.dump(t,f)

# some files can contains dict and list. 
d = {
    'student':'netra',
    'marks':[23,35,56,77]
}

with open('demo3.json','w') as f:
    json.dump(d,f)

# Serializing and Deserializing with Custom Objects. 
print("------------------")
print(" Serializing and Deserializing with Custom Objects. ")
class Person:

    def __init__(self,fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
    
    # format to printed in 
    # -> Netra Khatri age -> 24 gender -> male

person = Person('Netra','Khatri',24,'male')

# As a string. 
import json 

def show_object(person):
    if isinstance(person, Person):
        return "{} {} age -> {}".format(person.fname, person.lname, person.age, person.gender)
    
with open('demo4.json','w') as f:
    json.dump(person,f,default=show_object)
print("------------------------------\n")

# Pickling
print("\n------------------------------")
print("Pickling: Python Object converted into the byte stream.\n unpickling: inverse operation")
class Person1:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Hi my name is ", self.name, " and I am ", self.age, " years old.")

p = Person1('Netra',24)

# pickle dump
import pickle 
with open('person.pkl','wb') as f:
    pickle.dump(p,f)

with open('person.pkl','rb') as f:
    p1 = pickle.load(f)
    p1.display_info()

print("------------------------------\n")

print("Differences between Pickle Vs Json")
# Pickle : lets the user to store the data into the binary format. 
# Json : lets the user to store the data into the human readable format. 


