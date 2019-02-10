import folium
from tqdm import tqdm
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim


def create_map(file, dct):
    """
    (string, dict) ->

    This function creates a map with HTML file
    """
    map = folium.Map(tiles="Mapbox Bright")
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open(file, 'r',
                                             encoding='utf-8-sig').read(),
                                   style_function=lambda x: {'fillColor':
                                                             'green'
                    if x['properties']['POP2005'] < 10000000 else 'orange'
        if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    fg_hc = folium.FeatureGroup(name="Years of the films")
    for key, value in dct.items():
        fg_hc.add_child(folium.CircleMarker(location=value,
                                            radius=2, popup=key,
                                            color='red', fill_opacity=0.5))
    map.add_child(fg_pp)
    map.add_child(fg_hc)
    map.add_child(folium.LayerControl())

    map.save("Map1.html")


def get_locations(dct):
    """
    (dict) -> dict

    This function returns a dict with the name of a film as a key and list of
    locations as a value
    """
    dct_loc = dict()
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    for key, value in tqdm(dct.items()):
        try:
            value = value.split(",")
            location = geolocator.geocode(value[0])
            dct_loc[key] = [location.latitude, location.longitude]
        except:
            pass

    return dct_loc


def file_data(path, year):
    """
    (string, int) -> dict

    Function returns dict with film as a key and location as a value.
    """
    lst_of_locations = []
    with open(path, errors='ignore') as f:
        for line in f:
            line = line.strip()
            lst_of_locations.append(line)

    dct = {}
    locations = []
    del lst_of_locations[:14]

    for elem in lst_of_locations:
        if "(" + str(year) + ")" in elem:
            elem = elem.replace('\t', " ")
            elem = elem.split(" ")
            if elem != '':
                locations.append(elem)

    for i in tqdm(locations):
        for elem in i:
            if 6 <= len(elem) <= 10 and "(" in elem and ")" in elem:
                ind = i.index(elem)
                one_str = i[:ind+1]
                one_str = " ".join(one_str)
                two_str = i[ind+1:]
                two_str = " ".join(two_str)
                if "(V)" in two_str:  # checking for rubbish
                    two_str = two_str.replace("(V)", "")
                if "(TV)" in two_str:
                    two_str = two_str.replace("(TV)", "")
                if "(VG)" in two_str:
                    two_str = two_str.replace("(VG)", "")
                if one_str not in dct.keys() or two_str not in dct.values():
                    dct[one_str] = two_str.strip()
    return dct


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    create_map("../docs/world.json", get_locations(file_data("../docs/locations.list.txt",
                                                     year)))

