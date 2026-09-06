# Calcuate Simple Interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time: "))

si = (p * r * t) / 100
total_amount = p + si

print("Simple Intrest:", si)
print("total amount:", total_amount)