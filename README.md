# Country Details

A python package for retrieving data of all the countries in the world.

## Install

`pip install countrydetails`


## Usage

There are 2 modules -
1. Retrieving data of all countries **(Module Countries)**
2. Retrieving data of a single country **(Module Country)**

## Module Countries

> For the sake of simplicity, I will be showing less data in outputs here.

### .countries()
Returns the list of all available countries in the world

``` python
from Countrydetails import countries

data = countries.all_countries()
data.countries() 

```

``` python
['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas The',  'Vietnam', 'Virgin Islands (British)', 'Virgin Islands (US)', 'Wallis And Futuna Islands', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'] 

```

### .phone_code()
Returns phone codes of each country in a dictionary

``` python
from countrydetails import countries

country = countries.all_countries()
print(country.phone_code()) 

```

``` python
{'Afghanistan': '93', 'Aland Islands': '+358-18', 'Albania': '355', 'Algeria': '213', 'American Samoa': '+1-684', 'Andorra': '376', 'Angola': '244', 'Anguilla': '+1-264', 'Antarctica': '', 'Antigua And Barbuda': '+1-268', 'Argentina': '54', 'Armenia': '374', 'Aruba': '297', 'Australia': '61', 'Austria': '43', 'Azerbaijan': '994', 'Bahamas The': '+1-242', 'Bahrain': '973', 'Bangladesh': '880', 

````

### .currencies()
Returns currencies of each country in a dictionary

```python
from countrydetails import countries

country = countries.all_countries()
print(country.currencies()) 

