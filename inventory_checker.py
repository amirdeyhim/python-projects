import logging

logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
raw_file_path = "data/raw/inventory_raw.csv"

try:
    with open(raw_file_path, "r") as raw_file:
        lines = raw_file.readlines()
        header = lines[0]
        data_rows = lines[1:]

        clean_inventory = []
        error_inventory = []

        for row in data_rows:
            parts = row.strip().split(",")
            product_id = parts[0]
            product_name = parts[1]
            stock_str = parts[2]
            try:
                stock = int(stock_str)

                if stock < 0:
                    error_inventory.append(f"{product_id},Negative stock: {stock}")
                    logging.warning(f"Product {product_id} rejected: negative stock")
                else:
                    clean_row = f"{product_id},{product_name},{stock}"
                    clean_inventory.append(clean_row)

            except ValueError:
                error_inventory.append(f"{product_id},Invalid format: '{stock_str}'")
                logging.warning(
                    f"Product {product_id} rejected: non-numeric stock '{stock_str}'"
                )
    clean_file_path = "data/processed/inventory_clean.csv"
    with open(clean_file_path, "w") as clean_file:
        clean_file.write(header)
        for item in clean_inventory:
            clean_file.write(item + "\n")

    logging.info(f"Clean items written. Total: {len(clean_inventory)}")

    error_file_path = "data/processed/inventory_error.csv"
    with open(error_file_path, "w") as error_file:
        error_file.write("product_id,error_reason\n")  # تیتر فایل خطا
        for error in error_inventory:
            error_file.write(error + "\n")

    logging.info(f"Error items written. Total: {len(error_inventory)}")
    print("پردازش انبار با موفقیت تمام شد! فایل‌های خروجی ساخته شدند.")


except FileNotFoundError:
    logging.error(f"file not found: {raw_file_path}")
