import re


def normalize_phone(phone_number: str) -> str:
    """Нормалізує український номер телефону до формату +380XXXXXXXXX."""
    phone_number = re.sub(r"\D", "", phone_number) #Видаляємо все, крім цифр

    if phone_number.startswith("380"):  # Перевіряємо, чи номер починається з "380"
        return "+" + phone_number

    return "+38" + phone_number


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(number) for number in raw_numbers]

print(f"Нормалізовані номери телефонів для SMS-розсилки:\n{sanitized_numbers}")