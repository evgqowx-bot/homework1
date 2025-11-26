def is_valid_email(value: str) -> bool:

    if not value or value.startswith('@') or value.endswith('@') \
       or value.startswith('.') or value.endswith('.'):
        return False

    parts = value.split('@')
    if len(parts) != 2:
        return False

    local, domain = parts
    if '.' not in domain:
        return False

    return True


def avg(values: list[float]) -> float:

    if not values:
        raise ValueError("List is empty")

    return sum(values) / len(values)


def uah_to_usd(amount: float, rate: float) -> float:

    if amount <= 0:
        raise ValueError("Amount must be > 0")

    if rate <= 0:
        raise ValueError("Rate must be > 0")

    return amount / rate
