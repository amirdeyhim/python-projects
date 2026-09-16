import logging

# ۱. تنظیمات لاگ
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

raw_file_path = "data/raw/orders_raw.csv"

try:
    # ۲. خواندن فایل خام
    with open(raw_file_path, "r") as file:
        lines = file.readlines()
        logging.info(f"File opened successfully. Total lines: {len(lines)}")

    # ۳. آماده‌سازی
    header = lines[0]
    data_rows = lines[1:]

    clean_orders = []
    error_orders = []

    # ۴. حلقه پردازش
    for row in data_rows:
        parts = row.strip().split(",")
        order_id = parts[0]
        user_id = parts[1]
        quantity_str = parts[2]
        price = parts[3]
        card_number = parts[4]

        # ۵. اعتبارسنجی
        try:
            quantity = int(quantity_str)

            if quantity <= 0:
                error_orders.append(f"{order_id},Invalid quantity: {quantity}")
                logging.warning(f"Order {order_id} rejected: quantity <= 0")
            else:
                masked_card = "*******" + card_number[-4:]
                clean_row = f"{order_id},{user_id},{quantity},{price},{masked_card}"
                clean_orders.append(clean_row)

        except ValueError:
            error_orders.append(f"{order_id},Invalid format: '{quantity_str}'")
            logging.warning(
                f"Order {order_id} rejected: non-numeric quantity '{quantity_str}'"
            )

    # ۶. نوشتن فایل تمیز
    clean_file_path = "data/processed/orders_clean.csv"
    with open(clean_file_path, "w") as clean_file:
        clean_file.write(header)
        for order in clean_orders:
            clean_file.write(order + "\n")

    logging.info(
        f"Clean orders written to {clean_file_path}. Total: {len(clean_orders)}"
    )

    # ۷. نوشتن فایل خطا
    error_file_path = "data/processed/orders_error.csv"
    with open(error_file_path, "w") as error_file:
        error_file.write("order_id,error_reason\n")
        for error in error_orders:
            error_file.write(error + "\n")

    logging.info(
        f"Error orders written to {error_file_path}. Total: {len(error_orders)}"
    )

    print("پردازش تمام شد. فایل‌های clean و error در پوشه processed ساخته شدند.")

except FileNotFoundError:
    logging.error(f"File not found: {raw_file_path}")
