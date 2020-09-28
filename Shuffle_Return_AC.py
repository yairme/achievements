
def Dialog(x):
   return 5 * x

print(Dialog(7))
print(Dialog(10))
print(Dialog(12))

def greet(name, msg):
    print(f"Hello {name} , {msg}" )
greet("Yair", "Good morning!!")

def Line(name, msg="Good morning."):
    print(f"Hello {name} , {msg}" )
Line("Yair")
Line("Mikey", "How's it going?")

def List(*names):
    for name in names:
        print("Hello", name)
List("Yair","Anthony","Arno","Logan","Gino","Lily")