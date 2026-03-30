import locale

try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')  # fallback auf System


def format_currency(amount):
    """format currency as dollars"""
    return locale.currency(amount, grouping=True)