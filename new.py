
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    number = request.form['number']

    import phonenumbers
    from phonenumbers import geocoder
# from test import number
    import folium
    import os

    key = "YOUR API KEY"

    check_number = phonenumbers.parse(number)
    number_location = geocoder.description_for_number(check_number, "en")
    print("Country:-", number_location)

    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number)
    print("Service provider:-", carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode
    geocoder = OpenCageGeocode(key)

    query = str(number_location)
    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print(lat, lng)

    map_location = folium.Map(location = [lat,lng], zoom_start=9)
    folium.Marker([lat,lng], popup=number_location).add_to(map_location)
    file_path = os.path.join(app.root_path, 'templates', 'track.html')
    map_location.save(file_path)




    return render_template('track.html')

if __name__ =='__main__':
    app.run(debug=True)


