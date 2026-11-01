distance = float(input("Enter distance in km: "))

if distance <= 1:
    fare = 20
elif distance <= 5:
    fare = distance * 6
elif distance <= 12:
    fare = distance * 5.5
elif distance <= 20:
    fare = distance * 5
else:
    print("Invalid distance")
    exit()

print("Total fare = ", fare, "rupees")
