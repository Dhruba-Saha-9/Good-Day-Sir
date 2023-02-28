import time
name=input("Enter your name : ")
timestamp = time.strftime("%H:%M:%S")
h=int(time.strftime("%H"))
print(timestamp)

if h >= 4 and h < 12:
    print ("Good Morning Sir", name)
elif h >= 12 and h < 16:
    print("Good Afternoon Sir", name)
elif h >= 16 and h < 21:
    print("Good Evening Sir", name)
else:
    print("Good Night Sir", name)



