from datetime import datetime

now = datetime.now().minute
color = "Red" if (now%5 in [3, 4]) else "Green"
#print(now)
print(color)