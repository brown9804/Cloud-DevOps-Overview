from .src.shared import *

country_name = "Spain"
latitude = "40.416705"
longitude = "-3.703582"
from_currency = "EUR"
to_currency = "USD"
amount = "100"
year_asked = "2024"
month_asked = "3"
day_asked = "19"

def country_info_test(country_name):
    if country_name != " ":
        dataframe = country_info(country_name)
        country_info_result = "Completed"
    else:
        country_info_result = "Dismiss"
    return country_info_result

def covid_data_test(country_name):
    if country_name != " ":
        ans = covid_data(country_name)
        covid_data_result = "Completed"
    else:
        covid_data_result = "Dismiss"
    return covid_data_result

def capital_weather_test(latitude, longitude):
    if (latitude and longitude) != " ":
        capital_weather(latitude, longitude)
        weather_result = "Completed"
    else:
        weather_result = "Dismiss"
    return weather_result


def convert_currency_test(from_currency, to_currency, amount, year_asked, month_asked, day_asked):
    if (from_currency and to_currency and amount and year_asked and month_asked and day_asked) != " ":
        amount_converted = convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked)
        currency_convert_result = "Completed"
    else:
        currency_convert_result = "Dismiss"
    return currency_convert_result

def test0():
    assert country_info_test(country_name) == "Completed"

def test1():
    assert capital_weather_test(latitude, longitude) == "Completed"

def test2():
    convert_currency_test(from_currency, to_currency, amount, year_asked, month_asked, day_asked) == "Completed"

def test3():
    convert_currency_test(from_currency, to_currency, amount, year_asked, month_asked, day_asked) == "Completed"
