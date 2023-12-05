import pandas as pd
import plotly.express as px

# Filter the DataFrame for all causes deaths in 2017
allcauses_df_2017 = merged_df[(merged_df['Year'] == 2017) & (merged_df['Cause Name'] == 'All causes')]

# Calculate the ratio of all causes deaths to population for each state
ratios_by_state = {}

for state in merged_df['State'].unique():
    state_data = allcauses_df_2017[allcauses_df_2017['State'] == state]

    if not state_data.empty:
        allcauses_deaths = state_data['Deaths'].iloc[0]
        population = state_data['Population'].iloc[0]

        # Avoid division by zero
        if population != 0:
            ratio = allcauses_deaths / population
            ratios_by_state[state] = ratio

# Create a DataFrame from the dictionary
ratios_df = pd.DataFrame(list(ratios_by_state.items()), columns=['State', 'Ratio'])

# Create a bar chart
fig = px.bar(
    ratios_df,
    x='State',
    y='Ratio',
    title='Ratio of All Causes Deaths to Population in 2017',
    labels={'Ratio': 'Ratio of Deaths to Population'},
    color='Ratio',
    color_continuous_scale='Viridis'
)

# Customize the layout
fig.update_layout(xaxis=dict(tickmode='linear'), xaxis_title='State', yaxis_title='Deaths per Capita')

# Show the plot
fig.show()

fig.write_html("./plot1.html")
