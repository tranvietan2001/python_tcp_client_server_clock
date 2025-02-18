# def split_string(input_string):
#     # Tách chuỗi theo dấu phẩy và xóa khoảng trắng dư thừa
#     items = [item.strip().strip("'") for item in input_string.split(',')]
#     return items

# # Chuỗi đầu vào
# input_string = "'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Ciudad_Juarez', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Kyiv', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kanton', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET', 'Zulu'"

# # Tách chuỗi
# result = split_string(input_string)

# # In kết quả
# for item in result:
#     print(item)



# import pytz
# from datetime import datetime

# def get_time_in_timezone(timezone):
#     # Lấy thời gian hiện tại theo múi giờ cụ thể
#     tz = pytz.timezone(timezone)
#     return datetime.now(tz)

# # Danh sách các quốc gia và múi giờ tương ứng
# timezones = {
#     'Vietnam': 'Asia/Ho_Chi_Minh',
#     'United States (New York)': 'America/New_York',
#     'United Kingdom': 'Europe/London',
#     'Japan': 'Asia/Tokyo',
#     'Germany': 'Europe/Berlin',
#     'Australia (Sydney)': 'Australia/Sydney',
# }

# # Hiển thị thời gian cho mỗi quốc gia
# for country, timezone in timezones.items():
#     current_time = get_time_in_timezone(timezone)
#     print(f"Current time in {country}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")