```

```python
{'Afghanistan': 'AFN', 'Aland Islands': 'EUR', 'Albania': 'ALL', 'Algeria': 'DZD', 'American Samoa': 'USD', 'Andorra': 'EUR', 'Angola': 'AOA', 'Anguilla': 'XCD', 'Antarctica': '', 'Antigua And Barbuda': 'XCD', 'Argentina': 'ARS', 'Belgium': 'EUR', 'Belize': 'BZD', 'Benin': 'XOF', 'Bermuda': 'BMD', 'Bhutan': 'BTN', 'Bolivia': 'BOB', 'Bosnia and Herzegovina': 'BAM', 'Botswana': 'BWP',

```

### .capitals()
Returns captial cities of each country in a dictionary
```python
from countrydetails import countries

country = countries.all_countries()
print(country.capitals()) 
```
```python
{'Afghanistan': 'Kabul', 'Aland Islands': 'Mariehamn', 'Albania': 'Tirana', 'Algeria': 'Algiers', 'American Samoa': 'Pago Pago', 'Andorra': 'Andorra la Vella', 'Angola': 'Luanda', 'Anguilla': 'The Valley', 'Antarctica': '', 'Antigua And Barbuda': "St. John's",  'Bahamas The': 'Nassau', 'Bahrain': 'Manama', 'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Belize': 'Belmopan', 
```

### .continents()
Returns continents of each country
```python
from countrydetails import countries

country = countries.all_countries()
print(country.continents()) 
```

```
[{'country': 'Afghanistan', 'continent': 'Asia'}, {'country': 'Albania', 'continent': 'Europe'}, {'country': 'Algeria', 'continent': 'Africa'}, {'country': 'American Samoa', 'continent': 'Oceania'}, {'country': 'Andorra', 'continent': 'Europe'}, {'country': 'Angola', 'continent': 'Africa'}, {'country': 'Anguilla', 'continent': 'North America'},{'country': 'Antarctica', 'continent': 'Antarctica'}],

```

### .countries_in_continents()
Returns a list of countries present in a continent
```python
from countrydetails import countries

country = countries.all_countries()
print(country.countries_in_continents()) 
```

```python
{'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon',   'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
```

### .regions()
Returns countries with its region
```python
from countrydetails import countries

country = countries.all_countries()
print(country.regions()) 
```

```python
[{'country': 'Afghanistan', 'location': 'Southern and Central Asia'}, {'country': 'Albania', 'location': 'Southern Europe'}, {'country': 'Algeria', 'location': 'Northern Africa'}, {'country': 'American Samoa', 'location': 'Polynesia'}, {'country': 'Andorra', 'location': 'Southern Europe'}, {'country': 'Aruba', 'location': 'Caribbean'}, {'country': 'Australia', 'location': 'Australia and New Zealand'},  
```

### .countries_in_region()
Returns list of countries present in its region
```python
from countrydetails import countries

country = countries.all_countries()
print(country.countries_in_region()) 
```

```python
{'Antarctica': ['Antarctica', 'Heard Island and McDonald Islands', 'South Georgia and the South Sandwich Islands'], 'Eastern Europe': ['Belarus', 'Hungary', 'Moldova', 'Poland', 'Romania', 'Ukraine'], 'Southern Europe': ['Albania', 'Andorra',   'Italy', 'North Macedonia', 'Yugoslavia'], 'Western Europe': ['Austria', 'Belgium', 'France', 'Germany', 'Liechtenstein',  'Switzerland'], 'North America': ['Bermuda',  'United States'],
```

### .states()
Returns all the available states in the world with its state code 
```python
from countrydetails import countries

country = countries.all_countries()
print(country.states()) 
```
```python
{'id': 1836, 'name': 'Nenets Autonomous Okrug', 'state_code': 'NEN'}, {'id': 1857, 'name': 'Nizhny Novgorod Oblast', 'state_code': 'NIZ'}, {'id': 1834, 'name': 'Novgorod Oblast', 'state_code': 'NGR'}, {'id': 1888, 'name': 'Novosibirsk', 'state_code': 'NVS'}, {'id': 1846, 'name': 'Omsk Oblast', 'state_code': 'OMS'}, {'id': 1886, 'name': 'Orenburg Oblast', 'state_code': 'ORE'}, {'id': 1908, 'name': 'Oryol Oblast', 'state_code': 'ORL'}, {'id': 1909, 'name': 'Penza Oblast', 'state_code': 'PNZ'}, {'id': 1871, 'name': 'Perm Krai', 'state_code': 'PER'}, {'id': 1833, 'name': 'Primorsky Krai', 'state_code': 'PRI'}, {'id': 1863, 'name': 'Pskov Oblast', 'state_code': 'PSK'}, {'id': 1852, 'name': 'Republic of Adygea', 'state_code': 'AD'} 
```

## Module Country

### .info()

```python
from Countrydetails import country

country = country.country_details('India')  #you can give your desired country
print(country.info()) 
```
```
```

### .name()
Returns the name of the country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.name()) 

```

```
India
```


### .states()
Returns all available in a  states list
```python
from Countrydetails import country

country = country.country_details('India')
print(country.states()) 

```
```python
['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 
'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
```


### .cities()
Returns all available cities in a list
```python
from Countrydetails import country

country = country.country_details('India')
print(country.cities()) 

```

```python
# I am just displaying just a part of information here due to huge huge data
['Bamboo Flat', 'Nicobar', 'Port Blair', 'South Andaman', 'Addanki', 'Ādoni', 'Akasahebpet', 'Akivīdu', 'Akkarampalle', 'Amalāpuram', 'Amudālavalasa', 'Anakāpalle', 'Anantapur', 'Atmakūr', 'Attili', 'Avanigadda', 'Badvel', 'Banganapalle', 'Bāpatla', 'Betamcherla', 'Bhattiprolu', 'Bhīmavaram', 'Bhīmunipatnam', 'Bobbili', 'Challapalle', 'Chemmumiahpet', 'Chilakalūrupet', 'Chinnachowk', 'Chīpurupalle', 'Chīrāla', 'Chittoor',  'Diguvametta', 'East Godāvari', 'Elamanchili', 'Puttaparthi', 'Puttūr', 'Rājahmundry',  'Takdah', 'Taki', 'Tamluk', 'Tarakeswar', 'Titagarh', 'Tufanganj', 'Tulin', 'Uchalan', 'Ula', 'Uluberia', 'Uttar Dinajpur district', 'Uttarpara Kotrung']
```

### .states_and_cities()
Returns states and cities in a dict
```python
from Countrydetails import country

country = country.country_details('India')
print(country.states_and_cities()) 
```

```python
# I am just displaying just a part of information here due to huge huge data
[{'id': 142095, 'name': 'South 24 Parganas district', 'latitude': '22.16197000', 'longitude': '88.43170000'}, {'id': 142096, 'name': 'Srikhanda', 'latitude': '23.60000000', 'longitude': '88.08330000'}, {'id': 142097, 'name': 'Srirampur', 'latitude': '23.35000000', 'longitude': '88.12000000'}, {'id': 142098, 'name': 'Suri', 'latitude': '23.91666667', 'longitude': '87.53333333'}, {'id': 142099, 'name': 'Swarupnagar community development block', 'latitude': '22.83330000', 'longitude': '88.86670000'}, {'id': 142100, 'name': 'Takdah', 'latitude': '27.03330000', 'longitude': '88.36670000'}, ]}]
```


### .iso()
Returns ISO codes for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.iso()) 

```

```
{'alpha2': 'IN', 'alpha3': 'IND'}
```
### .alt_spellings()
```python
Returns alternate spellings for the name of a specified country
from Countrydetails import country

country = country.country_details('India')
print(country.alt_spellings()) 

```

```
['IN', 'Bhārat', 'Republic of India', 'Bharat Ganrajya']
```
### .area()
Returns area (km²) for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.area()) 

```

```
3287590
```
### .borders()
Returns bordering countries (ISO3) for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.borders()) 

```

```
['AFG', 'BGD', 'BTN', 'MMR', 'CHN', 'NPL', 'PAK', 'LKA']
```
### .capital()
Returns capital city for a specified country
```python
Returns international calling codes for a specified country
from Countrydetails import country

country = country.country_details('India')
print(country.capital()) 

```

```
New Delhi
```

### .calling_codes()
```python
Returns international calling codes for a specified country
from Countrydetails import country

country = country.country_details('India')
print(country.calling_codes()) 

```

```
 ["91"]
```
### .independence()
Returns independence year for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.independence()) 

```

```
1947
```
### .currency()
Returns official currency for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.currency()) 

```

```
['INR']
```
### .capital_latlng()
Returns capital city latitude and longitude for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.capital_latlng()) 

```

```
[28.614179, 77.202266]
```
### .demonym()
Returns the demonyms for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.demonym()) 

```

```
Indian
```
### .flag()
Returns SVG link of the official flag for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.flag()) 

```

```
Sorry there is no link for indain flag :(
```

### .languages()
Returns all spoken languages for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.languages()) 

