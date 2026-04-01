import locale

try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')  # fallback auf System


def format_currency(amount):
    """format currency as dollars"""
    return locale.currency(amount, grouping=True)


def validate_not_empty(value, field_name="Value"):
    """validate if value is empty"""
    if not value or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"{field_name} must not be empty")


def validate_non_negative(value, field_name="Value"):
    """validate if value is negative"""
    if value < 0:
        raise ValueError(f"{field_name} must be >= 0")


def validate_not_enough_in_stock(value, stock, field_name):
    if value > stock:
        raise ValueError(f"Not enough stock for {field_name}")