# Chuỗi đầu vào
input_string = '''
"AD": "Andorra",
"AE": "United Arab Emirates",
"AF": "Afghanistan",
"AG": "Antigua and Barbuda",
"AI": "Anguilla",
"AL": "Albania",
"AM": "Armenia",
"AO": "Angola",
"AQ": "Antarctica",
"AR": "Argentina",
"AS": "American Samoa",
"AT": "Austria",
"AU": "Australia",
"AW": "Aruba",
"AX": "\u00c5land Islands",
"AZ": "Azerbaijan",
"BA": "Bosnia and Herzegovina",
"BB": "Barbados",
"BD": "Bangladesh",
"BE": "Belgium",
"BF": "Burkina Faso",
"BG": "Bulgaria",
"BH": "Bahrain",
"BI": "Burundi",
"BJ": "Benin",
"BL": "Saint Barthélemy",
"BM": "Bermuda",
"BN": "Brunei Darussalam",
"BO": "Bolivia, Plurinational State of",
"BQ": "Caribbean Netherlands",
"BR": "Brazil",
"BS": "Bahamas",
"BT": "Bhutan",
"BV": "Bouvet Island",
"BW": "Botswana",
"BY": "Belarus",
"BZ": "Belize",
"CA": "Canada",
"CC": "Cocos (Keeling) Islands",
"CD": "Congo, the Democratic Republic of the",
"CF": "Central African Republic",
"CG": "Republic of the Congo",
"CH": "Switzerland",
"CI": "C\u00f4te d'Ivoire",
"CK": "Cook Islands",
"CL": "Chile",
"CM": "Cameroon",
"CN": "China (People's Republic of China)",
"CO": "Colombia",
"CR": "Costa Rica",
"CU": "Cuba",
"CV": "Cape Verde",
"CW": "Cura\u00e7ao",
"CX": "Christmas Island",
"CY": "Cyprus",
"CZ": "Czech Republic",
"DE": "Germany",
"DJ": "Djibouti",
"DK": "Denmark",
"DM": "Dominica",
"DO": "Dominican Republic",
"DZ": "Algeria",
"EC": "Ecuador",
"EE": "Estonia",
"EG": "Egypt",
"EH": "Western Sahara",
"ER": "Eritrea",
"ES": "Spain",
"ET": "Ethiopia",
"EU": "Europe",
"FI": "Finland",
"FJ": "Fiji",
"FK": "Falkland Islands (Malvinas)",
"FM": "Micronesia, Federated States of",
"FO": "Faroe Islands",
"FR": "France",
"GA": "Gabon",
"GB-ENG": "England",
"GB-NIR": "Northern Ireland",
"GB-SCT": "Scotland",
"GB-WLS": "Wales",
"GB": "United Kingdom",
"GD": "Grenada",
"GE": "Georgia",
"GF": "French Guiana",
"GG": "Guernsey",
"GH": "Ghana",
"GI": "Gibraltar",
"GL": "Greenland",
"GM": "Gambia",
"GN": "Guinea",
"GP": "Guadeloupe",
"GQ": "Equatorial Guinea",
"GR": "Greece",
"GS": "South Georgia and the South Sandwich Islands",
"GT": "Guatemala",
"GU": "Guam",
"GW": "Guinea-Bissau",
"GY": "Guyana",
"HK": "Hong Kong",
"HM": "Heard Island and McDonald Islands",
"HN": "Honduras",
"HR": "Croatia",
"HT": "Haiti",
"HU": "Hungary",
"ID": "Indonesia",
"IE": "Ireland",
"IL": "Israel",
"IM": "Isle of Man",
"IN": "India",
"IO": "British Indian Ocean Territory",
"IQ": "Iraq",
"IR": "Iran, Islamic Republic of",
"IS": "Iceland",
"IT": "Italy",
"JE": "Jersey",
"JM": "Jamaica",
"JO": "Jordan",
"JP": "Japan",
"KE": "Kenya",
"KG": "Kyrgyzstan",
"KH": "Cambodia",
"KI": "Kiribati",
"KM": "Comoros",
"KN": "Saint Kitts and Nevis",
"KP": "Korea, Democratic People's Republic of",
"KR": "Korea, Republic of",
"KW": "Kuwait",
"KY": "Cayman Islands",
"KZ": "Kazakhstan",
"LA": "Laos (Lao People's Democratic Republic)",
"LB": "Lebanon",
"LC": "Saint Lucia",
"LI": "Liechtenstein",
"LK": "Sri Lanka",
"LR": "Liberia",
"LS": "Lesotho",
"LT": "Lithuania",
"LU": "Luxembourg",
"LV": "Latvia",
"LY": "Libya",
"MA": "Morocco",
"MC": "Monaco",
"MD": "Moldova, Republic of",
"ME": "Montenegro",
"MF": "Saint Martin",
"MG": "Madagascar",
"MH": "Marshall Islands",
"MK": "North Macedonia",
"ML": "Mali",
"MM": "Myanmar",
"MN": "Mongolia",
"MO": "Macao",
"MP": "Northern Mariana Islands",
"MQ": "Martinique",
"MR": "Mauritania",
"MS": "Montserrat",
"MT": "Malta",
"MU": "Mauritius",
"MV": "Maldives",
"MW": "Malawi",
"MX": "Mexico",
"MY": "Malaysia",
"MZ": "Mozambique",
"NA": "Namibia",
"NC": "New Caledonia",
"NE": "Niger",
"NF": "Norfolk Island",
"NG": "Nigeria",
"NI": "Nicaragua",
"NL": "Netherlands",
"NO": "Norway",
"NP": "Nepal",
"NR": "Nauru",
"NU": "Niue",
"NZ": "New Zealand",
"OM": "Oman",
"PA": "Panama",
"PE": "Peru",
"PF": "French Polynesia",
"PG": "Papua New Guinea",
"PH": "Philippines",
"PK": "Pakistan",
"PL": "Poland",
"PM": "Saint Pierre and Miquelon",
"PN": "Pitcairn",
"PR": "Puerto Rico",
"PS": "Palestine",
"PT": "Portugal",
"PW": "Palau",
"PY": "Paraguay",
"QA": "Qatar",
"RE": "Réunion",
"RO": "Romania",
"RS": "Serbia",
"RU": "Russian Federation",
"RW": "Rwanda",
"SA": "Saudi Arabia",
"SB": "Solomon Islands",
"SC": "Seychelles",
"SD": "Sudan",
"SE": "Sweden",
"SG": "Singapore",
"SH": "Saint Helena, Ascension and Tristan da Cunha",
"SI": "Slovenia",
"SJ": "Svalbard and Jan Mayen Islands",
"SK": "Slovakia",
"SL": "Sierra Leone",
"SM": "San Marino",
"SN": "Senegal",
"SO": "Somalia",
"SR": "Suriname",
"SS": "South Sudan",
"ST": "Sao Tome and Principe",
"SV": "El Salvador",
"SX": "Sint Maarten (Dutch part)",
"SY": "Syrian Arab Republic",
"SZ": "Kingdom of Eswatini",
"TC": "Turks and Caicos Islands",
"TD": "Chad",
"TF": "French Southern Territories",
"TG": "Togo",
"TH": "Thailand",
"TJ": "Tajikistan",
"TK": "Tokelau",
"TL": "Timor-Leste",
"TM": "Turkmenistan",
"TN": "Tunisia",
"TO": "Tonga",
"TR": "Republic of Türkiye",
"TT": "Trinidad and Tobago",
"TV": "Tuvalu",
"TW": "Taiwan (Republic of China)",
"TZ": "Tanzania, United Republic of",
"UA": "Ukraine",
"UG": "Uganda",
"UM": "US Minor Outlying Islands",
"US": "United States",
"UY": "Uruguay",
"UZ": "Uzbekistan",
"VA": "Holy See (Vatican City State)",
"VC": "Saint Vincent and the Grenadines",
"VE": "Venezuela, Bolivarian Republic of",
"VG": "Virgin Islands, British",
"VI": "Virgin Islands, U.S.",
"VN": "Vietnam",
"VU": "Vanuatu",
"WF": "Wallis and Futuna Islands",
"WS": "Samoa",
"XK": "Kosovo",
"YE": "Yemen",
"YT": "Mayotte",
"ZA": "South Africa",
"ZM": "Zambia",
"ZW": "Zimbabwe"
'''



