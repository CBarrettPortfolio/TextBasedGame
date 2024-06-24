#Cody Barrett

#dicrionary that lists rooms with their key for movement and their item
rooms = {
        'Start Room': {'South': 'Waiting Room', 'West': 'Exam Room', 'North': 'Pathology Suite'},
        'Waiting Room': {'North': 'Start Room', 'West': 'Desk Office Space', 'item': 'Staff Badge'},
        'Desk Office Space': {'North': 'Exam Room', 'East': 'Waiting Room', 'item': 'Leather Folder'},
        'Exam Room': {'South': 'Desk Office Space', 'East': 'Start Room', 'item': 'Used Syringe'},
        'Pathology Suite': {'South': 'Start Room', 'East': 'Surgical Suite', 'item': 'Used Microscope Slide',},
        'Surgical Suite': {'West': 'Pathology Suite', 'North': 'Control Room', 'East': "Dr. Senagore's Office", 'item': 'Loaded Scalpel',},
        'Control Room': {'South': 'Surgical Suite', 'item': 'Spceimen Cup (Unlabeled)'},
        "Dr. Senagore's Office": {'West': 'Surgical Suite'} #villain room
}

#creates an empty list for the player inventory
player_inventory = []


#define function game_intro that prints the intro story to the player
def game_intro():
        print("You find yourself immersed in a high-stakes investigation within the confines of a mysterious medical facility.")
        print("As a seasoned detective with a keen eye for detail, you have infiltrated the inner circle of the notorious Dr. Senagore, a respected neurologist by day and a cunning criminal mastermind by night.")
        print("Armed with incriminating evidence, you navigate through the facility's labyrinthine corridors, meticulously searching room by room for crucial items that will bring Dr. Senagore to justice.")
        print("Each discovery brings you closer to unraveling the doctor's dark secrets and exposing his illicit activities.")
        print("With determination and resourcefulness, you move stealthily through the facility, piecing together the evidence needed to confront Dr. Senagore and ensure that his reign of deception comes to an end.")
        print("The fate of justice hangs in the balance as you inch closer to the thrilling finale of this gripping tale of mystery and intrigue.")

#defines a function to pick up an item with the current room as the perameter
def pickup_item(current_room):
        #if that checks to see if the current room is a key in the dictionary and has a nested dictionary with the key item room and is not equal to none
        if rooms[current_room]['item'] != 'none':
                #assigns that dictionary entry to variable item
                item = rooms[current_room]['item']
                #sets the item in the dictionary to none
                rooms[current_room]['item'] = 'none'
                #adds the item to the player inventory list
                player_inventory.append(item)
                #tells the player they have picked up the item
                print('You found a {}!'.format(item))
                #prints the players current inventory
                print('Your inventory currently contains: {}'.format(player_inventory))
        else:
                print('There is nothing here!')


