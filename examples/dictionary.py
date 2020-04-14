# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 02:12:14 2020

@author: Novin
"""
'''
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print( dict)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print( dict)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for item in dict.items():
    print(item)
    
    
    
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_set = set(zip(keys, values))
print(color_set)


myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
    
print(myDict)    
'''
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
'''

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   }
  }
    
for key,value in student_data.items():
    print('==========================')
    print(key)
    for childkey,childvalue in value.items():
        print(childkey,childvalue)
        
    
    
  '''  
    
    
    
    
    
    
    
    

