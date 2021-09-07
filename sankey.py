import pandas as pd
import holoviews as hv
hv.extension('bokeh')
from bokeh.plotting import show
import csv

#read the data
col_list = ["Col1", "Col2", "Value"]
csvdata = csv.reader(open("taxonomy_data.csv", "rt"), delimiter=",", quotechar="|")
value_list = []

for row in csvdata:
	value_list.append(row[1])
data = pd.read_csv("taxonomy_data.csv", usecols=col_list, error_bad_lines=False)
print(data["Col1"])


boolean_series = data.Col2.isin(value_list)

data = data[boolean_series]

print (data.head)


sankey1 = hv.Sankey(data,kdims=["Col1", "Col2"], vdims=["Value"])
show (hv.render(sankey1))


sankey2 = hv.Sankey(data,kdims=["Col1", "Col2"], vdims=["Value"])
sankey2.opts(cmap="PuBuGn_r",label_position='outer',
                                edge_color='Col1', edge_line_width=0,
                                 node_alpha=1.0, node_width=10, node_sort=True,
                                 width=4200, height=4200, bgcolor="snow",
                                 title="UX of AI Taxonomy Data Structure")

show (hv.render(sankey2))
