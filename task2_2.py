
# input section
your_list = list(map(int, input('Enter your list: ').strip().split()))
#print(your_list)

# solution
for i in range(len(your_list)//2):
    your_list[i], your_list[len(your_list)-1-i] = your_list[len(your_list)-1-i], your_list[i]
print('your new list: {}'.format(your_list))