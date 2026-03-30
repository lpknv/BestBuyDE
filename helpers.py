import locale

locale.setlocale(locale.LC_ALL, 'en_US')


def format_currency(amount):
    """format currency as dollars"""
    return '${:,.2f}'.format(amount)