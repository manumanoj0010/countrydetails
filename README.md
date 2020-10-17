# Country Details

A python package for retrieving data from all the countries in the world.

![](https://raw.githubusercontent.com/manumanoj0010/countrydetails/master/Readme_Images/cd.jpeg)

## Install

```python
pip install countrydetails
```

## Usage

There are 2 modules -
1. Retrieving data of all countries **(Module Countries)**
2. Retrieving data of a single country **(Module Country)**

### Modules and their functions

##### Module Countries

- [countries()](#countries)
- [phone_code()](#phone_code)
- [currencies()](#currencies) 
- [capitals()](#capitals)  
- [continents()](#continents)   
- [countries_in_continents()](#countries_in_continents)
- [regions()](#regions)
- [countries_in_region()](#countries_in_region) 
- [states()](#states) 

##### Module Country

- [info()](#info) 
- [name()](#name)  
- [states()](#states) 
- [cities()](#cities)  
- [states_and_cities()](#states_and_cities)  
- [iso()](#iso) 
- [alt_spelling()](#alt_spellings) 
- [area()](#area)  
- [borders()](#borders)  
- [capital()](#capital)  
- [calling_codes()](#calling_codes)  
- [independence()](#independence) 
- [currency()](#currency) 
- [capital_latlng()](#capital_latlng) 
- [demonym()](#demonym) 
- [flag()](#flag) 
- [languages()](#languages) 
- [latlang()](#latlng)  
- [native_name()](#native_name) 
- [population()](#population)  
- [timezones()](#timezones) 
- [tld()](#tld) 
- [translations()](#translations) 
- [continents()](#continent) 
- [temperature()](#temperature)  
- [government()](#government) 
- [expectancy()](#expectancy)  
- [dish()](#dish)  
- [symbol()](#symbol) 
- [desnity()](#density)  
- [region()](#region) 
- [religion()](#religion)  
- [total_states()](#total_states)  
- [total_cities()](#total_cities)  
- [wiki()](#wiki)  
- [gei_json()](#geo_json)  
- [all()](#all) 


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

```

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
# Returns the data present below in a dict
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
from Countrydetails import country

country = country.country_details('India')
print(country.capital()) 

```

```
New Delhi
```

### .calling_codes()
```python
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

## Created & Maintained By

### [Manumanoj](https://github.com/manumanoj0010)

A Passionate Python and Web Developer. Currently pursuing his carrer as a student.

<a href="https://www.linkedin.com/in/manumanoj0010/" target="_blank"><img src="https://github.com/aritraroy/social-icons/blob/master/linkedin-icon.png?raw=true" width="60"></a><a href="https://facebook.com/manumanoj0010" target="_blank"><img src="https://github.com/aritraroy/social-icons/blob/master/facebook-icon.png?raw=true" width="60"></a><a href="https://instagram.com/m.a.n.u.m.a.n.o.j" target="_blank"><img src="https://github.com/aritraroy/social-icons/blob/master/instagram-icon.png?raw=true" width="60"></a><a href="https://github.com/manumanoj0010" target="_blank"><img src="https://img.icons8.com/material-outlined/52/000000/github.png"></a><a href="http://manojmanu.me/"  target="_blank"><img src="https://img.icons8.com/metro/52/000000/domain.png"></a>

[![GitHub stars](https://img.shields.io/github/stars/manumanoj0010/countrydetails.svg?style=social&label=Star)](https://github.com/manumanoj0010/countrydetails) [![GitHub forks](https://img.shields.io/github/forks/manumanoj0010/countrydetails.svg?style=social&label=Fork)](https://github.com/manumanoj0010/countrydetails/fork) [![GitHub watchers](https://img.shields.io/github/watchers/manumanoj0010/countrydetails?style=social&label=Watch)](https://github.com/manumanoj0010/countrydetails) [![GitHub followers](https://img.shields.io/github/followers/manumanoj0010.svg?style=social&label=Follow)](https://github.com/manumanoj0010)

