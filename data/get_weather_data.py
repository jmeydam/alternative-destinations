import requests
import random

# command to generate .csv file:
# python get_weather_data.py > weather_conditions.csv

api_key = '1a2b3c' # change
#DEBUG_COUNTER = 0
with open('./destinations.csv', encoding='utf-8') as destinations_file:
    print('"iata_code","month","min_temperature_celsius","max_temperature_celsius","daily_precipitation_mm"')
    for line in destinations_file:
        #DEBUG_COUNTER += 1
        #if DEBUG_COUNTER > 1:
        #    quit()
        # "city","country","iata_code","lat","long"
        # "Reykjavik","Iceland","RKV",64.13,-21.9406
        line = line.replace('"', '')
        fields = line.split(',')
        iata_code=fields[2]
        url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={iata_code}&date=2020-01-01&cc=no&mca=yes&format=json"
        r = requests.get(url)
        data = r.json()
        for i in range(12): 
            avgs = data['data']['ClimateAverages'][0]['month'][i]
            month = avgs['name']
            # randomize to get demo data
            min_temperature_celsius = str(round(float(avgs['avgMinTemp']) + random.random() - 0.5, 1))
            # field name suggests *absolute* max temperature, not average - looking at values, these may actually be averages
            max_temperature_celsius = str(round(float(avgs['absMaxTemp']) + random.random() - 0.5, 1))
            daily_precipitation_mm  = str(round(abs(float(avgs['avgDailyRainfall']) + random.random() - 0.5), 1)) 
            print(f'"{iata_code}","{month}","{min_temperature_celsius}","{max_temperature_celsius}","{daily_precipitation_mm}"')
