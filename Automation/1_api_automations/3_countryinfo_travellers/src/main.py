#Python3

##--------------------------------------------------------------------
##                         Copyright (C) 2022
##                         Belinda Brown Ramírez 
##                         belindabrownr04@gmail.com
##--------------------------

from shared import *
import asyncio

if __name__ == '__main__':
    country_name = input("Which country would you like information about?\n")     #  user input

    print("\n************ Country - General Information ***********************\n")
    df_info = country_info(country_name)
    print(df_info.to_string(index=False))
    print("\n************ Country - Covid Data ***********************\n")
    covid_data_inf = covid_data(country_name)
    print(covid_data_inf)
    print("\n************ Country - Weather Information ***********************\n")
    country_capital = df_info["Values"][12]
    latitude = country_capital[0]
    longitude = country_capital[1]
    asyncio.run(capital_weather(latitude, longitude))
    print("\n************ Country - Currency Convert ***********************\n")
    from_currency = df_info["Values"][6][0]
    to_currency = input("Into which currency would you like to convert?\n") #  user input
    amount = input("How much money would you like to convert?\n") # user input
    year_asked = input("Considerintg which YEAR for the exchange?\n") # user input
    month_asked = input("Considerintg which MONTH for the exchange?\n") # user input 
    day_asked = input("Considerintg which DAY for the exchange?\n") # user input 
    convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked)
