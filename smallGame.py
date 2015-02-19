from sys import exit

def first_room():
    print 'This is the first room.'
    print 'Here you found a chair,table, and a door.'
    print 'What do you want to do?'
    user_input = raw_input('> ')

    if 'table' in user_input:
        table()
    elif 'chair' in user_input:
        chair()
    elif 'door' in user_input:
        next_door()
    else:
        print 'I didn\'t understand what you said, could you repeat plz?'
        first_room()


def table():
    print 'You approached the table.'
    print 'Look, there\'s a book on the table!'
    print 'What do you whant to do?'
    user_input = raw_input('> ')

    if 'read' in user_input:
        book()
    else:
        print 'What was that sound?'
        print 'A monster killed you while you were thinking '
        dead('A monster killed you while you were thinking ')

def book():
    print 'You read the book.'
    print 'It was interesting.'
    print 'What do you want to do now?'
    user_input = raw_input('> ')

    if 'again' in user_input:
        book()
    elif 'back' in user_input:
        first_room()

def next_door():
    print 'You entered a new room.'
    print 'Muhammed Ali is in the room'
    print 'What do you want to do?'
    user_input = raw_input('> ')

    if 'fight' in user_input:
        print 'You can\'t win M.A.'
        dead('You tried to fight M.A.')
    else:
        print 'What did you say?'
        next_door()

def chair():
    print 'You sit in the chair.'
    print 'It is comfortable.'
    dead('There was a monster behind the chair.')

def dead(why):
    print why, 'Good Job'
    exit(0)

first_room()


