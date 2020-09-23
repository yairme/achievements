while True:
    day = input("What day is it: ")
    if day in ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sat', 'Sun']:
        break
if day == "Mo":
    print("you have to go to school, at 10 AM, catching the train at 8 AM.")
elif day == "Tu":
    print("You got online lessons, at 9 AM. Note: Don't play ARK.")
elif day == "We":
    print("you have to go to school, at 11 AM, catching the train at 9 AM.")
elif day == "Th":
    print("You have online lessons, at 9 AM. Note: Don't play ARK.")
elif day == "Fr":
    print("You have online lessons, at 9 AM. Note: Don't play ARK.")
elif day == "Sat":
    print("Bruh, you drunk.")
elif day == "Sun":
    print("Bruh, go home.")
    