#defines a function for a room description that uses current_room as a parameter
def room_desc(current_room):
        #if that checks if the current room is the start room and prints a description of the start room
        if current_room == 'Start Room':
                print("In the vestibule of the medical facility, you find yourself standing at the entrance, surrounded by a sense of anticipation and mystery.")
                print("The room is dimly lit, with the faint hum of medical equipment echoing in the background.")
                print("As you gaze around, you notice several doors leading off in different directions, each veiled in shadows hinting at the unknown beyond.")
                input('press enter to continue...')
                print("To the South, a passage leads to the Waiting Room, where whispers of conversations and the shuffle of footsteps can be faintly heard.")
                print("The Westward door beckons you towards the Exam Room, a place of medical scrutiny and procedures.")
                print("Looking North, you catch a glimpse of the Pathology Suite, where scientific investigations unfold.")

        #else if that checks if the current room is the Waiting room and prints a description of the waiting room
        elif current_room == 'Waiting Room':
                print("In the Waiting Room, a hushed stillness envelops the space, broken only by the occasional sound of rustling papers or distant footsteps.")
                print("The room exudes a sense of anticipation, as if it holds secrets waiting to be unraveled.")
                print("Soft light filters through the windows, casting a gentle glow over the room's furnishings.")
                input('press enter to continue...')
                print("As you take in your surroundings, you notice a desk in the corner, cluttered with files and documents.")
                print("The air carries a faint scent of antiseptic, mingling with the subtle aroma of freshly brewed coffee.")
                print("Chairs line the walls, inviting visitors to sit and wait in quiet contemplation.")
                input('press enter to continue...')
                print("Near the reception desk, there is a glint of metal on the floor.")
                print("This spot seems to hold a hidden potential, a place where an item of significance might be found.")
                print("The atmosphere in the room suggests that there are hidden treasures waiting to be discovered, adding an air of mystery to your investigation within the medical facility.")

        # similar to above but for the Desk office space
        elif current_room == 'Desk Office Space':
                print("In the desk office space, a sense of purpose and efficiency fills the air.")
                print("The room is organized with precision, every item in its designated place.")
                print("The hum of computers and printers provides a backdrop of productivity, while the aroma of freshly brewed coffee lingers in the air.")
                input('press enter to continue...')
                print("The desk is a focal point, commanding attention with its neat stacks of papers and array of office supplies.")
                print("A computer screen displays a screensaver, momentarily idle in the midst of a busy workday.")
                print("The ergonomic chair invites you to take a seat, offering a moment of respite in the midst of your investigation.")
                input('press enter to continue...')
                print("Amidst this professional setting, there is a drawer that catches your eye.")
                print("It seems to hold a hidden potential, a space where an item of significance might be concealed.")
                print("The desk office space hints at a wealth of information and possibilities, waiting to be uncovered as you delve deeper into your quest within the medical facility.")

        #similar to above but for the exam room
        elif current_room == 'Exam Room':
                print("In the exam room, a sense of anticipation and vulnerability lingers in the air.")
                print("The room is designed for comfort and functionality, with medical equipment neatly arranged and a sterile cleanliness pervading the space.")
                print("Soft lighting creates a soothing ambiance, while the faint sound of a ticking clock adds a sense of urgency.")
                input('press enter to continue...')
                print("The examination table stands at the center, a symbol of both healing and vulnerability.")
                print("Posters on the walls display anatomical diagrams and health information, serving as educational aids for patients.")
                print("The room is a sanctuary for healing, where patients place their trust in the expertise of medical professionals.")
                input('press enter to continue...')
                print("As you explore the exam room, your gaze falls upon a cabinet in the corner.")
                print("It holds a promise of hidden secrets, a space where an item of significance might be concealed.")
                print("The room exudes a mix of apprehension and hope, creating a backdrop for pivotal moments in patients' health journeys.")
                print("There is a sense of discovery waiting to unfold within the confines of the exam room, inviting you to uncover its mysteries.")

        #similar to above but for the pathology suite
        elif current_room == 'Pathology Suite':
                print("In the pathology suite, a sense of precision and analysis fills the air.")
                print("The room is meticulously organized, with shelves lined with specimen containers and microscopes ready for examination.")
                print("The sterile environment is a testament to the importance of accuracy in diagnosing and treating illnesses.")
                input('press enter to continue...')
                print("The hum of laboratory equipment provides a constant background noise, indicating the ongoing work of analyzing samples and identifying diseases.")
                print("The room is illuminated by bright fluorescent lights, casting a clinical glow on the various tools and instruments scattered across the counters.")
                input('press enter to continue...')
                print("The pathology suite is a realm of investigation and discovery, where medical professionals unravel the mysteries of disease through careful examination of tissues and cells.")
                print("The microscope is a focal point, offering a window into the microscopic world of pathology.")
                input('press enter to continue...')
                print("As you navigate the pathology suite, your attention is drawn to a locked cabinet in the corner.")
                print("It hints at confidential information and guarded secrets, holding the key to understanding complex medical conditions.")
                print("The room exudes a sense of purpose and determination, as experts work diligently to provide accurate diagnoses and insights into patients' health.")
                print("There is an aura of expertise and precision in the pathology suite, inviting you to delve deeper into the world of medical investigation.")

        #similar to above but for the surgical suite
        elif current_room == 'Surgical Suite':
                print("In the Surgical Suite, a sense of precision and focus fills the air, palpable in the meticulous arrangement of tools and equipment.")
                print("The room is bathed in a sterile white light, casting sharp shadows against the gleaming surfaces.")
                print("The hum of machinery provides a steady background rhythm, underscoring the gravity of the procedures performed within these walls.")
                input('press enter to continue...')
                print("As you step into the suite, you are struck by the sight of surgical instruments neatly arranged on trays, their edges glinting under the bright lights.")
                print("The air is heavy with the scent of disinfectant, a reminder of the sterile environment necessary for delicate surgeries.")
                print("Monitor screens display vital signs in a constant stream of data, a visual symphony of life and health.")
                input('press enter to continue...')
                print("Amidst this clinical setting, your eyes are drawn to a small alcove near the surgical table.")
                print("There, a faint glimmer catches your attention, hinting at a spot where an item of importance might be concealed.")
                print("Could this alcove hold a key piece of the puzzle in your investigation, shedding light on the mysteries that unfold within the Surgical Suite?")
                input('press enter to continue...')
                print("The atmosphere in the suite is charged with a sense of urgency and purpose, beckoning you to explore further and uncover the secrets that lie beneath the surface.")
                print("The hidden spot in the alcove tantalizes with the promise of discovery, offering a glimpse into the intricate web of intrigue that surrounds the medical facility.")

        #similar to above but for the control room
        elif current_room == 'Control Room':
                print("In the Control Room, a hum of activity fills the air, punctuated by the soft whirring of machinery and the occasional beep of monitors.")
                print("Screens flicker with data streams, displaying intricate diagrams and graphs that hint at the inner workings of the facility.")
                print("Control panels line the walls, adorned with buttons and switches that seem to hold the power to shape the course of events.")
                input('press enter to continue...')
                print("As you step into the room, a sense of command and authority washes over you, fueled by the knowledge that this is where decisions are made and actions are coordinated.")
                print("The room is bathed in a soft, artificial light that casts a futuristic sheen over the high-tech equipment and consoles.")
                input('press enter to continue...')
                print("Amidst this controlled chaos, your gaze is drawn to a corner of the room where a gleam catches your eye.")
                print("A small, inconspicuous keycard lies on a console, seemingly forgotten in the midst of the bustling activity.")
                print("Could this keycard be the key to unlocking secure areas or accessing confidential information within the facility?")
                input('press enter to continue...')
                print("The Control Room beckons you to explore its inner workings, to decipher the intricacies of its systems and unravel the mysteries that lie at the heart of the facility.")
                print("As you ponder the significance of the keycard, you sense that it holds the potential to open doors to hidden truths and unveil secrets that are waiting to be uncovered.")

        #similar to above but for Senagore's office
        elif current_room == "Dr. Senagore's Office":
                #if that checks for if the player has all 6 items
                if len(player_inventory) != 6:
                        #prints out game lose case
                        print("The air is heavy with tension as you push open the door and step inside, your eyes meeting the chilling gaze of the mad scientist himself.")
                        print("Dr. Senagore's sharp eyes sweep over you, assessing your presence with a knowing look. It becomes apparent to him that you are not his trusted assistant,")
                        print("for you lack the essential items that would mark you as a legitimate member of his medical team.")
                        print("A sly smile curls at the corners of his lips as he reaches for a mysterious syringe on his desk.")
                        input('Press enter to continue...')
                        print("Before you can react, he swiftly injects you with the contents of the syringe.")
                        print(" A wave of dizziness washes over you, and the room begins to spin.")
                        print("Your vision blurs, sounds fade into a distant echo, and the world around you slowly fades to black...")
                        print('YOU LOSE THE GAME!')
                        input("Press enter to exit")
                #else for when the player has all 6 items
                else:
                        #prints out the win case
                        print("With a steely resolve, you stride into Dr. Senagore's office, carrying the weight of the evidence you've meticulously gathered throughout your investigation.")
                        print("The six crucial items clutched in your hands serve as both a testament to the doctor's malevolence and your unwavering determination to bring him to justice.")
                        input('Press enter to continue...')
                        print("As you enter, Dr. Senagore initially mistakes you for his assistant, a fleeting sense of familiarity crossing his features at the sight of you bearing the incriminating items.")
                        print("However, as he studies you more closely, a realization dawns in his eyes - you are not who he thought you were.")
                        print("The facade of calm authority falters for a brief moment, a glimmer of unease betraying his composed demeanor as he recognizes you as an undercover cop.")
                        input('Press enter to continue...')
                        print("Quick to regain his composure, Dr. Senagore reaches for the familiar syringe, his intent clear.")
                        print("However, this time you are prepared. With a swift and calculated move, you evade his attempt to inject you, the syringe harmlessly grazing the air where you once stood.")
                        input('Press enter to continue...')
                        print("Before the doctor can react, the sound of heavy footsteps echoes through the room as law enforcement officers burst in, their presence a beacon of authority and justice.")
                        print("In a swift and coordinated effort, they swarm around Dr. Senagore, restraining him before he can make another move.")
                        input('Press enter to continue...')
                        print("As the doctor is led away in handcuffs, his once-imposing figure now reduced to a defeated shadow of his former self, you stand victorious.")
                        print("The weight of your mission lifts from your shoulders, replaced by a sense of accomplishment and closure.")
                        input('Press enter to continue...')
                        print("The room buzzes with the energy of a successful operation, the culmination of your undercover investigation leading to the downfall of a dangerous criminal.")
                        print("Justice prevails, thanks to your courage and unwavering dedication to the truth.")
                        print('YOU WIN!')
                        input("Press enter to exit")

#sets the current room to the start room
current_room = 'Start Room'

#calls function game intro
game_intro()

#asks the user to hit enter to continue for readability
input('press enter to continue...')

print('You will move room to room and pick up items by typing the following: North, South, East, West, or Pick Up Item. Remember, controls are case sensitive!')

input('press enter to continue...')

#continues to loop through the following
while True:
        #calls function room_desc to print a description of the room
        room_desc(current_room)

        #if the current room is dr senagor's office, the game ends becasue it can only happen after the boss fight, or the lose case
        if current_room == "Dr. Senagore's Office":
                break

        #asks the user for input to move to another room or pick up item, and assigns that input to variable named move
        move = input('You are in the {}! What would you like to do? (North, South, East, West, or Pick Up Item):\n'.format(current_room))

        #if that checks if the player input for move was pick up item and calls the function to pick up the item in the current room
        if move == 'Pick Up Item':
                pickup_item(current_room)

        #else if that checks if the player input move was a valid move in the rooms dictionary
        elif move in rooms[current_room]:
                #sets current room to the valid room that was moved to
                current_room = rooms[current_room][move]
        #else that tells the player their move was not valid
        else:
                print("Sorry! You can't go there!")




