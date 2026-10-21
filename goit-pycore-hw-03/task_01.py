from datetime import datetime


from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Повертає кількість днів між заданою датою та сьогоднішньою датою.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Помилка: введіть дату у форматі YYYY-MM-DD.")
        return None

    today = datetime.now().date()

    return (today - target_date).days


date = input("Введіть дату у форматі YYYY-MM-DD: ")

days = get_days_from_today(date)

if days is not None:
    print(f"Кількість днів: {days}")


# Реальний приклад використання:

# Приклад 1:
"""
Введіть дату у форматі YYYY-MM-DD: 2026-10-10
Кількість днів: 11
"""

# Приклад 2:
"""
Введіть дату у форматі YYYY-MM-DD: 2026-11-03
Кількість днів: -13
"""

