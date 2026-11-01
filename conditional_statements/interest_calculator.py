# 4. Balance interset calculation
balance = float(input("Enter your balance: "))

if balance <= 3000:
    rate = 0
elif balance <= 15000:
    rate = 3
elif balance <= 45000:
    rate = 4
elif balance <= 100000:
    rate = 6
else:
    rate = 7

interest = (balance * rate) / 100
total_interest = (balance + interest)

print("Balance =", balance )
print("Interest Rate =", rate,"%")
print("Total balance =", total_interest)
