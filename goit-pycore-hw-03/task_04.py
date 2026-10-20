from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Повертає список привітань на найближчі 7 днів."""
    today = datetime.now().date()   # Отримуємо сьогоднішню дату
    upcoming_birthdays = []

    for user in users:  # Проведемо конвертацію рядка з датою народження в об'єкт
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )   # Якщо день народження вже пройшов у цьому році, розглянемо на наступний рік

        days_until_birthday = (birthday_this_year - today).days # Перевіримо найближчі 7 днів

        if 0 <= days_until_birthday < 7:    # Перевіримо, чи день народження потрапив в інтервал 7 днів
            congratulation_date = birthday_this_year
            # Перенесемо дату привітання, якщо вона припадає на вихідний
            # Понеділок - 0, Неділя - 6
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # Неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })  # Додаємо результат у список

    return upcoming_birthdays

# --- Приклад використання ---
# Сьогодні 2024.10.21, тому результатом може бути:
users = [
    {"name": "John Doe", "birthday": "1985.10.26"}, # Понеділок, 26 жовтня , наступного тижня
    {"name": "Jane Smith", "birthday": "1990.10.24"}, # Субота, 24 жовтня -> переносимо на Понеділок, 26
    {"name": "Peter Pan", "birthday": "1992.10.25"},    # Неділя, 25 жовтня -> переносимо на Понеділок, 26
    {"name": "Alice Wonderland", "birthday": "1995.10.30"}, # П'ятниця, 30 жовтня -> вже за межами 7 днів
    {"name": "Sam Winchester", "birthday": "2000.10.21"}, # Сьогодні
    {"name": "Dean Winchester", "birthday": "1979.08.02"}, # Вже минув цього року, наступний через рік
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("-"*20)
print("Сьогодні:", datetime.now().date())
print("-"*60)
print("Список привітань на цьому тижні:")
for num in upcoming_birthdays:
        print(num)
print("-"*60)


# Реальний приклад використання:

"""
--------------------
Сьогодні: 2026-10-21
------------------------------------------------------------
Список привітань на цьому тижні:
{'name': 'John Doe', 'congratulation_date': '2026.10.26'}
{'name': 'Jane Smith', 'congratulation_date': '2026.10.26'}
{'name': 'Peter Pan', 'congratulation_date': '2026.10.26'}
{'name': 'Sam Winchester', 'congratulation_date': '2026.10.21'}
------------------------------------------------------------
"""