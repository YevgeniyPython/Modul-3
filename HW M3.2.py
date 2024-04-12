import random

def get_numbers_ticket(min, max, quantity):
    try:
        numbers = sorted(list(random.sample(range(min, max+1), quantity)))
        return numbers
    except ValueError:
        return "Sample larger than population or is negative"


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Winning numbers:", lottery_numbers)