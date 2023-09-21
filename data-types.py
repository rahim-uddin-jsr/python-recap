####### Standard data types


### Number

# integer
a=52

# complex type 
c = 1+3j  

# floating type 
b=50.22

""" print(type(a)) #integer
print(type(b)) #complex
print(type(c)) #float """


### Sequence Type
    # string
    # list
    # tuple
# string
name='Rahim Uddin' #thats string type data

#list 
### LIST CAN BE MANIPULATED  ###
fruits=['apple','banana','mango','guava','orange'] #list type
more_fruits=['coconut','grapes','watermelon']
# List slicing  
# print (fruits[3:])  
# print (fruits[:3])  
# print (fruits[3])  
# print (fruits[0:3]) 

# list concatenation 
new_list=fruits+more_fruits
# print(new_list)

# list repetition using Operator
# print(new_list*5)


#tuple 

#### TUPLE IS READ ONLY DATA ####
fruits_name=('apple','banana','mango','guava','orange') #list type

""" print(type(name))
print(type(fruits))
print(type(fruits_name)) """




# dictionary
student_info={
    'std_name':'Rahim Uddin',
    'std_roll':127219,
    'std_class':'Seven'
}


print(student_info['std_name'] )
keys_of_student_info=student_info.keys()
values_of_student_info=student_info.values()
""" print(keys_of_student_info )
print(values_of_student_info ) """


#### Boolean

is_friend=True
is_job_holdar=False
""" 
print(type(is_friend))
print(type(is_job_holdar)) """


#######SET

# creating empty set 

set=set()

set_2={'ami','tumi',52,'amra'}

print(set)

# added item in set 
set_2.add('added later')
print(set_2)
# remove from set 
set_2.remove('added later')
print(set_2)