items = ["phone", "laptop", "mouse"]

print("First:", items[0])
print("Last:", items[-1])

items.append("tablet")

print("updated:", items)
print("count:", len(items))

top_items = items[0:2]
print("top:", top_items)

prices = [450, 120, 80, 300]

prices.sort()
print("Ascending:", prices)

prices.sort(reverse=True)
print("Descending:", prices)

roles = ["user", "editor", "admin"]

print("has admin:", "admin" in roles)
print("admin index:", roles.index("admin"))

order_statuses = ("pending", "paid", "cancelled")

print("First Status:", order_statuses[0])
print("Total Statuses:", len(order_statuses))

# لیست خام مشتریان که شامل ایمیل تکراری است
raw_emails = ["user1@test.com", "user2@test.com", "user1@test.com", "user3@test.com"]

# پاک‌سازی تکراری‌ها با Set
unique_emails = set(raw_emails)

print("Original Count:", len(raw_emails))
print("Cleaned Emails:", unique_emails)
print("Cleaned Count:", len(unique_emails))
