#################################################
# Import Dependencies
#################################################

import pandas as pd


a = pd.read_csv("Resources/cities.csv")
a.to_html("rawdata.html", index=False )


