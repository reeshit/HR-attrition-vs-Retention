import pandas as pd
import plotly.express as px


df = pd.read_csv("Age Group.csv", sep="\t", encoding="utf-16", header=None)


print(df.head())  


df.columns = ["Category", "Metric", "< 25", "25-34", "35-44", "45-55", "> 55"]

# Keep only rows where "Metric" is "Employee Count"
df_filtered = df[df["Metric"] == "Employee Count"].drop(columns=["Metric"])


df_filtered = df_filtered.set_index("Category").transpose()

# Reset index for plotting
df_filtered.reset_index(inplace=True)
df_filtered.rename(columns={"index": "Age Group"}, inplace=True)


df_filtered["Attrition"] = df_filtered["Attrition"].astype(float).astype(int)
df_filtered["Retention"] = df_filtered["Retention"].astype(float).astype(int)

# Create stacked bar chart using Plotly
fig = px.bar(
    df_filtered, 
    x="Age Group", 
    y=["Retention", "Attrition"], 
    title="Attrition vs Retention Across Age Groups",
    labels={"value": "Employee Count", "variable": "Category"},
    color_discrete_map={"Retention": "black", "Attrition": "tan"},
    barmode="stack"
)

fig.show()

