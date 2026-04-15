from flask import Flask,jsonify,request
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

@app.route("/ufo_sightings_country",methods = ["GET"])
def get_sightings_country():
    #get the value from the querystring that is in the country argument
    country = request.args.get("country","")
    sightings = load_ufo_data("data/sightings.csv")
    #make a copy of the sightings list
    filtered_sightings = sightings.copy()

    for sighting in sightings:
       if not country and sighting["country"].lower() != country.lower():
          filtered_sightings.remove(sighting)

    #return the filtered list
    return jsonify(filtered_sightings)   

#Instead of removing rows that DO NOT match, start with an empty filtered_sightings, and ADD the ones that do match
# New route
@app.route("/ufo_sightings_country_add",methods = ["GET"])
def get_sightings_country_add():
    #get the value from the querystring that is in the country argument
    country = request.args.get("country","")
    sightings = load_ufo_data("data/sightings.csv")
    #make a copy of the sightings list
    filtered_sightings = []

    for sighting in sightings:
       if country or sighting["country"].lower() == country.lower():
          filtered_sightings.append(sighting)

    #return the filtered list
    return jsonify(filtered_sightings)   
       
@app.route("/ufo_sightings_comments",methods = ["GET"])
def get_sightings_comments():
    search_text = request.args.get("search_text","")
    sightings = load_ufo_data("data/sightings.csv")

    filtered_sightings = []

    for sighting in sightings:
        comments = sighting.get("comments","").lower()
        if search_text in comments:
           filtered_sightings.append(sighting)
    
    return jsonify(filtered_sightings)
