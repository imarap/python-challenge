import warnings
warnings.filterwarnings('ignore')

# Import Dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, Table, select
from flask import Flask, render_template, jsonify, request, redirect
import os
import pandas as pd
### 

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
#Base.classes.keys()

Otu = Base.classes.otu
Samples = Base.classes.samples
SamplesMetadata = Base.classes.samples_metadata
session = Session(engine)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/names")
def get_sample_names():
    csvpath = os.path.join('DataSets','belly_button_biodiversity_samples.csv')
    bbd_df = pd.read_csv(csvpath)
    bbd_data = []
    totrows = len(bbd_df.axes[1])
    for i in bbd_df.index:
        if (i < totrows and i>0):
            bbd_data.append(bbd_df.columns[i])
    
    return jsonify(bbd_data)


@app.route("/otu")
def get_otu_id():
    #results = (session
    #           .query(Otu.lowest_taxonomic_unit_found)
    #           .all())
    csvpath = os.path.join('DataSets','belly_button_biodiversity_otu_id.csv')
    bbd_df = pd.read_csv(csvpath)
    bbd_data = []
    for index, row in bbd_df.iterrows():
        bbd_data.append(row['lowest_taxonomic_unit_found'])
    
    return jsonify(bbd_data)


@app.route('/metadata/<sample>')
def get_sample(sample='BB_940'):
    sample = sample[3:6]
    results = (session
              .query(SamplesMetadata.AGE, SamplesMetadata.BBTYPE, SamplesMetadata.ETHNICITY, SamplesMetadata.GENDER, SamplesMetadata.LOCATION, SamplesMetadata.SAMPLEID)
              .filter(SamplesMetadata.SAMPLEID == sample)
              .all()
              )
    bbd_dict = []
    for res in results:
        row = {}
        row["AGE"] = res[0]
        row["BBTYPE"] = res[1]
        row["ETHNICITY"] = res[2]
        row["GENDER"] = res[3]
        row["LOCATION"] = res[4]
        row["SAMPLEID"] = res[5]
        bbd_dict.append(row)
    
    return jsonify(bbd_dict)

@app.route('/wfreq/<sample>')
def get_wfreq(sample='BB_940'):
    wsample = sample[3:6]
    results = (session
              .query(SamplesMetadata.WFREQ)
              .filter(SamplesMetadata.SAMPLEID == wsample)
              .scalar()
              )
    return jsonify(results)
    
@app.route("/samples/<sample>")
def get_otu_samples(sample='BB_940'):
    csvpath = os.path.join('DataSets','belly_button_biodiversity_samples.csv')
    bbd_df = pd.read_csv(csvpath)
    otu_sample_df = bbd_df[['otu_id', sample]]
    sorted_df = otu_sample_df.sort_values(by=[sample],ascending=False)
    sorted_df = sorted_df.dropna(axis=0, how='any')
    bbd_otu = []
    bbd_sample = []
    bbd_data = []
    for index, row in sorted_df.iterrows():
        bbd_otu.append(str(int(row['otu_id'])))
        bbd_sample.append(int(row[sample]))
    bbd_dict = {
        "otu_ids": bbd_otu,
        "sample_values": bbd_sample
    }
    bbd_data.append(bbd_dict)
    return jsonify(bbd_data)

if __name__ == "__main__":
	
    app.run(debug=True)