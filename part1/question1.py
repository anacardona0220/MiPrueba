################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
    """
    Get the current temperature of a given city.

    Args:
        city (str): The name of the city for which you want to obtain the temperature.

    Returns:
        int: The current temperature in degrees Celsius for the city. If the city is unknown, it returns "unknown city".

    Example:
        >>> get_city_temperature("Quito")
        22
    """
    if city == "Quito":
        return 22
    if city == "Sao Paulo":
        return 17
    if city == "San Francisco":
        return 16
    if city == "New York":
        return 14
    else:
        return "unknown city"

def get_city_weather(city):
    """
    Get the current weather condition of a given city.

    Args:
        city (str): The name of the city for which you want to obtain the weather condition.

    Returns:
        str: A string describing the current weather condition and temperature in the city.
        If the city is unknown, it returns "Unknown city".

    Example:
        >>> get_city_weather("Quito")
        '22 degrees and sunny'
    """
    sky_condition = None

    if city == "Sao Paulo":
        sky_condition = "cloudy"
    elif city == "New York":
        sky_condition = "rainy"
    elif city == "Quito":
        sky_condition = "sunny"
    else:
        return "Unknown city"

    temperature = get_city_temperature(city)

    return str(temperature) + " degrees and " + sky_condition
