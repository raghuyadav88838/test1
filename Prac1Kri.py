# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:50:41 2021

@author: raghu
"""

2+2
4*5
10/2
10**2
20*'str'
type(False)
"Hello"
'raghu'
a=100
type(a)
a='chinnu'
type(a)
a=1
b=2
print(a*b)
print(a/b)
print((a*b)+(a/b))
first_name='Raghu'
last_name='Chintu'
print("My first name is {} and last name is {}".format(first_name,last_name))
len('raghu')     
my_str="ChinnuChintu12"
my_str.isalnum()
my_str.startswith('C')
True and True
True and False
True or False
lst_example=[]
type(lst_example)
lst=list()
type(lst)
lst=['math', 'Chem', 100, 200, 300]
type(lst)
len(lst)
lst.append("Raghu") #append means add elements in the list
lst
lst[5] #indexing the list
lst[:]
lst[1:5]
lst.insert(2,"Wick") #insert in specific order
lst
lst.append(["Hello World"])
lst
lst=[1,2,3,4,5]
lst.extend([6,7]) #extend method
lst
lst=[1,2,3,4,5]
sum(lst) #to sum
lst.pop() #pop() method
lst
lst.pop(0)
lst
lst=[1,1,1,2,2,3,4,4,4,4,4]
lst.count(1) #Calculate total occurance of given element of list
lst.count(4)
len(lst)
list.index(3,1,10) #index doubt?
min(lst)
max(lst)
# sets, A set is an unordered collection data type that is iterable mutable and has no duplicate elements
set_var=set()
print(set_var)
print(type(set_var))
set_var={"wick","bill","don"}
print(set_var)
type(set_var)
set_var.add("miller") #to add 
print(set_var)
set1={"wick","bill","don"}
set2={"wick","bill","don","sam"}
set2.difference(set1)
set2.difference_update(set1)
print(set2)
set2.intersection(set1)
set2.intersection_update(set1)
set2
#Dictionaries- it is a collection which is unordered changable indexed. written curly brac have keys and values
dic={}
type(dic)
dic={1,2,3,4}
type(dic)
#lets create a dictionary
my_dict={"bike1":"Honda","bike2":"Hero","bike3":"pulser"}
type(my_dict)
my_dict['bike1'] #bike1 is key 
my_dict['bike2']
my_dict['bike3']
#we can even loop through dic values
for X in my_dict:print(X) #for key
for X in my_dict.values():print(X) #for values
for X in my_dict.items():print(X)
my_dict['bike4']='enfield' #to add items in dic
my_dict
my_dict['bike1']='bajaj'
my_dict
#Nested Dic
car1_model={'Maruthi': 1950}
car2_model={'Wagon': 1970}
car3_model={'Benz': 1980}
car_type={'car1':car1_model,'car2': car2_model,'car3': car3_model}
print(car_type)
print(car_type['car1'])
print(car_type['car1']['Maruthi'])
#tuples
my_tuple=tuple()
type(my_tuple)
my_tuple=()
type(my_tuple)
my_tuple=("raghu","babu","sai")
my_tuple[0]
#tuples can be used where the definition of item is required just for one time
my_tuple=("raghu","babu","sai")
print(type(my_tuple))
print(my_tuple)
my_tuple.count('raghu')
my_tuple.index('sai')

pip install numpy
import numpy as np
my_list=[1,2,3,4,5]
arr=np.array(my_list)
type(arr)
arr
arr.shape
#multinested array [] one dimentional array [[]] 2 dimentional array
my_lst1=[1,2,3,5]
my_lst2=[2,5,6,7]
my_lst3=[4,1,9,8]
arr=np.array([my_lst1,my_lst2,my_lst3])
arr
arr.shape #check the shape of array
arr.reshape(4,3)
#indexing   To retrive the data
arr
arr[:,:]
arr[0:2,0:2]
arr[1:3,2:4]
arr=np.arange(0,10,step=2)
arr
np.linspace(1,10,50)
arr=np.array([1,2,3,4,5,6,7,8,9])
arr[3:]=100 #copy function and broadcasting
arr
arr1=arr
arr1[3:]=500
print(arr1)
arr
arr1=arr.copy()
print(arr)
arr1[3:]=1000
print(arr1)
arr
#some conditions are very useful in EDA
val=2
arr>2
arr*2
arr[arr>2]
arr[arr<2]
np.ones(4)
np.ones(4,dtype=int)
np.ones(5,dtype=float)
np.ones((2,5),dtype=int)
# random distribution
np.random.rand(3,3)
arr_ex=np.random.randn(4,4)
arr_ex

pip install pandas
import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['Column1','Column2','Column3','Column4'])
df.head()
df.to_csv('Test1.csv')
#Accessing the elements > 1. .loc 2. .iloc
df.loc['Row1']
type(df.loc['Row1'])
#series can be any 1 row or 1 column
df.iloc[:,:]
df.iloc[0:3,0:2]
