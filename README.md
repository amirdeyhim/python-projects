# برنامه جامع ۲۴ ماهه توسعه مهارت

# Product KPI Calculator

پروژه نهایی ماه اول آموزش پایتون برای محاسبه و اعتبارسنجی شاخص‌های عملکرد محصول و مارکتینگ.

## شاخص‌های محاسبه‌شده (KPIs)

- **Conversion Rate (CR):** نرخ تبدیل لید به بازدید
- **Cost Per Acquisition (CPA):** هزینه جذب به ازای هر لید
- **Return on Ad Spend (ROAS):** نرخ بازگشت هزینه تبلیغات
- **Average Order Value (AOV):** میانگین ارزش هر سفارش

## اعتبارسنجی و مهار خطاها (Validation & Error Handling)

- جلوگیری از کرش برنامه هنگام وارد کردن متن به جای عدد با `try / except`
- جلوگیری از خطای تقسیم بر صفر (`ZeroDivisionError`)
- اعتبارسنجی مقادیر منفی
- بررسی منطقی قیف فروش (بررسی حالت `Lead > Visit`)

## نحوه اجرا

```bash
python kpi_calculator.py
```
