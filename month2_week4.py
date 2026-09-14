# # # # Open file in write mode
# # # file = open("my_data.txt", "w")
# # # file.write("This is my first persistent data!")
# # # file.close()

# # # print("Data saved successfully.")

# # # # Open file in read mode
# # # file = open("my_data.txt", "r")
# # # content = file.read()
# # # file.close()

# # # print("File content:", content)


# # # ##################

# # # with open("user_info.txt", "w") as file:
# # #     file.write("my name is amir.")

# # # with open("user_info.txt", "r") as file:
# # #     content = file.read()
# # # print("file content:", content)

# # # ##################
# # # with open("user_info.txt", "a") as file:
# # #     file.write("\nI am learning Python.")

# # # with open("user_info.txt", "r") as file:
# # #     content = file.read()
# # # print("file content:", content)
# # # ##################

# # # with open("user_info.txt", "a") as file:
# # #     file.write("\nThis is my new exercise.")
# # # with open("user_info.txt", "r") as file:
# # #     content = file.read()
# # # print("file content:", content)

# # # ##################

# # # try:
# # #     # برنامه سعی می کند متن را بگیرد و به عدد تبدیل کند
# # #     user_input = input("Enter order quantity: ")
# # #     quantity = int(user_input)
# # #     print("Order confirmed for:", quantity)

# # # except ValueError:
# # #     # اگر کاربر متن نامعتبر (مثل حروف) وارد کند، این بخش اجرا می شود
# # #     print("Error: Please enter a valid numeric value.")
# # # ##################

# # # import logging

# # # # تنظیمات پایه: به پایتون می‌گوییم پیام‌ها را از سطح INFO به بالا ثبت کن
# # # logging.basicConfig(level=logging.INFO)

# # # # ثبت چند پیام تستی در سطوح مختلف
# # # logging.info("Application started.")
# # # logging.warning("User input was not standard.")
# # # logging.error("Failed to process transaction.")
# # # ##################

# # # import logging

# # # # تنظیمات: ذخیره مستقیم لاگ‌ها داخل فایلی به نام app.log
# # # logging.basicConfig(
# # #     filename="app.log",
# # #     filemode="a",
# # #     level=logging.INFO,
# # #     format="%(asctime)s - %(levelname)s - %(message)s",
# # # )

# # # # ثبت پیام‌ها
# # # logging.info("Application started successfully.")
# # # logging.warning("User entered a non-standard input.")
# # # logging.error("Database connection failed.")
# # import logging

# # # پیکربندی سیستم لاگ برای ذخیره در فایل
# # logging.basicConfig(
# #     filename="app.log",
# #     filemode="a",
# #     level=logging.INFO,
# #     format="%(asctime)s - %(levelname)s - %(message)s",
# # )

# # logging.info("Order system initialized.")

# # user_input = input("Enter product quantity: ")

# # try:
# #     quantity = int(user_input)
# #     total_price = quantity * 25

# #     print("Order confirmed. Total price:", total_price)
# #     logging.info("Order completed successfully.")

# # except ValueError:
# #     print("Invalid input! Please enter digits only.")
# #     logging.error("Failed order: User entered non-numeric input.")
# ##################################################


# import logging

# logging.basicConfig(
#     filename="app.log",
#     filemode="a",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

# # داده‌های ورودی فرضی
# user_id = 452
# phone_number = "09123456789"
# password = "superSecretPassword123"

# # تکنیک ماسک کردن شماره تلفن (فقط ۴ رقم آخر دیده شود)
# masked_phone = "*******" + phone_number[-4:]

# # ثبت امن در لاگ:
# # ۱. پسورد اصلاً آورده نمی‌شود
# # ۲. شماره تلفن ماسک شده است
# # ۳. از شناسه عددی (ID) استفاده شده است
# logging.info(f"User registered successfully. User ID: {user_id}, Phone: {masked_phone}")
#######################################################################################


import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

card_number = "09121234567"
cvv2 = "345"

masked_card_number = "*******" + card_number[-4:]

logging.info(f"card number: {masked_card_number}")
