# Program to calculate interest using map()

balance = [1000, 2000, 3000, 4000, 5000]

months = int(input("Enter months period: "))

def interest(ball):
    return (ball * 3 / 100) * months

print("Balance:", balance)

m1 = map(interest, balance)

print("Interest:", list(m1))
