def remove_spaces(string):
    string = string.strip().split()
    string = ''.join(string)
    return string

def is_palindrome(string):
    for i in range(len(string)//2):
        #print(string[i], string[len(string)-1-i]) 
        if string[i] != string[len(string)-1-i]:      
            return False
    return True
        
        
# input
your_string = input('Enter your string: ')
spaces = input("Take into account spaces: Y/N: ")

#solution
if spaces == "N":
    your_string = remove_spaces(your_string)
if is_palindrome(your_string):
    print('Your string is a palindrome')
else:
    print('Your string isn\'t a palindrome')
