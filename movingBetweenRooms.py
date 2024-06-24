#Cody Barrett


#dictionary that lists the rooms along with their key
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

#sets the Great Hall to the current room
current_room = 'Great Hall'

#continues to loop through the following
while True:
    #prints You are in and places the current room in the {}'s
    print('You are in the {}!'.format(current_room))
    #if statement that checks to see if the current room is the great hall, and prints information to the player
    if current_room == "Great Hall":
        print('You are standing in a large hallway! To your South down the hall you can see a door.')
    #similar to above but for the bedroom
    elif current_room == 'Bedroom':
        print('To your East you can see a staircase leading down somewhere. To your North you can see a door.')
    #similar to above but for the cellar
    elif current_room == 'Cellar':
        print('To your West you can see a staricase leading up.')

    #user input for where to move to, and assigns it to variable named move
    move = input('Where would you like to go? (North, South, East, West, or Quit):\n')

    #if the variable move equals Quit, the game ends
    if move == 'Quit':
        break

    #else if that checks to see if move is valid for the current room
    elif move in rooms[current_room]:
        #if move is valid, sets current room to the value in the dictionary
        current_room = rooms[current_room][move]
    #if move is not valid, prints that the player can not go there
    else:
        print("sorry, you can't go there!")







