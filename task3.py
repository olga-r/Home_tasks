# functions

        
def create_set_of_square_distances(x1, y1, x2, y2, x3, y3, distances):
    distances.add((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distances.add((x3 - x2) ** 2 + (y3 - y2) ** 2)
    distances.add((x1 - x3) ** 2 + (y1 - y3) ** 2)

def check_for_triangle(distances):
    if 0 in distances:
        return False   
    else:
        return True

def check_for_equilateral_triangle(distances):
    if len(distances) == 1:
        return True
    else:
        return False

def check_for_rightangled_triangle(distances):
    distances = sorted(list(distances),reverse=True)
    #print(distances)
    delta = (distances[0] - distances[1] - distances[2]) if (len(distances) == 3) else (distances[0] - 2 * distances[1])
    if delta == 0:
        return True
    else:
        return False

# input section
x1, y1, x2, y2, x3, y3 = map(int, input('Enter coordinates of triangle: x1, y1, x2, y2, x3, y3: ').strip().split())
triangle = None
square_distances = set()

# solution
create_set_of_square_distances(x1, y1, x2, y2, x3, y3, square_distances)
if not check_for_triangle(square_distances):
    triangle = "Your input doesn't correspond to triangle"
else:
    if check_for_equilateral_triangle(square_distances):
        triangle = "Your input corresponds to equilateral, but not to rightangled triangle"
    else:
        if not check_for_rightangled_triangle(square_distances):
            triangle = "Your input doesn't correspond to rightangled triangle"
        else:
            triangle = "Your input corresponds to rightangled triangle"
print(triangle)
