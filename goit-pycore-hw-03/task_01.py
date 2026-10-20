from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Повертає кількість днів між заданою датою та сьогоднішньою датою.
    """
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.now().date()

    return (today - target_date).days


date = input("Введіть дату у форматі YYYY-MM-DD: ")

try:
    days = get_days_from_today(date)
    print(f"Кількість днів: {days}")
except ValueError:
    print("Помилка: введіть дату у форматі YYYY-MM-DD.")