```

```
['Asami', 'Bengali', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Odia', 'Punjabi', 'Tamil', 'Telugu', 'Urdu', 'Sanskrit', 'English', 'Konkani', 'Nepali', 'Bodo', 'Kashmiri', 'Maithili', 'Santali', 'Sindhi']
```
### .latlng()
Returns approx latitude and longitude for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.latlng()) 

```

```
 [20, 77]
```
### .native_name()
Returns the name of the country in its native tongue
```python
from Countrydetails import country

country = country.country_details('India')
print(country.native_name()) 

```

```
भारत
```
### .population()
Returns the population of the specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.population()) 

```

```
1263930000
```
### .timezones()
Returns the timezones of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.timezones()) 

```

```
['UTC+05:30']
```
### .tld()
Returns the domain extension of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.tld()) 

```

```
['.in']
```
### .translations()
Returns translations of a given country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.translations()) 

```

```
{'de': 'Indien', 'es': 'India', 'fr': 'Inde', 'ja': 'インド', 'it': 'India'}
```
### .continent()
Returns the continent of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.continent()) 

```

```
Asia
```
### .temperature()
Returns the average temperature for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.temperature()) 

```

```
23.65
```
### .government()
Returns the type of government for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.government()) 

```

```
Federal Republic
```
### .expectancy()
Returns the life expectancy of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.expectancy()) 

```

```
62.5
```
### .dish()
Returns the national dish of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.dish()) 

```

```
No officially announced national dish
```
### .symbol()
Returns the national symbol of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.symbol()) 

```

```
animal
```
### .density()
Returns the density of a specified country in sq km
```python
from Countrydetails import country

country = country.country_details('India')
print(country.density()) 

```

```
454.9380726
```
### .region()
Returns the region of a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.region()) 

```

```
Southern and Central Asia
```
### .religion()
Returns the religion of the specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.religion()) 

```

```
Hinduism
```
### .total_states()
Returns the total number of states for the specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.total_states()) 

```

```
37 #including union territories
```
### .total_cities()
Return total numnber of cities for the specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.total_cities()) 

```

```
3865
```
### .wiki()
Returns the Wikipedia page link for the specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.wiki()) 

```

```
http://en.wikipedia.org/wiki/india
```
### .all()
Returns the every available data of all the countries in the world
```python
from Countrydetails import country

