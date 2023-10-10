import locale

class NumberFormatter:
    def __init__(self, locale_str='en_US'):
        self.locale_str = locale_str

    def add_comma(self, number):
        try:
            locale.setlocale(locale.LC_ALL, self.locale_str)
            formatted_number = locale.format_string("%d", number, grouping=True)
            return formatted_number
        except Exception as e:
            print(f"Error formatting number: {e}")
            return str(number)
    
    def convert_to_percentage(self, decimal_number, decimal_places=2):
        try:
            percentage = decimal_number * 100
            format_str = "{:." + str(decimal_places) + "f}%"
            return format_str.format(percentage)
        except Exception as e:
            print(f"Error converting to percentage: {e}")
            return str(decimal_number)
