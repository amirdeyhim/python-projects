# محاسبه نرخ بازگشت سرمایه تبلیغات (ROAS)
total_revenue = 40000000
spend = 0
try:
    roas = total_revenue / spend
    if roas >= 4:
        print("عالی")
    else:
        print("ضعیف")
except ZeroDivisionError:
     print("spend cant be zero")