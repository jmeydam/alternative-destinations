import requests

api_key = '1a2b3c' # change
iata_code = 'LHR'
url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={iata_code}&date=2020-01-01&cc=no&mca=yes&format=json"
r = requests.get(url)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print('--------------------- JSON -------------------------------')
print(r.text)
print('--------------------- JSON -> Python ---------------------')
print(r.json())

# formatted output:
#
# {
#   'data': 
#   {
#     'request': 
#     [{
#       'type': 'IATA', 
#       'query': 'LHR, London Heathrow Airport, United Kingdom'
#     }], 
#     'ClimateAverages': 
#     [{
#       'month': 
#       [
#         {'index': '1', 'name': 'January', 'avgMinTemp': '2.9', 'avgMinTemp_F': '36.9', 'absMaxTemp': '8.964516', 'absMaxTemp_F': '47.9', 'avgDailyRainfall': '2.90'}, 
#         {'index': '2', 'name': 'February', 'avgMinTemp': '2.9', 'avgMinTemp_F': '36.9', 'absMaxTemp': '9.921428', 'absMaxTemp_F': '49.9', 'avgDailyRainfall': '2.98'}, 
#         {'index': '3', 'name': 'March', 'avgMinTemp': '3.9', 'avgMinTemp_F': '38.9', 'absMaxTemp': '14.99677', 'absMaxTemp_F': '58.9', 'avgDailyRainfall': '1.90'}, 
#         {'index': '4', 'name': 'April', 'avgMinTemp': '6.9', 'avgMinTemp_F': '42.9', 'absMaxTemp': '18.96667', 'absMaxTemp_F': '65.9', 'avgDailyRainfall': '1.93'}, 
#         {'index': '5', 'name': 'May', 'avgMinTemp': '9.9', 'avgMinTemp_F': '49.9', 'absMaxTemp': '21.93226', 'absMaxTemp_F': '69.9', 'avgDailyRainfall': '2.94'}, 
#         {'index': '6', 'name': 'June', 'avgMinTemp': '12.9', 'avgMinTemp_F': '55.9', 'absMaxTemp': '23.99667', 'absMaxTemp_F': '74.9', 'avgDailyRainfall': '2.94'}, 
#         {'index': '7', 'name': 'July', 'avgMinTemp': '14.9', 'avgMinTemp_F': '58.9', 'absMaxTemp': '27.93548', 'absMaxTemp_F': '80.9', 'avgDailyRainfall': '2.93'}, 
#         {'index': '8', 'name': 'August', 'avgMinTemp': '13.9', 'avgMinTemp_F': '57.9', 'absMaxTemp': '24.92581', 'absMaxTemp_F': '76.9', 'avgDailyRainfall': '2.93'}, 
#         {'index': '9', 'name': 'September', 'avgMinTemp': '11.9', 'avgMinTemp_F': '52.9', 'absMaxTemp': '22.92333', 'absMaxTemp_F': '73.9', 'avgDailyRainfall': '1.93'}, 
#         {'index': '10', 'name': 'October', 'avgMinTemp': '9.9', 'avgMinTemp_F': '49.9', 'absMaxTemp': '17.94193', 'absMaxTemp_F': '63.9', 'avgDailyRainfall': '1.95'}, 
#         {'index': '11', 'name': 'November', 'avgMinTemp': '6.9', 'avgMinTemp_F': '43.9', 'absMaxTemp': '12.93333', 'absMaxTemp_F': '55.9', 'avgDailyRainfall': '2.92'}, 
#         {'index': '12', 'name': 'December', 'avgMinTemp': '3.9', 'avgMinTemp_F': '38.9', 'absMaxTemp': '12.96129', 'absMaxTemp_F': '53.9', 'avgDailyRainfall': '2.96'}
#       ]
#     }]
#   }
# }

data = r.json()
print(data['data']['ClimateAverages'][0]['month'][0])

avgs = data['data']['ClimateAverages'][0]['month'][0]
print(avgs)
# {'index': '1', 'name': 'January', 'avgMinTemp': '2.9', 'avgMinTemp_F': '36.9', 'absMaxTemp': '8.964516', 'absMaxTemp_F': '47.9', 'avgDailyRainfall': '2.90'}

# alternative destinations url parameters:
# - iata_code=LHR
# - date=2019-01-31
# - min_temperature_celsius=5
# - max_temperature_celsius=20
# - max_precipitation_mm=0
# - max_cloud_cover_percent=20 # deprecate

month = avgs['name']
avg_min_temperature_celsius = avgs['avgMinTemp']
avg_max_temperature_celsius = avgs['absMaxTemp'] # *absolute*, not average
avg_daily_precipitation_mm  = avgs['avgDailyRainfall']

print(iata_code)
print(month)
print(avg_min_temperature_celsius)
print(avg_max_temperature_celsius)
print(avg_daily_precipitation_mm)

# LHR
# January
# 2.9
# 8.964516
# 2.90

