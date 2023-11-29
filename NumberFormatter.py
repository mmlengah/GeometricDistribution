import locale
import logging

class NumberFormatter:
    def __init__(self, locale_str='en_US'):
        try:
            locale.setlocale(locale.LC_ALL, locale_str)
            self.locale_str = locale_str
        except locale.Error:
            logging.error(f"Locale {locale_str} not supported. Falling back to default.")
            self.locale_str = 'en_US'

    def add_commas(self, number):
        try:
            return locale.format_string("%d", number, grouping=True, monetary=False)
        except (ValueError, locale.Error) as e:
            logging.error(f"Error formatting number: {e}")
            return str(number)

    def add_percentage(self, decimal_number, decimal_places=2):
        try:
            format_str = "{:." + str(decimal_places) + "f}%"
            return format_str.format(decimal_number * 100)
        except Exception as e:
            logging.error(f"Error converting to percentage: {e}")
            return str(decimal_number)
