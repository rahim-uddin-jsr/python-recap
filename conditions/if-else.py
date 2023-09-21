# find the smallest number from 3 numbers
print('Please Give me 3 Numbers')
first_number,second_number,third_number=input('Enter the value of First Number= ? \n='),input('Enter the value of Second Number= ? \n='),input('Enter the value of Third Number= ? \n=')

if (first_number>second_number and first_number>third_number):
    print('First Number '+first_number + ' is big')
elif(second_number>first_number and second_number>third_number):
    print('Second number '+second_number + ' is big')
else:
    print('Third Number'+third_number + ' is big')
