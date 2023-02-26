import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
if int(time.strftime("%H")) >= 21 and int(time.strftime("%H")) < 4:
    print("Good Night Sir")
elif int(time.strftime("%H")) >= 4 and int(time.strftime("%H")) < 12:
    print ("Good Morning Sir")
elif int(time.strftime("%H")) >= 12 and int(time.strftime("%H")) < 16:
    print ("Good Afternoon Sir")
else:
    print ("Good Evening Sir")
