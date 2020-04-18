# from flask import Flask, render_template, jsonify
# import json
# import pandas as pd
# from json import dumps
# import sqlalchemy
# from sqlalchemy.orm import class_mapper
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, inspect, func

# engine = create_engine('postgresql://postgres:Notkerino342@localhost:5432/EnergyDB')
# connection = engine.connect()
# inspector = inspect(engine)
# print(inspector.get_table_names())

# residential1 = pd.read_sql('SELECT * FROM "Residential_Sector"', connection)
# commercial1 = pd.read_sql('SELECT * FROM "Commercial_Sector"', connection)
# industrial1 = pd.read_sql('SELECT * FROM "Industrial_Sector"', connection)
# transportation1 = pd.read_sql('SELECT * FROM "Transportation_Sector"', connection)
# total_consumption1 = pd.read_sql('SELECT * FROM "Total_Consumption"', connection)
# state_sources1 = pd.read_sql('SELECT * FROM "State_Sources"', connection)
# us_sources1 = pd.read_sql('SELECT * FROM "US_Sources"', connection)

# residential = residential1.to_dict()
# commercial = commercial1.to_dict()
# industrial = industrial1.to_dict()
# transportation = transportation1.to_dict()
# total_consumption = total_consumption1.to_dict()
# state_sources = state_sources1.to_dict()
# us_sources = us_sources1.to_dict()

# # --------------------------------------------------

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", residential = residential,\
#                                          commercial = commercial,\
#                                          industrial = industrial,\
#                                          transportation = transportation,\
#                                          total_consumption = total_consumption,\
#                                          state_sources = state_sources,\
#                                          us_sources = us_sources)


# if __name__ == "__main__":
#     app.run(debug=True)
# print(json.dumps(us_sources))

import pandas as pd
from flask import Flask, render_template, jsonify
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

engine = create_engine('postgresql://postgres:Notkerino342@localhost:5432/EnergyDB')
connection = engine.connect()
inspector = inspect(engine)
#print(inspector.get_table_names())
residential_columns= inspector.get_columns('Residential_Sector')
#for column in residential_columns:
    #print(column["name"], column["type"])

residential1 = pd.read_sql('SELECT * FROM "Residential_Sector"', connection)
commercial1 = pd.read_sql('SELECT * FROM "Commercial_Sector"', connection)
industrial1 = pd.read_sql('SELECT * FROM "Industrial_Sector"', connection)
transportation1 = pd.read_sql('SELECT * FROM "Transportation_Sector"', connection)
total_consumption1 = pd.read_sql('SELECT * FROM "Total_Consumption"', connection)
state_sources1 = pd.read_sql('SELECT * FROM "State_Sources"', connection)
us_sources1 = pd.read_sql('SELECT * FROM "US_Sources"', connection)

residential = pd.DataFrame(residential1)       
residentialdict = residential.to_dict()

commercial = pd.DataFrame(commercial1)
commercialdict = commercial.to_dict()

industrial = pd.DataFrame(industrial1)
industrialdict = industrial.to_dict()

transportation = pd.DataFrame(transportation1)
transportationdict = transportation.to_dict()

total_consumption = pd.DataFrame(total_consumption1)
total_consumptiondict = total_consumption.to_dict()

state_sources = pd.DataFrame(state_sources1)
state_sourcesdict = state_sources.to_dict()
state_sourcesdict

us_sources = pd.DataFrame(us_sources1)
us_sourcesdict = us_sources.to_dict()
#us_sourcesdict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", residential = residentialdict,\
                                         commercial = commercialdict,\
                                         industrial = industrialdict,\
                                         transportation = transportationdict,\
                                         total_consumption = total_consumptiondict,\
                                         state_sources = state_sourcesdict,\
                                         us_sources = us_sourcesdict)
                                         

if __name__ == "__main__":
    app.run(debug=True)