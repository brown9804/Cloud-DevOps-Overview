#!/usr/bin/env python3

from countryinfo.countryinfo import CountryInfo as CountryInfo
from tkinter import *
import requests
from bs4 import BeautifulSoup as BS 
import pandas as pd 
import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import date
from currency_converter import CurrencyConverter

###    Return info of search country
def country_info(country_name):
    country = CountryInfo(country_name)

    d = []
    d.append(["Country Name", country.name().capitalize()])
    d.append(["Other spelling for country name", country.alt_spellings()])
    d.append(["Capital", country.capital().capitalize()])
    d.append(["Provinces", country.provinces()])
    d.append(["Region", country.region().capitalize()])
    d.append(["Subregion", country.subregion().capitalize()])
    d.append(["Currency", country.currencies()])
    d.append(["Languages", country.languages()])
    d.append(["Borders", country.borders()])
    d.append(["Calling Code", country.calling_codes()])
    d.append(["Area", country.area()])
    d.append(["Population", country.population()])
    d.append(["Lat/Long", country.capital_latlng()])
    d.append(["Code", country.iso(2)])

    dataframe = pd.DataFrame(d, columns=["Information", "Values"])
    return dataframe

###    Read covid data
def covid_data(country_name):

    country_name = country_name.lower()
    if " " in country_name:
        country_name = country_name.replace(" ", "-")
    else:
        country_name = country_name

    url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
    data = requests.get(url) 
    soup = BS(data.text, 'html.parser')    # converting the text  
    cases = soup.find_all("div", class_ = "maincounter-number") # finding meta info for cases 
    total = cases[0].text # getting total cases number 
    total = total[1 : len(total) - 2] # filtering it 
    recovered = cases[2].text # getting recovered cases number 
    recovered = recovered[1 : len(recovered) - 1] # filtering it 
    deaths = cases[1].text # getting death cases number 
    deaths = deaths[1 : len(deaths) - 1]  # filtering it 
    ans ={'Total Cases' : total, 'Recovered Cases' : recovered, 'Total Deaths' : deaths} # saving details in dictionary 
    return ans 
   
###  Request capital weather 
async def capital_weather(latitude, longitude):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print(hourly_dataframe.head(5))
    return hourly_dataframe

### Convert from currency to X 
def convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked):
    c = CurrencyConverter(fallback_on_wrong_date=True)
    amount_converted = c.convert(int(amount), from_currency, to_currency, date=date(int(year_asked), 
                                                                                    int(month_asked), 
                                                                                    int(day_asked)))
    print(str(amount_converted) + " " + from_currency + " to " + to_currency + " is: " + str(amount_converted))
    print("At " + str(year_asked) + "/" + str(month_asked) + "/" + str(day_asked))
    return amount_converted

