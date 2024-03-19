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
        current_span = trace.get_current_span()
        current_span.add_event("Input0 - Asking for Country Name ...")
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
            current_span.add_event("Input1 - Asking for ToCurrency exchange ...")
            to_currency = input("Into which currency would you like to convert?\n") #  user input

            current_span.add_event("Input2 - Asking for Amount of Money for exchange ...")
            amount = input("How much money would you like to convert?\n") # user input

            current_span.add_event("Input3 - Asking for YEAR of exchange ...")
            year_asked = input("Considering which YEAR for the exchange?\n") # user input

            current_span.add_event("Input4 - Asking for MONTH of exchange ...")
            month_asked = input("Considering which MONTH for the exchange?\n") # user input 

            current_span.add_event("Input5 - Asking for DAY of exchange ...")
            day_asked = input("Considering which DAY for the exchange?\n") # user input 
            convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked)
