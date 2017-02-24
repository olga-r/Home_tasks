def quadrant(x, y):
    quadrant = None
    if x > 0:
        if y > 0:
            quadrant = '1',    
        elif y < 0:
            quadrant = '4', 
        else:
            quadrant = '1', '4'
    elif x < 0:
        if y > 0:
            quadrant = '2',    
        elif y < 0:
            quadrant = '3', 
        else:
            quadrant = '2', '3'
    else:
        if y > 0:
            quadrant = '1', '2'    
        elif y < 0:
            quadrant = '3', '4' 
        else:
            quadrant = '1', '2', '3', '4'
    quadrant = ', '.join(quadrant)
    return quadrant
  
# input
x, y = map(float, input('Enter coordinates x y: ').strip().split())

#solution
print('Your point is in quadrant(s): {}'.format(quadrant(x, y)))


