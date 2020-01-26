temp = float(input("Enter temperature: "))
type = input("Enter the type")
Celsius=(temp-32) * 5/9
Farenheit=(temp * 9/5) + 32
if type == "Celsius":
    print(Farenheit, "Farenheit")
elif type == "Farenheit":
	print(Celsius, "Celsius")