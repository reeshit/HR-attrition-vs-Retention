import pandas as pd
import plotly.graph_objects as go

# manual data
data = {
    "Education Level": [
        "Bachelor's Degree", "Bachelor's Degree",
        "Master's Degree", "Master's Degree",
        "Associates Degree", "Associates Degree",
        "High School", "High School",
        "Doctoral Degree", "Doctoral Degree"
    ],
    "Category": [
        "Attrition", "Retention",
        "Attrition", "Retention",
        "Attrition", "Retention",
        "Attrition", "Retention",
        "Attrition", "Retention"
    ],
    "Employee Count": [
        99, 473,
        58, 340,
        44, 238,
        31, 139,
        5, 43
    ]
}


df = pd.DataFrame(data)


df["Category"] = df["Category"].str.strip()

# Pivot table for proper grouping
df_pivot = df.pivot(index="Education Level", columns="Category", values="Employee Count").reset_index()


df_pivot.columns = df_pivot.columns.str.strip()


fig = go.Figure()

# Add bars for Retention
fig.add_trace(go.Bar(
    x=df_pivot["Education Level"],
    y=df_pivot["Retention"],
    name="Retention",
    marker=dict(color="black")
))

# Add bars for Attrition
fig.add_trace(go.Bar(
    x=df_pivot["Education Level"],
    y=df_pivot["Attrition"],
    name="Attrition",
    marker=dict(color="tan")
))

# Update layout for grouped bars
fig.update_layout(
    title="Education Level vs Attrition & Retention",
    barmode="group",  
    xaxis_title="Education Level",
    yaxis_title="Employee Count",
    template="simple_white"
)


fig.show()
