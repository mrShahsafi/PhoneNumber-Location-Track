import phonenumbers as pn
from text import number
from phonenumbers import geocoder
from phonenumbers import carrier


'''
Geocoder here is a function in phonenumbers. It provides geographical coordinates corresponding to a location.

'''
try:
    
    ch_number = pn.parse(number, "CH") # CH stands for Country History.
    service_provider = pn.parse(number, "RO")

    output_country = geocoder.description_for_number(ch_number, "en")
    output_carier = carrier.name_for_number(service_provider, "en")
except Exception as e:
    output_country = ' NaaN '
    output_carier = ' Naan '

print(
    f'Number Country origin:{output_country}.\n Number Carier:{output_carier}'
)
