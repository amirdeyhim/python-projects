try:
    visit = int(input("Visit: "))
    lead = int(input("Lead: "))
    cost = float(input("Cost: "))
    revenue = float(input("Revenue: "))
    order = int(input("Order: "))
    # ۱. بررسی مقادیر منفی
    if visit < 0 or lead < 0 or cost < 0 or revenue < 0 or order < 0:
         print("Error: Values cannot be negative.")

    # ۲. بررسی منطق بیزینس (لید نمی‌تواند بیشتر از بازدید باشد)
    elif lead > visit:
            print("Error: Lead cannot be greater than Visit.")

    # ۳. محاسبات با مدیریت تک‌به‌تک تقسیم بر صفر
    elif visit == 0 or lead == 0 or cost == 0 or order == 0:
        print("Error: Visit, Lead, Cost, and Order cannot be zero.")

    else:
        conversion_rate = (lead / visit) * 100
        cpa=(cost / lead)
        roas=(revenue / cost)
        aov=(revenue / order)

        print(f"conversion_rate: {conversion_rate:.2f}%")
        print(f"cpa: {cpa:.2f}")
        print(f"roas: {roas:.2f}")
        print(f"aov: {aov:.2f}")

except ValueError:
    print("Error: Please enter numbers only.")