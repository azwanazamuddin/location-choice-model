import requests
import numpy as np

class Geocoder:
    # Static API key
    api_key = "AIzaSyBGixZaVSudQgXOabY-ok8psg8xqiJgwPM"

    @classmethod
    def geocode_address(cls, address):
        address = str(address)
        address += ""
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={cls.api_key}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return lat, lng
        else:
            return np.nan, np.nan
