# ۱. متغیرهای عملکردی یک کمپین تبلیغاتی
conversion_rate = 4.2       # درصد نرخ تبدیل ثبت‌شده
total_spend = 250.0         # بودجه مصرف‌شده (دلار)
budget_limit = 200.0        # سقف بودجه مجاز
target_cvr = 3.0            # حداقل نرخ تبدیل هدف

# ۲. استفاده از and: موفقیت فقط وقتی حاصل می‌شود که هم تارگت زده شود و هم بودجه رعایت شود
is_campaign_successful = (conversion_rate >= target_cvr) and (total_spend <= budget_limit)

# ۳. استفاده از or: اگر حداقل یکی از مشکلات رخ دهد، کمپین نیازمند بررسی فوری است
needs_review = (conversion_rate < target_cvr) or (total_spend > budget_limit)

# ۴. استفاده از not: بررسی اینکه آیا کمپین از سقف بودجه خارج شده است یا خیر
is_over_budget = not (total_spend <= budget_limit)

# ۵. چاپ خروجی‌های تحلیلی
print(f"Is campaign performing successfully? {is_campaign_successful}")
print(f"Does campaign need emergency review? {needs_review}")
print(f"Is campaign spend over the allowed limit? {is_over_budget}")