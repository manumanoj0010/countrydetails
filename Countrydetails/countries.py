from glob import glob
from os.path import isfile, realpath, dirname
import json


# Everything is clear no errors and mostly no error handling is required here


class all_countries:
    """To get the details of all countries in the world

    Example:
        country = all_countries()
    """
    def __init__(self):
        """constructor method"""
        dir_path = dirname(realpath(__file__))
        countries_file_path = dir_path + '/data/countries.json'
        continents_file_path = dir_path + '/data/continents.json'
        region_file_path = dir_path + '/data/region.json'
        states_file_path = dir_path + '/data/states.json'
        languages_to_capitals_file_path = dir_path + '/data/langtocountries.json'
        with open(countries_file_path, encoding='utf-8') as file:
            countries_file = json.load(file)
            self.countries_file = countries_file
        with open(continents_file_path, encoding='utf-8') as file:
            continents_file = json.load(file)
            self.continents_file = continents_file
        with open(region_file_path, encoding='utf-8') as file:
            region_file = json.load(file)
            self.region_file = region_file
        with open(states_file_path, encoding='utf-8') as file:
            states_file = json.load(file)
            self.states_file = states_file
        with open(languages_to_capitals_file_path, encoding='utf-8') as file:
            languages_to_capitals_file = json.load(file)
            self.languages_to_capitals_file = languages_to_capitals_file


        self.country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo The Democratic Republic Of The', 'Cook Islands', 'Costa Rica', "Cote D'Ivoire (Ivory Coast)", 'Croatia (Hrvatska)', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji Islands', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey and Alderney', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard and McDonald Islands', 'Honduras', 'Hong Kong S.A.R.', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau S.A.R.', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Man (Isle of)', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 
        'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands Antilles', 'Netherlands The', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory Occupied', 'Panama', 'Papua new Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Island', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent And The Grenadines', 'Saint-Barthelemy', 'Saint-Martin (French part)', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard And Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State (Holy See)', 'Venezuela', 'Vietnam', 'Virgin Islands (British)', 'Virgin Islands (US)', 'Wallis And Futuna Islands', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


    def countries(self):

        """Returns all the available countries in the world.
        :return: list
        """
        return self.country_list


    def phone_code(self):
 
        """Returns the countries and their Phone codes.
        :return: dict
        """
        phonecode_dict={}
        a = self.countries_file
        for i in a:
            phonecode_dict[i['name']]=i['phone_code']
        return phonecode_dict

    def currencies(self):

        """Returns the countries and their Currencies.
        :return: dict
        """
        currency_dict={}
        a = self.countries_file
        for i in a:
            currency_dict[i['name']]=i['currency']
        return currency_dict

    def capitals(self):
        
        """Returns the countries and their capitals.
        :return: dict
        """
        capital_dict={}
        a = self.countries_file
        for i in a:
            capital_dict[i['name']]=i['capital']
        return capital_dict
            
    def continents(self):
        """Returns the countries with their continents.
        :return: json
        """
        return self.continents_file


    def countries_in_continents(self):
        """Returns the list of countries under continents.
        :return: dict
        """
        asia =[]
        europe=[]
        africa =[]
        oceania =[]
        north_america =[]
        antarctica = []
        south_america = []
        continents_dict={}
        for i in self.continents_file:
            if i['continent'] == 'Asia':
                asia.append(i['country'])
            if i['continent'] == 'North America':
                north_america.append(i['country'])
            if i['continent'] == 'Europe':
                europe.append(i['country'])
            if i['continent'] == 'Africa':
                africa.append(i['country'])
            if i['continent'] == 'South America':
                south_america.append(i['country'])
            if i['continent'] == 'Oceania':
                oceania.append(i['country'])
            if i['continent'] == 'Antarctica':
                antarctica.append(i['country'])
        continents_dict['Asia'] =asia
        continents_dict['North America'] = north_america
        continents_dict['Europe'] = europe
        continents_dict['Africa'] = africa
        continents_dict['South America'] = south_america
        continents_dict['Oceania'] = oceania
        continents_dict['Antarctica'] = antarctica
        
        return continents_dict
    
    def regions(self):
        """Returns the countries with their region.
        :return: json
        """
        return self.region_file

    def countries_in_region(self):
        """Returns the list of countries in a region.
        :return: dict
        """
        Southern_and_Central_Asia =[]
        Middle_East = []
        Southeast_Asia = []
        Eastern_Asia = []
        Southern_Europe=[]
        Western_Europe = []
        Eastern_Europe = []
        Nordic_Countries = []
        Baltic_Countries = []
        Northern_Africa =[]
        Central_Africa =[]
        Western_Africa = []
        Southern_Africa = []
        Eastern_Africa = []
        Caribbean = []
        South_America = []
        North_America = []
        Central_America = []
        Polynesia = []
        Melanesia = []
        Micronesia = []
        British_Isles = []
        Australia_and_New_Zealand = []
        Antarctica = []
        null = []

        region_dict={}

        for i in self.region_file:
            if i['location'] == 'Southern and Central Asia':
                Southern_and_Central_Asia.append(i['country'])

            elif i['location'] == 'Middle East':
                Middle_East.append(i['country'])

            elif i['location'] == 'Southeast Asia':
                Southeast_Asia.append(i['country'])
            
            elif i['location'] == 'Eastern Asia':
                Eastern_Asia.append(i['country'])

            elif i['location'] == 'Southern Europe':
                Southern_Europe.append(i['country'])

            elif i['location'] == 'Western Europe':
                Western_Europe.append(i['country'])

            elif i['location'] == 'Eastern Europe':
                Eastern_Europe.append(i['country'])

            elif i['location'] == 'Nordic Countries':
                Nordic_Countries.append(i['country'])
            
            elif i['location'] == 'Baltic Countries':
                Baltic_Countries.append(i['country'])

            elif i['location'] == 'Northern Africa':
                Northern_Africa.append(i['country'])

            elif i['location'] == 'Central Africa':
                Central_Africa.append(i['country'])

            elif i['location'] == 'Western Africa':
                Western_Africa.append(i['country'])

            elif i['location'] == 'Southern Africa':
                Southern_Africa.append(i['country'])

            elif i['location'] == 'Eastern Africa':
                Eastern_Africa.append(i['country'])

            elif i['location'] == 'Caribbean':
                Caribbean.append(i['country'])
            
            elif i['location'] == 'South America':
                South_America.append(i['country'])

            elif i['location'] == 'North America':
                North_America.append(i['country'])

            elif i['location'] == 'Central America':
                Central_America.append(i['country'])

            elif i['location'] == 'Melanesia':
                Melanesia.append(i['country'])

            elif i['location'] == 'Polynesia':
                Polynesia.append(i['country'])

            elif i['location'] == 'Micronesia':
                Micronesia.append(i['country'])

            elif i['location'] == 'British Isles':
                British_Isles.append(i['country'])
            
            elif i['location'] == 'Australia and New Zealand':
                Australia_and_New_Zealand.append(i['country'])

            elif i['location'] == 'Antarctica':
                Antarctica.append(i['country'])
        
            else:
                null.append(i['country'])

        region_dict['Antarctica'] = Antarctica
        region_dict['Eastern Europe'] = Eastern_Europe
        region_dict['Southern Europe'] = Southern_Europe
        region_dict['Western Europe'] = Western_Europe
        region_dict['North America'] = North_America
        region_dict['South America'] = South_America
        region_dict['Central America'] = Central_America
        region_dict['Eastern Asia'] = Eastern_Asia
        region_dict['Southeast Asia'] = Southeast_Asia
        region_dict['Southern and Central_Asia'] = Southern_and_Central_Asia
        region_dict['Middle East'] = Middle_East
        region_dict['Australia and New_Zealand'] = Australia_and_New_Zealand
        region_dict['Baltic Countries'] = Baltic_Countries
        region_dict['British Isles'] = British_Isles
        region_dict['Micronesia'] = Micronesia
        region_dict['Polynesia'] = Polynesia
        region_dict['Melanesia'] = Melanesia
        region_dict['Caribbean'] = Caribbean
        region_dict['Central Africa'] = Central_Africa
        region_dict['Eastern Africa'] = Eastern_Africa
        region_dict['Northern Africa'] = Northern_Africa
        region_dict['Western Africa'] = Western_Africa
        region_dict['Southern Africa'] = Southern_Africa
        region_dict['Australia and New_Zealand'] = Australia_and_New_Zealand
        region_dict['Baltic Countries'] = Baltic_Countries
        region_dict['Nordic Countries'] = Nordic_Countries
        region_dict['Null'] = null

        return region_dict

    def states(self):
        """Returns all the available states in the world.
        :return: dict
        """
        states_dict = {}
        for i in self.states_file:
            states_dict[i['name']] = i['states']
        return states_dict

    def languages(self):
        """ Returns capitals with their languages
        :return: dict
        :format: {country_name: ( capital, national_language[] in code ) }
        """
        languages_capital_dict={}
        a = self.languages_to_capitals_file
        for i in range(65,91):
          for j in range(65,91):
            res_str = chr(i)+chr(j)
            if(res_str in a):
              languages_capital_dict[a[res_str]["name"]]=(a[res_str]["capital"],a[res_str]["languages"])
        return languages_capital_dict
