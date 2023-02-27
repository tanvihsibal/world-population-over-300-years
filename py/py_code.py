import pandas as pd
import plotly.express as px

# ************************
# download the following xlsx file and save it in data/
# https://gapm.io/dl_popv7

# Population data is in the 3rd sheet
df = pd.read_excel('data/population_data.xlsx', sheet_name=3, header=0)

df['iso_alpha'] = df['geo'].str.upper()

# display for year 2010
# df_2010 = df[df['time'] == 2010]
# fig = px.choropleth(
# 	df_2010,
# 	locations = "iso_alpha",
# 	color = "Population",
# 	color_continuous_scale = "RdBu_r",
# 	scope = "world"
# )

# fig.update_layout(
# 	title_text = 'World Population in 2010',
# )

# fig.show()

# display from 1800 to 2100 gapped by 20 years
gap_years = [i for i in range(1800, 2101, 20)]
df_by_20 = df[df['time'].isin(gap_years)]

# to add fixed range: range_color = (0, 1_500_000_000)
fig = px.choropleth(
	df_by_20,
	locations = "iso_alpha",
	color = "Population",
	hover_name = "name", 
	color_continuous_scale = "RdBu_r",
	scope = "world",
	animation_frame = "time",
)

fig.update_layout(
	title_text = 'World Population Prediction 1800 - 2100',
)

fig.show()