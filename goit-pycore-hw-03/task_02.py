import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Повертає відсортований список унікальних випадкових чисел."""
    if not (1 <= min <= max <= 1000):
        return []

    if not (1 <= quantity <= max - min + 1):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))

# Тест 1: Класична лотерея 6 із 49
lottery_numbers_1 = get_numbers_ticket(1, 49, 6)
# Тест 2: Спроба зламати (хочемо 10 чисел, а діапазон лише 1-5)
lottery_numbers_2 = get_numbers_ticket(1, 5, 10)
# Тест 3: Числа поза діапазоном
lottery_numbers_3 = get_numbers_ticket(1, 1001, 5)


print("-"*30)
print("Ваші лотерейні числа:", lottery_numbers_1)
print("-"*30)
print("Ваші лотерейні числа:", lottery_numbers_2)
print("-"*30)
print("Ваші лотерейні числа:", lottery_numbers_3)