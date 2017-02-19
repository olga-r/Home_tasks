
# input section
plates = int(input('Enter number of plates: '))
cleanser = float(input('Enter amount of cleanser: '))
print('You have {} ml of cleanser and {} plates'.format(cleanser, plates))

# solution
while True:
    plates -= 1
    cleanser -= 0.5
    if plates >= 1 and cleanser >= 0.5:
        print('You\'ve washed one plate and still have {} ml of cleanser and {} plates'.format(cleanser, plates))
        print 
    elif plates == 0 and cleanser > 0:
        print('You\'ve washed all plates and still have {} ml of cleanser'.format(cleanser))
        break
    elif plates == 0 and cleanser == 0:
        print('You\'ve washed all plates and don\'t have any cleanser'.format(cleanser))
        break
    elif cleanser < 0.5:
        print('You\'ve washed one plate and now you have {} ml of cleanser and {} plates.\nYou don\'t have enough cleanser to wash plates'.format(cleanser, plates))
        break