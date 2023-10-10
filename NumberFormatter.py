import locale

class NumberFormatter:
    def __init__(self, locale_str='en_US'):
        """
        Initialize a NumberFormatter object with a specified locale.

        :param locale_str: A string specifying the locale (default is 'en_US').
        """
        self.locale_str = locale_str

    def add_comma(self, number):
        """
        Format an integer with commas based on the specified locale.

        :param number: An integer to be formatted with commas.
        :return: The formatted number as a string.
        """
        try:
            # Set the locale to the specified value
            locale.setlocale(locale.LC_ALL, self.locale_str)
            # Format the number with commas using the locale
            formatted_number = locale.format_string("%d", number, grouping=True)
            return formatted_number
        except Exception as e:
            print(f"Error formatting number: {e}")
            # Return the original number as a string in case of an error
            return str(number)
    
    def convert_to_percentage(self, decimal_number, decimal_places=2):
        """
        Convert a decimal number to a percentage with a specified number of decimal places.

        :param decimal_number: A decimal number to be converted to a percentage.
        :param decimal_places: The number of decimal places to include in the percentage (default is 2).
        :return: The formatted percentage as a string.
        """
        try:
            # Multiply the decimal number by 100 to get a percentage
            percentage = decimal_number * 100
            # Create a format string with the desired number of decimal places
            format_str = "{:." + str(decimal_places) + "f}%"
            # Format the percentage using the format string
            return format_str.format(percentage)
        except Exception as e:
            print(f"Error converting to percentage: {e}")
            # Return the original decimal number as a string in case of an error
            return str(decimal_number)
