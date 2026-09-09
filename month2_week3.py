product = {"title": "laptop", "price": 900}

print("title:", product["title"])
print("price:", product["price"])

car = {"brand": "toyota", "color": "white"}
print("brand:", car["brand"])
print("color:", car["color"])

order = {
    "order_id": 1050,
    "payment": {
        "method": "credit",
        "status": "paid",
    },
}

print("Payment Status:", order["payment"]["status"])

customer = {
    "name": "raha",
    "contact": {
        "phone": "09121111111",
        "city": "tehran",
    },
}
print("phone:", customer["contact"]["phone"])

import json

# ۱. یک دیکشنری پایتونی
user_dict = {"name": "Raha", "role": "admin"}

# ۲. تبدیل دیکشنری به متن بین‌المللی JSON
user_json = json.dumps(user_dict)

print("Python Type:", type(user_dict))
print("JSON Type:", type(user_json))
print("JSON Text:", user_json)

import json

server_config = {
    "host": "localhost",
    "port": 8080,
}
config_json = json.dumps(server_config)
print(config_json)


def show_status():
    print("system is online")


show_status()


def show_error():
    print("connection failed")


show_error()


def show_price(amount):
    print("Price is:", amount)


show_price(1500)
show_price(2000)


def send_alert(message):
    print("alert:", message)


send_alert("low battery")


def notify_user(username):
    print("notification for:", username)


notify_user("raha")
notify_user("amir")


def calculate_tax(price):
    # فرض کن اینجا کلی قوانین پیچیده بیزینسی نوشته شده
    # ...
    return price * 0.1  # در نهایت خروجی را پرتاب می‌کنیم بیرون


# حالا می‌توانیم خروجی ماشین را بگیریم و با هم جمع کنیم!
laptop_tax = calculate_tax(1000)
phone_tax = calculate_tax(500)

total_bill_tax = laptop_tax + phone_tax
print("Total Tax is:", total_bill_tax)


def get_discount(price):
    return price * 0.2  # حالا خروجی به بیرون پرتاب می‌شود


my_discount = get_discount(100)

final_price = my_discount + 10
print("Final price is:", final_price)  # خروجی می‌دهد: 30.0


def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit


my_profit = calculate_profit(1000, 800)
print(my_profit)


def calculate_balance(income, expense):
    balance = income - expense
    return balance


my_balance = calculate_balance(5000, 2000)
print(my_balance)


def check_stock(inventory):
    if inventory > 0:
        return "available"
    else:
        return "out of stock"


print("check inventory:", check_stock(5))

