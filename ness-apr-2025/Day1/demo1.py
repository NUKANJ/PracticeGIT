pi = 3.14
print(type(pi))

age = 59
isEligible = age < 17
print(isEligible)
print(type(isEligible))

if age < 17:
    print('Eligible')
elif age > 58:
    print('pension')
else:
    print('not eligible')

# car_list  = ['honda','bmw','merc','hundai']
# for cars in car_list:
#     print(cars)
#     if(cars == 'hundai'):
#         print('car printed')
#     else:
#         print('end of statement')


# car_list  = ('honda','bmw','merc','hundai','honda')
# print(type(car_list))
# for cars in car_list:
#     print(cars)

# no duplications allowed in set
# car_list  = {"car1":"honda","car2":"bmw","car3":"merc"}
# print(car_list)
# print(type(car_list))

welcomeness = "welcome to ness"
wordlist = welcomeness.lower().capitalize().split(" ")
print(wordlist)
print(welcomeness.index('n'))

name = 'Sam'
welcomemsg = f'Hi {name}, welcome to python'
print(welcomemsg)

welcome = "My name is Kalyan"
wordsplit=welcome.lower().split(" ")
print(wordsplit)