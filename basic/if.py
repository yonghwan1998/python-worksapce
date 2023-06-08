weather = input("Weather? ")

if weather == "rain" or weather == "snow":
    print("take umbrella")
elif weather == "dusk":
    print("take mask")
else:
    print("no preparing")

print("================================================")

temp = int(input("temp? "))
if temp >= 30:
    print("Hot")
elif temp >= 10 and temp < 30:
    print("Good")
elif 0 <= temp < 10:
    print("Cool")
else:
    print("Cold")