# Tách chuỗi theo dấu phẩy
items = input_string.split(',')

# Bỏ phần trước dấu hai chấm và thêm dấu nháy đơn
formatted_countries = []
for item in items:
    parts = item.split(':')
    if len(parts) > 1:
        country = parts[1].strip().strip('"')
        formatted_countries.append(f"'{country}'")

# In kết quả
for country in formatted_countries:
    print(country)





# country_name = pytz.timezone("America/Sao_Paulo")
# country_time = datetime.now(country_name)
# print(country_name)
# print(country_time)
# print(country_time.strftime("%d-%m-%y -------- %H:%M:%S"))


# from PyQt6.QtCore import QPoint, Qt, QTime, QTimer
# from PyQt6.QtGui import QColor, QPainter, QPolygon
# from PyQt6.QtWidgets import QApplication, QWidget
# class AnalogClock(QWidget):
#     secondHand = QPolygon([
#         QPoint(7, 8),
#         QPoint(-7, 8),
#         QPoint(0, -95)
#     ])
#     hourHand = QPolygon([
#         QPoint(7, 8),
#         QPoint(-7, 8),
#         QPoint(0, -50)
#     ])
#     minuteHand = QPolygon([
#         QPoint(7, 8),
#         QPoint(-7, 8),
#         QPoint(0, -70)
#     ])
#     hourColor = QColor(127, 0, 127)
#     minuteColor = QColor(0, 100, 250, 200)
#     secondColor = QColor(195, 0, 0, 150)
#     def __init__(self, parent=None):
#         super(AnalogClock, self).__init__(parent)
#         timer = QTimer(self)
#         timer.timeout.connect(self.update)
#         timer.start(1000)
#         self.setWindowTitle("Analog Clock")
#         self.resize(600, 600)
#     def paintEvent(self, event):
#         side = min(self.width(), self.height())
#         time = QTime.currentTime()
#         painter = QPainter(self)
#         # painter.setRenderHint(QPainter.Antialiasing)
#         painter.translate(self.width() / 2, self.height() / 2)
#         painter.scale(side / 200, side / 200)
#         # painter.setPen(Qt.NoPen)
#         painter.setBrush(AnalogClock.hourColor)
#         painter.save()
#         painter.rotate(30.0 * (time.hour() + time.minute() / 60.0)) # 360/12.0 times per hour
#         print(f'hour:{time.hour()}, minute:{time.minute()}, second:{time.second()}')
#         painter.drawConvexPolygon(AnalogClock.hourHand)
#         painter.restore()
#         painter.setPen(AnalogClock.hourColor)

#         # vẽ 12 vạch 12 số
#         for i in range(12):
#             painter.drawLine(88, 0, 96, 0)
#             painter.rotate(30.0)


#         # painter.setPen(Qt.NoPen)
#         painter.setBrush(AnalogClock.minuteColor)
#         painter.save()
#         painter.rotate(6.0 * (time.minute() + time.second() / 60.0))  # 6 times a minute
#         painter.drawConvexPolygon(AnalogClock.minuteHand)
#         painter.restore()
#         painter.setPen(AnalogClock.minuteColor)
#         for j in range(60):
#             if (j % 5) != 0:
#                 painter.drawLine(92, 0, 96, 0)
#             painter.rotate(6.0)
#         # painter.setPen(Qt.NoPen)
#         painter.setBrush(AnalogClock.secondColor)
#         painter.save()
#         painter.rotate(360 * (time.minute() + time.second() / 60.0))  # 360 times in a minute
#         painter.drawConvexPolygon(AnalogClock.secondHand)
#         painter.restore()
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     clock = AnalogClock()
#     clock.show()
#     sys.exit(app.exec())