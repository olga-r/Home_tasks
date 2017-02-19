
# input section
your_list = list(map(int, input('Enter your list: ').strip().split()))
#print(your_list)

# solution
while True:
    interchange = 0
    for i in range(len(your_list)-1):
        if your_list[i] > your_list[i+1]:
            your_list[i], your_list[i+1] = your_list[i+1], your_list[i]
            interchange += 1
    if interchange == 0:
        break
print('your new list: {}'.format(your_list))