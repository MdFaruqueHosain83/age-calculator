from datetime import date

print("=== Age Calculator ===")
print("Made by Md Faruque Hosain")

# Today's date
today = date.today()
print(f"\nToday's Date: {today}")

# User input
birth_year = int(input("\nEnter your Birth Year (ex: 2000): "))
birth_month = int(input("Enter your Birth Month (1-12): "))
birth_day = int(input("Enter your Birth Day (1-31): "))

birth_date = date(birth_year, birth_month, birth_day)

# Calculate age
age_years = today.year - birth_date.year
age_months = today.month - birth_date.month
age_days = today.day - birth_date.day

# Adjust if birthday not yet come this year
if age_months < 0 or (age_months == 0 and age_days < 0):
    age_years -= 1
    age_months += 12

if age_days < 0:
    age_months -= 1
    age_days += 30

# Total days lived
total_days = (today - birth_date).days

print(f"\n🎂 You are {age_years} Years, {age_months} Months, {age_days} Days old!")
print(f"📅 You have lived {total_days} days in total!")
