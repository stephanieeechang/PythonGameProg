#The program helps the user decide what music he/she should listen at the moment

moving = input('Are you on the move while you work? (yes or no): ')
if moving == 'yes':
    howMove = input('On feet or on wheels? (feet or wheels): ')
    if howMove == 'feet':
        whatJob = input('Who are you? 1. In construction? 2. Athlete or a coach? 3. Bartender? (1, 2, or 3): ')
        if whatJob == 1:
            print('You need: CLASSIC ROCK or HEAVY METAL')
        elif whatJob == 2:
            print('You need: PUNK, HIP-HOP/RAP or ROCK')
        elif whatJob == 3:
            print('You need: CLASSIC ROCK, ROCK, REGGAE, JAZZ, COUNTRY, INDIE ROCK, OLDIES, POP or DUBSTEP')
    elif howMove == 'wheels':
        vehicle = input('Are you driving a motorized vehicle? (yes or no): ')
        if vehicle == 'yes':
            wheelsNum = input('How many wheels? (4 or 18): ')
            if wheelsNum == 4:
                print('You need: JAZZ, OLDIES, BAROQUE/CLASSICAL or POP')
            elif wheelsNum == 18:
                print('You need: DUBSTEP, PUNK, ROCK, TECHNO/TRANCE or HEAVY METAL')
        elif vehicle == 'no':
            print('Keep your ears tuned to the sounds of the road.')
elif moving == 'no':
    creative = input('Is your job creative? (yes or no): ')
    if creative == 'yes':
        print('You need: AMBIENT, JAZZ, BAROQUE/CLASSICAL or what ever floats your boat')
    elif creative == 'no':
        whatDo = input('What is your do? 1. Works with people all day 2. Chained to computer all day, just cranking away to get to the next payday (1 or 2): ')
        if whatDo == 1:
            setting = input('In what kind of setting? (retail or teacher): ')
            if setting == 'retail':
                store = input('What type of store do you work in? (record or department): ')
                if store == 'record':
                    print('You need: a special taste of yours---as long as no one else in the store has heard it before')
                elif store == 'department':
                     print('You need: JAZZ')
            elif setting == 'teacher':
                grade = input('What grade do you teach? (kindergarten, highschool, college): ')
                if grade == 'kindergarten':
                    print('You need: AMBIENT, COUNTRY or POLKA')
                elif grade == 'highschool':
                    print('You need: POP, DUBSTEP, or INDIE ROCK')
                elif grade == 'college':
                    print('You are teaching college because someone thinks your lectures re music for the soul. No music necessary here.')
        elif whatDo == 2:
            what = input('Who are you? 1. Working with numbers? 2. Programmer? (1 or 2): ')
            if what == 1:
                print('You need: JAZZ, POP, SMOOTH JAZZ, POLKA, BAROQUE/CLASSICAL, RAP/HIP-HOP, TECHNO/TRANCE or OLDIES')
            elif what == 2:
                print('JAZZ, ROCK, POP or TECHNO/TRANCE')
