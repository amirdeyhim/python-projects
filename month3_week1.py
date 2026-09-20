import pandas as pd

level = ["سشف", "low", "medium"]

products = ["product A", "product B", "product C"]

level_products = pd.Series(data=level, index=products)

print(level_products)
print(level_products["product A"])

#####################################################
import pandas as pd

viewer = [500, 600, 450]
days = ["sat", "sun", "mon"]
viewer_days = pd.Series(data=viewer, index=days)
print(viewer_days)
print(viewer_days["mon"])

#####################################################

import pandas as pd

sales_data = {
    "Product": ["Product A", "Product B", "Product C"],
    "Revenue": [1200, 800, 1500],
    "Status": ["High", "Low", "High"],
    "visitors": [5, 8, 7],
}
df = pd.DataFrame(data=sales_data)

print(df)

#####################################################

import pandas as pd

shopping_data = {
    "user_ID": [101, 102, 103],
    "category": ["electronics", "clothing", "book"],
    "cart_value": [4500, 1200, 300],
}
df = pd.DataFrame(data=shopping_data)
print(df)

####################################################

import pandas as pd

data = {
    "user_ID": [101, 102, 103],
    "category": ["electronics", "clothing", "book"],
    "cart_value": [4500, 1200, 300],
}
df = pd.DataFrame(data)

df.to_csv("user_carts.csv", index=False)

loaded_df = pd.read_csv("user_carts.csv")

print(loaded_df)

####################################################

import pandas as pd

data = {
    "user_ID": [1001, 1002, 1003],
    "rating": [4, 5, 2],
    "platform": ["web", "ios", "android"],
}
df = pd.DataFrame(data)

df.to_csv("user_feedbacks.csv", index=False)

loaded_df = pd.read_csv("user_feedbacks.csv")

print(loaded_df)

#####################################################

import pandas as pd

data = {
    "user_ID": [1001, 1002, 1003],
    "rating": [4, 5, 2],
    "platform": ["web", "ios", "android"],
}
df = pd.DataFrame(data)

df.to_excel(
    "feedbacks_report_v2.xlsx",
    sheet_name="User_Reviews",
    index=False,
    engine="openpyxl",
)

print("فایل اکسل با موفقیت ساخته شد. حالا برو و آن را در پوشه سیستم باز کن.")

#####################################################

import pandas as pd

data = {
    "Project": ["Risalto", "Metayar", "Payeh", "Nilmootti"],
    "Budget": [5000, 8000, 3000, 4500],
    "Status": ["Active", "Completed", "Active", "Paused"],
}
df = pd.DataFrame(data)

print("--- کل جدول ---")
print(df)

high_budget_condition = df["Budget"] > 4000

high_budget_projects = df[high_budget_condition]

print("\n--- پروژه‌های با بودجه بیشتر از 4000 ---")
print(high_budget_projects)

######################################################

import pandas as pd

data = {
    "Project": ["Risalto", "Metayar", "Payeh", "Nilmootti"],
    "Budget": [5000, 8000, 3000, 4500],
    "Status": ["Active", "Completed", "Active", "Paused"],
}
df = pd.DataFrame(data)

active_projects = df[df["Status"] == "Active"]

print(active_projects)
