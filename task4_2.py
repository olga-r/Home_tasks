#functions
def check_number(NUM, number):
    allowed_binary_symbols = "01"
    allowed_decimal_symbols = "0123456789"
    for char in number:
        if NUM == "BIN":
            if char not in allowed_binary_symbols:
                return False
        elif NUM == "DEC":
            if char not in allowed_decimal_symbols:
                return False
    return True  

def bin_to_dec(bin_number):
    dec_number = 0
    for n in range(len(bin_number)):
        dec_number += int(bin_number[len(bin_number)-1 - n])*(2**n)
    return dec_number

def dec_to_bin(dec_number):
    bin_number = ""
    while dec_number > 1:
        residue, dec_number = dec_number%2, dec_number//2
        bin_number = str(residue) + bin_number
    if dec_number == 1:
        bin_number = "1" + bin_number
    return bin_number    
    
# input and solution
num_sys = input('Enter numeral system of your number (BIN/DEC): ')

if num_sys == "BIN":
    your_number = input('Enter your BIN number: ')
    if not check_number(num_sys, your_number):
        print("Enter correct binary number")
    else:
        your_dec_number = bin_to_dec(your_number)
        print('your decimal number is: {}'.format(your_dec_number))
elif num_sys == "DEC":
    your_number = input('Enter your DEC number: ')
    if not check_number(num_sys, your_number):
        print("Enter correct decimal number")
    else:
        your_bin_number = dec_to_bin(int(your_number))
        print('your binary number is: {}'.format(your_bin_number))
else:
    print("Enter correct numeral system. Only BIN and DEC are allowed")
