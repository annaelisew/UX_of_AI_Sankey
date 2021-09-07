#Sankey Diagram python script for UX of AI research project
#https://www.linkedin.com/pulse/guide-making-sankey-diagrams-using-python-latest-covid-ying-li/

import pandas as pd
import holoviews as hv
hv.extension('bokeh')
from bokeh.plotting import show
import csv

#read the data
file_name = "taxonomy_data.csv" #to run a new csv file, change this name
col_list = ["Col1", "Col2", "Value"]
csvdata = csv.reader(open(file_name, "rt"), delimiter=",", quotechar="|")
value_list = []

#create array of all elements in Col2 (easier than listing out)
for row in csvdata:
	value_list.append(row[1])
data = pd.read_csv("taxonomy_data.csv", usecols=col_list, error_bad_lines=False)

#format data
boolean_series = data.Col2.isin(value_list)
data = data[boolean_series]
print (data.head)

#make basic sankey diagram
sankey1 = hv.Sankey(data,kdims=["Col1", "Col2"], vdims=["Value"])
show (hv.render(sankey1))

#more formatted version of sankey diagram
sankey2 = hv.Sankey(data,kdims=["Col1", "Col2"], vdims=["Value"])
sankey2.opts(cmap="PuBuGn_r",label_position='outer',
                                edge_color='Col1', edge_line_width=0,
                                 node_alpha=1.0, node_width=10, node_sort=True,
                                 width=4200, height=4200, bgcolor="snow",
                                 title="UX of AI Taxonomy Data Structure")

show (hv.render(sankey2))