country = country.country_details()
print(country.all()) 

```

```python
# I am not displaying the output here as the data is enormous. You can try it yourself :)
```

### .geo_json()
Returns geoJSON for a specified country
```python
from Countrydetails import country

country = country.country_details('India')
print(country.geo_json()) 

```

```
{
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "IND",
                "properties": {
                    "name": "India"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                77.837451,
                                35.49401
                            ],
                            [
                                78.912269,
                                34.321936
                            ],
                            [
                                78.811086,
                                33.506198
                            ],
                            [
                                79.208892,
                                32.994395
                            ],
                            [
                                79.176129,
                                32.48378
                            ],
                            [
                                78.458446,
                                32.618164
                            ],
                            [
                                78.738894,
                                31.515906
                            ],
                            [
                                79.721367,
                                30.882715
                            ],
                            [
                                81.111256,
                                30.183481
                            ],
                            [
                                80.476721,
                                29.729865
                            ],
                            [
                                80.088425,
                                28.79447
                            ],
                            [
                                81.057203,
                                28.416095
                            ],
                            [
                                81.999987,
                                27.925479
                            ],
                            [
                                83.304249,
                                27.364506
                            ],
                            [
                                84.675018,
                                27.234901
                            ],
                            [
                                85.251779,
                                26.726198
                            ],
                            [
                                86.024393,
                                26.630985
                            ],
                            [
                                87.227472,
                                26.397898
                            ],
                            [
                                88.060238,
                                26.414615
                            ],
                            [
                                88.174804,
                                26.810405
                            ],
                            [
                                88.043133,
                                27.445819
                            ],
                            [
                                88.120441,
                                27.876542
                            ],
                            [
                                88.730326,
                                28.086865
                            ],
                            [
                                88.814248,
                                27.299316
                            ],
                            [
                                88.835643,
                                27.098966
                            ],
                            [
                                89.744528,
                                26.719403
                            ],
                            [
                                90.373275,
                                26.875724
                            ],
                            [
                                91.217513,
                                26.808648
                            ],
                            [
                                92.033484,
                                26.83831
                            ],
                            [
                                92.103712,
                                27.452614
                            ],
                            [
                                91.696657,
                                27.771742
                            ],
                            [
                                92.503119,
                                27.896876
                            ],
                            [
                                93.413348,
                                28.640629
                            ],
                            [
                                94.56599,
                                29.277438
                            ],
                            [
                                95.404802,
                                29.031717
                            ],
                            [
                                96.117679,
                                29.452802
                            ],
                            [
                                96.586591,
                                28.83098
                            ],
                            [
                                96.248833,
                                28.411031
                            ],
                            [
                                97.327114,
                                28.261583
                            ],
                            [
                                97.402561,
                                27.882536
                            ],
                            [
                                97.051989,
                                27.699059
                            ],
                            [
                                97.133999,
                                27.083774
                            ],
                            [
                                96.419366,
                                27.264589
                            ],
                            [
                                95.124768,
                                26.573572
                            ],
                            [
                                95.155153,
                                26.001307
                            ],
                            [
                                94.603249,
                                25.162495
                            ],
                            [
                                94.552658,
                                24.675238
                            ],
                            [
                                94.106742,
                                23.850741
                            ],
                            [
                                93.325188,
                                24.078556
                            ],
                            [
                                93.286327,
                                23.043658
                            ],
                            [
                                93.060294,
                                22.703111
                            ],
                            [
                                93.166128,
                                22.27846
                            ],
                            [
                                92.672721,
                                22.041239
                            ],
                            [
                                92.146035,
                                23.627499
                            ],
                            [
                                91.869928,
                                23.624346
                            ],
                            [
                                91.706475,
                                22.985264
                            ],
                            [
                                91.158963,
                                23.503527
                            ],
                            [
                                91.46773,
                                24.072639
                            ],
                            [
                                91.915093,
                                24.130414
                            ],
                            [
                                92.376202,
                                24.976693
                            ],
                            [
                                91.799596,
                                25.147432
                            ],
                            [
                                90.872211,
                                25.132601
                            ],
                            [
                                89.920693,
                                25.26975
                            ],
                            [
                                89.832481,
                                25.965082
                            ],
                            [
                                89.355094,
                                26.014407
                            ],
                            [
                                88.563049,
                                26.446526
                            ],
                            [
                                88.209789,
                                25.768066
                            ],
                            [
                                88.931554,
                                25.238692
                            ],
                            [
                                88.306373,
                                24.866079
                            ],
                            [
                                88.084422,
                                24.501657
                            ],
                            [
                                88.69994,
                                24.233715
                            ],
                            [
                                88.52977,
                                23.631142
                            ],
                            [
                                88.876312,
                                22.879146
                            ],
                            [
                                89.031961,
                                22.055708
                            ],
                            [
                                88.888766,
                                21.690588
                            ],
                            [
                                88.208497,
                                21.703172
                            ],
                            [
                                86.975704,
                                21.495562
                            ],
                            [
                                87.033169,
                                20.743308
                            ],
                            [
                                86.499351,
                                20.151638
                            ],
                            [
                                85.060266,
                                19.478579
                            ],
                            [
                                83.941006,
                                18.30201
                            ],
                            [
                                83.189217,
                                17.671221
                            ],
                            [
                                82.192792,
                                17.016636
                            ],
                            [
                                82.191242,
                                16.556664
                            ],
                            [
                                81.692719,
                                16.310219
                            ],
                            [
                                80.791999,
                                15.951972
                            ],
                            [
                                80.324896,
                                15.899185
                            ],
                            [
                                80.025069,
                                15.136415
                            ],
                            [
                                80.233274,
                                13.835771
                            ],
                            [
                                80.286294,
                                13.006261
                            ],
                            [
                                79.862547,
                                12.056215
                            ],
                            [
                                79.857999,
                                10.357275
                            ],
                            [
                                79.340512,
                                10.308854
                            ],
                            [
                                78.885345,
                                9.546136
                            ],
                            [
                                79.18972,
                                9.216544
                            ],
                            [
                                78.277941,
                                8.933047
                            ],
                            [
                                77.941165,
                                8.252959
                            ],
                            [
                                77.539898,
                                7.965535
                            ],
                            [
                                76.592979,
                                8.899276
                            ],
                            [
                                76.130061,
                                10.29963
                            ],
                            [
                                75.746467,
                                11.308251
                            ],
                            [
                                75.396101,
                                11.781245
                            ],
                            [
                                74.864816,
                                12.741936
                            ],
                            [
                                74.616717,
                                13.992583
                            ],
                            [
                                74.443859,
                                14.617222
                            ],
                            [
                                73.534199,
                                15.990652
                            ],
                            [
                                73.119909,
                                17.92857
                            ],
                            [
                                72.820909,
                                19.208234
                            ],
                            [
                                72.824475,
                                20.419503
                            ],
                            [
                                72.630533,
                                21.356009
                            ],
                            [
                                71.175273,
                                20.757441
                            ],
                            [
                                70.470459,
                                20.877331
                            ],
                            [
                                69.16413,
                                22.089298
                            ],
                            [
                                69.644928,
                                22.450775
                            ],
                            [
                                69.349597,
                                22.84318
                            ],
                            [
                                68.176645,
                                23.691965
                            ],
                            [
                                68.842599,
                                24.359134
                            ],
                            [
                                71.04324,
                                24.356524
                            ],
                            [
                                70.844699,
                                25.215102
                            ],
                            [
                                70.282873,
                                25.722229
                            ],
                            [
                                70.168927,
                                26.491872
                            ],
                            [
                                69.514393,
                                26.940966
                            ],
                            [
                                70.616496,
                                27.989196
                            ],
                            [
                                71.777666,
                                27.91318
                            ],
                            [
                                72.823752,
                                28.961592
                            ],
                            [
                                73.450638,
                                29.976413
                            ],
                            [
                                74.42138,
                                30.979815
                            ],
                            [
                                74.405929,
                                31.692639
                            ],
                            [
                                75.258642,
                                32.271105
                            ],
                            [
                                74.451559,
                                32.7649
                            ],
                            [
                                74.104294,
                                33.441473
                            ],
                            [
                                73.749948,
                                34.317699
                            ],
                            [
                                74.240203,
                                34.748887
                            ],
                            [
                                75.757061,
                                34.504923
                            ],
                            [
                                76.871722,
                                34.653544
                            ],
                            [
                                77.837451,
                                35.49401
                            ]
                        ]
                    ]
                }
            }
        ]
    },
```
