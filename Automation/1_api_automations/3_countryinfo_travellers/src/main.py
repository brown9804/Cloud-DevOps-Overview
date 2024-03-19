#Python3

##--------------------------------------------------------------------
##                         Copyright (C) 2022
##                         Belinda Brown Ramírez 
##                         belindabrownr04@gmail.com
##--------------------------

from shared import *
import asyncio

if __name__ == '__main__':
    with tracer.start_as_current_span("Country_Information_For_Travellers") as parent:

        country_name = input("Which country would you like information about?\n")     #  user input

        with tracer.start_as_current_span("Country_General_Inf") as child:
            print("\n************ Country - General Information ***********************\n")
            df_info = country_info(country_name)
            print(df_info.to_string(index=False))

        with tracer.start_as_current_span("Country_CovidData") as child:
            print("\n************ Country - Covid Data ***********************\n")
            covid_data_inf = covid_data(country_name)
            print(covid_data_inf)

        with tracer.start_as_current_span("Country_WeatherInformation") as child:
            print("\n************ Country - Weather Information ***********************\n")
            country_capital = df_info["Values"][12]
            latitude = country_capital[0]
            longitude = country_capital[1]
            asyncio.run(capital_weather(latitude, longitude))

        with tracer.start_as_current_span("Country_CurrencyConvert") as child:
            print("\n************ Country - Currency Convert ***********************\n")
            from_currency = df_info["Values"][6][0] # country inf currency 
            to_currency = input("Into which currency would you like to convert?\n") #  user input
            amount = input("How much money would you like to convert?\n") # user input
            year_asked = input("Considerintg which YEAR for the exchange?\n") # user input
            month_asked = input("Considerintg which MONTH for the exchange?\n") # user input 
            day_asked = input("Considerintg which DAY for the exchange?\n") # user input 
            convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked)
