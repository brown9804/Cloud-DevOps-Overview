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
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

### Instrumentation with OpenTelemetry TRACES
## ref https://opentelemetry.io/docs/languages/python/instrumentation/
provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
# Sets the global default tracer provider
trace.set_tracer_provider(provider)
# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("country_info_app_global_tracer") 

### Instrumentation with OpenTelemetry METRICS
metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(metric_readers=[metric_reader])
# Sets the global default meter provider
metrics.set_meter_provider(provider)
# Creates a meter from the global meter provider
meter = metrics.get_meter("country_info_app_global_meterprovider")
# Creating and using synchronous instrument
work_counter = meter.create_counter(
    "work.counter", unit="1", description="Counts the amount of work done"
)

###    Return info of search country
def country_info(country_name):
    work_counter.add(1, {"work.type": "country_info"})
    with tracer.start_as_current_span("span_country_info") as span: # adding span for track 
        current_span = trace.get_current_span()
        country = CountryInfo(country_name)
        current_span.set_attribute("operation0", "Ok - Get information from CountryInfo")

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
        current_span.set_attribute("operation1", "Ok - Append country information to list")

        dataframe = pd.DataFrame(d, columns=["Information", "Values"])
        current_span.set_attribute("operation2", "Ok - Store information into dataframe")

        return dataframe

###    Read covid data
def covid_data(country_name):
    work_counter.add(1, {"work.type": "covid_data"})
    with tracer.start_as_current_span("span_covid_data") as span: # adding span for track 
        current_span = trace.get_current_span()
        country_name = country_name.lower()
        current_span.set_attribute("operation0", "Ok - Cast country name to lowerCase")

        if " " in country_name:
            country_name = country_name.replace(" ", "-")
            current_span.set_attribute("operation1", "Ok - Replace empty space for - ")
        else:
            country_name = country_name
            current_span.set_attribute("operation1", "Ok - No need to replace empty space for - ")

        url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"
        data = requests.get(url) 
        current_span.set_attribute("operation2", "Ok - get worldometers country's covid data")

        soup = BS(data.text, 'html.parser')    # converting the text  
        current_span.set_attribute("operation3", "Ok - converting the text")

        cases = soup.find_all("div", class_ = "maincounter-number") # finding meta info for cases 
        current_span.set_attribute("operation4", "Ok - finding meta info for cases")

        total = cases[0].text # getting total cases number 
        total = total[1 : len(total) - 2] # filtering it 
        current_span.set_attribute("operation5", "Ok - getting total cases number")

        recovered = cases[2].text # getting recovered cases number 
        recovered = recovered[1 : len(recovered) - 1] # filtering it 
        current_span.set_attribute("operation6", "Ok - getting recovered cases number")

        deaths = cases[1].text # getting death cases number 
        deaths = deaths[1 : len(deaths) - 1]  # filtering it 
        current_span.set_attribute("operation7", "Ok - getting deaths cases number")

        ans ={'Total Cases' : total, 'Recovered Cases' : recovered, 'Total Deaths' : deaths} # saving details in dictionary 
        current_span.set_attribute("operation8", "Ok - whole data in place")

        return ans 
   
###  Request capital weather 
async def capital_weather(latitude, longitude):
    work_counter.add(1, {"work.type": "capital_weather"})
    with tracer.start_as_current_span("span_capital_weather") as span: # adding span for track 
        current_span = trace.get_current_span()

        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)
        current_span.set_attribute("operation0", "Ok - Setup the Open-Meteo API client with cache and retry on error")

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m"
        }
        responses = openmeteo.weather_api(url, params=params)
        current_span.set_attribute("operation1", "Ok - Call Open-Meteo API")

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
        current_span.set_attribute("operation2", "Ok - Process first location. Add a for-loop for multiple locations or weather models")

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
        current_span.set_attribute("operation3", "Ok - Process hourly data")

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        print(hourly_dataframe.head(5))
        current_span.set_attribute("operation4", "Ok - Store data into Dataframe")

        return hourly_dataframe

### Convert from currency to X 
def convert_currency(from_currency, to_currency, amount, year_asked, month_asked, day_asked):
    work_counter.add(1, {"work.type": "convert_currency"})
    with tracer.start_as_current_span("span_convert_currency") as span: # adding span for track 
        current_span = trace.get_current_span()
        c = CurrencyConverter(fallback_on_wrong_date=True)
        current_span.set_attribute("operation0", "Ok - Call CurrencyConverter")

        amount_converted = c.convert(int(amount), from_currency, to_currency, date=date(int(year_asked), 
                                                                                        int(month_asked), 
                                                                                        int(day_asked)))
        print(str(amount_converted) + " " + from_currency + " to " + to_currency + " is: " + str(amount_converted))
        print("At " + str(year_asked) + "/" + str(month_asked) + "/" + str(day_asked))
        current_span.set_attribute("operation1", "Ok - Currency Exchanged")

        return amount_converted

