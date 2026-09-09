orders = [100, 0, 250, -10, 500]
total = 0

for price in orders:
    if price == 0:
        print("skip zero")
        continue
    if price < 0:
        print("Abnormal data")
        break
    total += price
print("total:", total)
