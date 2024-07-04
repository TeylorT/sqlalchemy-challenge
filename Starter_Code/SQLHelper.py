import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd
import numpy as np

# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///Resources/hawaii.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def query_precipitation(self):
        # Save reference to the table
        Precipitation = self.Base.classes.precipitation

        # Create our session (link) from Python to the DB
        session = Session(self.engine)

        # Query all passengers
        results =  session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

        # close session
        session.close()

        df = pd.DataFrame(results)
        data = df.to_dict(orient="prcp")
        return(data)

   