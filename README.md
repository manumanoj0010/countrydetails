# Country Details

A python package for retrieving data of all the countries in the world.

## Install

`pip install countrydetails`


## Usage

------------



There are 2 modules present -
1. Retrieving data of all countries **(Module Countries)**
2. Retrieving data of a single country **(Module Country)**

## Module Countries

### .countries()
Returns the list of available countries in the world

``` python
from countrydetails import countries

data = countries.all_countries()
data.countries() 

```

``` python
['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo The Democratic Republic Of The', 'Cook Islands', 'Costa Rica', "Cote D'Ivoire (Ivory Coast)", 'Croatia (Hrvatska)', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji Islands', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey and Alderney', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard and McDonald Islands', 'Honduras', 'Hong Kong S.A.R.', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau S.A.R.', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Man (Isle of)', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands Antilles', 'Netherlands The', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory Occupied', 'Panama', 'Papua new Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Island', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent And The Grenadines', 'Saint-Barthelemy', 'Saint-Martin (French part)', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard And Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State (Holy See)', 'Venezuela', 'Vietnam', 'Virgin Islands (British)', 'Virgin Islands (US)', 'Wallis And Futuna Islands', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'] 

```

### .phone_code()
Returns phone codes of all countries in a dictionary

``` python
from countrydetails import countries

country = countries.all_countries()
print(country.phone_code()) 

```

``` python
{'Afghanistan': '93', 'Aland Islands': '+358-18', 'Albania': '355', 'Algeria': '213', 'American Samoa': '+1-684', 'Andorra': '376', 'Angola': '244', 'Anguilla': '+1-264', 'Antarctica': '', 'Antigua And Barbuda': '+1-268', 'Argentina': '54', 'Armenia': '374', 'Aruba': '297', 'Australia': '61', 'Austria': '43', 'Azerbaijan': '994', 'Bahamas The': '+1-242', 'Bahrain': '973', 'Bangladesh': '880', 

````

### .currencies()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.currencies()) 

```

```python
{'Afghanistan': 'AFN', 'Aland Islands': 'EUR', 'Albania': 'ALL', 'Algeria': 'DZD', 'American Samoa': 'USD', 'Andorra': 'EUR', 'Angola': 'AOA', 'Anguilla': 'XCD', 'Antarctica': '', 'Antigua And Barbuda': 'XCD', 'Argentina': 'ARS', 'Armenia': 'AMD', 'Aruba': 'AWG', 'Australia': 'AUD', 'Austria': 'EUR', 'Azerbaijan': 'AZN', 'Bahamas The': 'BSD', 'Bahrain': 'BHD', 'Bangladesh': 'BDT', 'Barbados': 'BBD', 'Belarus': 'BYR', 'Belgium': 'EUR', 'Belize': 'BZD', 'Benin': 'XOF', 'Bermuda': 'BMD', 'Bhutan': 'BTN', 'Bolivia': 'BOB', 'Bosnia and Herzegovina': 'BAM', 'Botswana': 'BWP',

```

### .capitals()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.capitals()) 
```
```python
{'Afghanistan': 'Kabul', 'Aland Islands': 'Mariehamn', 'Albania': 'Tirana', 'Algeria': 'Algiers', 'American Samoa': 'Pago Pago', 'Andorra': 'Andorra la Vella', 'Angola': 'Luanda', 'Anguilla': 'The Valley', 'Antarctica': '', 'Antigua And Barbuda': "St. John's", 'Argentina': 'Buenos Aires', 'Armenia': 'Yerevan', 'Aruba': 'Oranjestad', 'Australia': 'Canberra', 'Austria': 'Vienna', 'Azerbaijan': 'Baku', 'Bahamas The': 'Nassau', 'Bahrain': 'Manama', 'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Belize': 'Belmopan', 
```

### .continents()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.continents()) 
```

```
[{'country': 'Afghanistan', 'continent': 'Asia'}, {'country': 'Albania', 'continent': 'Europe'}, {'country': 'Algeria', 'continent': 'Africa'}, {'country': 'American Samoa', 'continent': 'Oceania'}, {'country': 'Andorra', 'continent': 'Europe'}, {'country': 'Angola', 'continent': 'Africa'}, {'country': 'Anguilla', 'continent': 'North America'},{'country': 'Antarctica', 'continent': 'Antarctica'},

```

### .countries_in_continents()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.countries_in_continents()) 
```

```python
{'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macao', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
```

### .regions()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.regions()) 
```

```python
[{'country': 'Afghanistan', 'location': 'Southern and Central Asia'}, {'country': 'Albania', 'location': 'Southern Europe'}, {'country': 'Algeria', 'location': 'Northern Africa'}, {'country': 'American Samoa', 'location': 'Polynesia'}, {'country': 'Andorra', 'location': 'Southern Europe'}, {'country': 'Angola', 'location': 'Central Africa'}, {'country': 'Anguilla', 'location': 'Caribbean'}, {'country': 'Antarctica', 'location': 'Antarctica'}, {'country': 'Antigua and Barbuda', 'location': 'Caribbean'}, {'country': 'Argentina', 'location': 'South America'}, {'country': 'Armenia', 'location': 'Middle East'}, {'country': 'Aruba', 'location': 'Caribbean'}, {'country': 'Australia', 'location': 'Australia and New Zealand'},  
```

### .countries_in_region()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.countries_in_region()) 
```

```python
{'Antarctica': ['Antarctica', 'Bouvet Island', 'French Southern territories', 'Heard Island and McDonald Islands', 'South Georgia and the South Sandwich Islands'], 'Eastern Europe': ['Belarus', 'Bulgaria', 'Czech Republic', 'Hungary', 'Moldova', 'Poland', 'Romania', 'Russian Federation', 'Slovakia', 'Ukraine'], 'Southern Europe': ['Albania', 'Andorra', 'Bosnia and Herzegovina', 'Croatia', 'Gibraltar', 'Greece', 'Holy See (Vatican City State)', 'Italy', 'North Macedonia', 'Malta', 'Portugal', 'San Marino', 'Slovenia', 'Spain', 'Yugoslavia'], 'Western Europe': ['Austria', 'Belgium', 'France', 'Germany', 'Liechtenstein', 'Luxembourg', 'Monaco', 'Netherlands', 'Switzerland'], 'North America': ['Bermuda', 'Canada', 'Greenland', 'Saint Pierre and Miquelon', 'United States'],
```

### .states()

```python
from countrydetails import countries

country = countries.all_countries()
print(country.states()) 
```
```python
{'id': 1836, 'name': 'Nenets Autonomous Okrug', 'state_code': 'NEN'}, {'id': 1857, 'name': 'Nizhny Novgorod Oblast', 'state_code': 'NIZ'}, {'id': 1834, 'name': 'Novgorod Oblast', 'state_code': 'NGR'}, {'id': 1888, 'name': 'Novosibirsk', 'state_code': 'NVS'}, {'id': 1846, 'name': 'Omsk Oblast', 'state_code': 'OMS'}, {'id': 1886, 'name': 'Orenburg Oblast', 'state_code': 'ORE'}, {'id': 1908, 'name': 'Oryol Oblast', 'state_code': 'ORL'}, {'id': 1909, 'name': 'Penza Oblast', 'state_code': 'PNZ'}, {'id': 1871, 'name': 'Perm Krai', 'state_code': 'PER'}, {'id': 1833, 'name': 'Primorsky Krai', 'state_code': 'PRI'}, {'id': 1863, 'name': 'Pskov Oblast', 'state_code': 'PSK'}, {'id': 1852, 'name': 'Republic of Adygea', 'state_code': 'AD'} 
```
