print(''' Welcome to our house
The house has four important rooms
1.loofing area
2.kitchen
3.bathrom and the toilet
4.bedrooms ''')

room_chose_text = input('Please enter the room number: ')
room_number = int(room_chose_text)

if room_number == 1:
    print('you have choosen the loofing area')
    print('there is an age limit to use that area')
else:
    age_room = input('Please enter your age: ')
    age = int(age_room)
if room_number == 2:
    print('You have selected the Kitchen')
    if age >= 20 :
        print('You can go to the kitchen.')
else:
    print('Sorry. You are too young.')

if room_number == 3:
    print('You have selected the bathrom and the toilet')
    if age >= 5:
        print('You can go on the bathroom or toilet.')
else:
    print('Sorry. You are too young.')
if room_number == 4:
    print('You have selected The Bedroom ')
    if age >= 25:
# Age is not too low
        if age > 35:
# Age is too high
            print('Sorry. You are too old.')
    else:
# Age is in the correct range
        print('You can go on the bedroom.')
else:
# Age is too low
    print('Sorry. You are too young.')
