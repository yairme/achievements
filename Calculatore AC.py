def add(x, y):
	return x + y
def subtract(x,y):
	return x - y
def multiply(x, y):
	return x * y
def divide(x, y):
	return x / y

print("selecteer operatie")
print("1.Plus")
print("2.Aftrekken")
print("3.Keren")
print("4.Deelen")

while True:
	choice = input("Enter keuze(1/2/3/4):")
	
	if choice in ('1', '2', '3', '4'):
		num1 = float(input("Voer eerste nummer in: "))
		num2 = float(input("Voer tweede nummer in: "))
		
		if choice == '1':
			print(num1, "+", num2, "=", add(num1, num2))
		elif choice == '2':
			print(num1, "-", num2, "=", subtract(num1, num2))
		elif choice == '3':
			print(num1, "X", num2, "=", multiply(num1, num2))
		elif choice == '4':
			print(num1, "/", num2, "=", divide(num1, num2))
		break
	else:
		print("Ongeldige invoer")