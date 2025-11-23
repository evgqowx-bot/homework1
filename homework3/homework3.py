def is_strong_password(password: str) -> bool:
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)

    return len(password) >= 8 and has_digit and has_upper and has_lower


def has_duplicates(your_list: list[int | float | str | bool]) -> bool:
    return len(your_list) != len(set(your_list))


def is_warm(temp_celsius: float) -> bool:
    return temp_celsius > 20


if __name__ == "__main__":
    print(is_strong_password("Abc12345"))
    print(has_duplicates([1, 2, 3, 2]))
    print(is_warm(25))


