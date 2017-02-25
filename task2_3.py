
def is_palindrome(string):
    string = string.strip().split()
    string = ''.join(string)
    for i in range(len(string)//2):
        #print(string[i], string[len(string)-1-i]) 
        if string[i] != string[len(string)-1-i]:      
            return False
    return True
        
        
# input
your_string = input('Enter your string: ')
capitals = input("Take into account capitals: Y/N: ")

#solution
if capitals == "N":
    your_string = your_string.lower()
if is_palindrome(your_string):
    print('Your string is a palindrome')
else:
    print('Your string isn\'t a palindrome')
