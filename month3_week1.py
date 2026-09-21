# # # # # # import pandas as pd

# # # # # # level = ["سشف", "low", "medium"]

# # # # # # products = ["product A", "product B", "product C"]

# # # # # # level_products = pd.Series(data=level, index=products)

# # # # # # print(level_products)
# # # # # # print(level_products["product A"])

# # # # # # #####################################################
# # # # # # import pandas as pd

# # # # # # viewer = [500, 600, 450]
# # # # # # days = ["sat", "sun", "mon"]
# # # # # # viewer_days = pd.Series(data=viewer, index=days)
# # # # # # print(viewer_days)
# # # # # # print(viewer_days["mon"])

# # # # # # #####################################################

# # # # # # import pandas as pd

# # # # # # sales_data = {
# # # # # #     "Product": ["Product A", "Product B", "Product C"],
# # # # # #     "Revenue": [1200, 800, 1500],
# # # # # #     "Status": ["High", "Low", "High"],
# # # # # #     "visitors": [5, 8, 7],
# # # # # # }
# # # # # # df = pd.DataFrame(data=sales_data)

# # # # # # print(df)

# # # # # # #####################################################

# # # # # # import pandas as pd

# # # # # # shopping_data = {
# # # # # #     "user_ID": [101, 102, 103],
# # # # # #     "category": ["electronics", "clothing", "book"],
# # # # # #     "cart_value": [4500, 1200, 300],
# # # # # # }
# # # # # # df = pd.DataFrame(data=shopping_data)
# # # # # # print(df)

# # # # # # ####################################################

# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     "user_ID": [101, 102, 103],
# # # # # #     "category": ["electronics", "clothing", "book"],
# # # # # #     "cart_value": [4500, 1200, 300],
# # # # # # }
# # # # # # df = pd.DataFrame(data)

# # # # # # df.to_csv("user_carts.csv", index=False)

# # # # # # loaded_df = pd.read_csv("user_carts.csv")

# # # # # # print(loaded_df)

# # # # # # ####################################################

# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     "user_ID": [1001, 1002, 1003],
# # # # # #     "rating": [4, 5, 2],
# # # # # #     "platform": ["web", "ios", "android"],
# # # # # # }
# # # # # # df = pd.DataFrame(data)

# # # # # # df.to_csv("user_feedbacks.csv", index=False)

# # # # # # loaded_df = pd.read_csv("user_feedbacks.csv")

# # # # # # print(loaded_df)

# # # # # # #####################################################

# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     "user_ID": [1001, 1002, 1003],
# # # # # #     "rating": [4, 5, 2],
# # # # # #     "platform": ["web", "ios", "android"],
# # # # # # }
# # # # # # df = pd.DataFrame(data)

# # # # # # df.to_excel(
# # # # # #     "feedbacks_report_v2.xlsx",
# # # # # #     sheet_name="User_Reviews",
# # # # # #     index=False,
# # # # # #     engine="openpyxl",
# # # # # # )

# # # # # # print("فایل اکسل با موفقیت ساخته شد. حالا برو و آن را در پوشه سیستم باز کن.")

# # # # # # #####################################################

# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     "Project": ["Risalto", "Metayar", "Payeh", "Nilmootti"],
# # # # # #     "Budget": [5000, 8000, 3000, 4500],
# # # # # #     "Status": ["Active", "Completed", "Active", "Paused"],
# # # # # # }
# # # # # # df = pd.DataFrame(data)

# # # # # # print("--- کل جدول ---")
# # # # # # print(df)

# # # # # # high_budget_condition = df["Budget"] > 4000

# # # # # # high_budget_projects = df[high_budget_condition]

# # # # # # print("\n--- پروژه‌های با بودجه بیشتر از 4000 ---")
# # # # # # print(high_budget_projects)

# # # # # # ######################################################

# # # # # # import pandas as pd

# # # # # # data = {
# # # # # #     "Project": ["Risalto", "Metayar", "Payeh", "Nilmootti"],
# # # # # #     "Budget": [5000, 8000, 3000, 4500],
# # # # # #     "Status": ["Active", "Completed", "Active", "Paused"],
# # # # # # }
# # # # # # df = pd.DataFrame(data)

# # # # # # active_projects = df[df["Status"] == "Active"]

# # # # # # print(active_projects)

# # # # # ################################################################

# # # # # import pandas as pd

# # # # # data = {
# # # # #     "Campaign": ["C1", "C2", "C3", "C4"],
# # # # #     "Spend": [1000, 500, 2500, 1500],
# # # # #     "Conversion": [20, 5, 50, 10],
# # # # # }
# # # # # df = pd.DataFrame(data)

# # # # # efficient_campaigns1 = df[(df["Conversion"] > 15) & (df["Spend"] < 2000)]
# # # # # efficient_campaigns2 = df[(df["Conversion"] > 15) | (df["Spend"] < 2000)]
# # # # # print(efficient_campaigns1)
# # # # # print(efficient_campaigns2)

# # # # # #################################################################

# # # # import pandas as pd

# # # # data = {
# # # #     "Campaign": ["C1", "C2", "C3", "C4"],
# # # #     "Spend": [1000, 500, 2500, 1500],
# # # #     "Conversion": [20, 5, 50, 10],
# # # # }
# # # # df = pd.DataFrame(data)

# # # # print("--- جدول اصلی ---")
# # # # print(df)

# # # # top_campaigns = df.sort_values(by="Conversion", ascending=False)

# # # # print("\n--- کمپین‌ها مرتب شده بر اساس بیشترین تبدیل ---")
# # # # print(top_campaigns)

# # # ######################################################################

# # # import pandas as pd

# # # data = {
# # #     "Campaign": ["C1", "C2", "C3", "C4"],
# # #     "Spend": [1000, 500, 2500, 1500],
# # #     "Conversion": [20, 5, 50, 10],
# # # }
# # # df = pd.DataFrame(data)

# # # print("--- جدول اصلی ---")
# # # print(df)

# # # top_campaigns = df.sort_values(by="Spend", ascending=True)

# # # print("\n--- کمپین‌ها مرتب شده بر اساس کمترین هزینه ---")
# # # print(top_campaigns)

# # # #####################################################################

# # import pandas as pd

# # data = {
# #     "user": ["U1", "U2", "U3", "U4"],
# #     "logins": [12, 5, 45, 20],
# #     "purchases": [1, 0, 8, 3]
# # }
# # df = pd.DataFrame(data)

# # top_purchases = df.sort_values(by="purchases", ascending=False)

# # print(top_purchases)

# # #######################################################################

# import pandas as pd

# data = {
#     "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Books"],
#     "sales": [500, 200, 600, 300, 150],
# }
# df = pd.DataFrame(data)

# print("--- کل داده‌ها ---")
# print(df)

# category_sales = df.groupby("category").sum()

# print("\n--- مجموع فروش هر دسته‌بندی ---")
# print(category_sales)

# # #######################################################################

# import pandas as pd

# data = {
#     "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Books"],
#     "sales": [500, 200, 600, 300, 150],
# }
# df = pd.DataFrame(data)

# print("--- کل داده‌ها ---")
# print(df)

# category_sales = df.groupby("category").mean()

# print("\n--- مجموع فروش هر دسته‌بندی ---")
# print(category_sales)

#######################################################################

import pandas as pd

data = {
    "city": ["Tehran", "Shiraz", "Tehran", "Shiraz"],
    "agent": ["Ali", "Reza", "Sara", "Neda"],
    "sales": [2000, 1500, 3000, 2500],
}
df = pd.DataFrame(data)

category_sales = df.groupby("city")["sales"].sum()
print(category_sales)
