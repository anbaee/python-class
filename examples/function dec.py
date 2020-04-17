# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:24:12 2020

@author: Novin


def my_function():
  print("Hello from a function")
  
my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(country = "Norway" , university = 'IAUM'):
  print("I am from " , country ,'and university of ',university)

my_function(country ="Canada",university ='SFU')
my_function("Australia",'Monash')
my_function(country ="Iran")
my_function(university ="FIAU")
my_function()


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def power(x,y):
  powerValue = 1  
  for i in range(y):
      powerValue = powerValue * x
  return powerValue


print(power(2,3))
print(power(2,6))




def power(x,y):
  if y == 0:
      return (1)  
  else:
      return (x * power(x,y-1))
  


print(power(2,3))
print(power(2,6))


x = lambda a, b : a * b


print(x(5, 6))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)



my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

print( list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))
"""
print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))






