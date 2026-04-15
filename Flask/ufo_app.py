from flask import Flask,jsonify
from csv import DictReader

app = Flask(__name__)




@app.route("/")
def home():
   return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>UFO sightings from around the world!</h1>
        </body>
    </html>
    """ 

#function that takes parameter of a filepath string
#returns a list of dictionaries from the file
def load_ufo_data(filepath):
   sightings = []
   with open(filepath,'r',newline="") as f:
      reader = DictReader(f)
      for row in reader:
         sightings.append(row)
   return sightings

#Route to display all the sightings from sightings.csv
@app.route("/ufo_sightings_file")
def get_sightings_info():
   sightings = load_ufo_data("data/sightings.csv")
   return jsonify(sightings)

#Route to display city and state of each sighting in a unordered list
@app.route("/ufo_sightings_locations")
def get_sightings_locations():
    sightings = load_ufo_data("data/sightings.csv")

    UFO_html = ""

    for sighting in sightings:
      UFO_html += f"<li>{sighting["city"]}, {sighting["state"]}</li>"

    return f"""
    <html>
        <head>
            <title>Sighting Locations</title>
        </head>
        <body>
            <h1>Locations</h1>
            <ul>
            {UFO_html}
            </ul>
        </body>
    </html>
"""

