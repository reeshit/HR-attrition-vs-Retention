import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('Gender.csv', sep="\t", encoding="utf-16")

# Rename columns properly
df.columns = ["Gender", "Category", "% Attrition", "Attrition Count", "Employee Count"]

# Remove empty rows and convert Employee Count to numeric
df = df.dropna(subset=["Employee Count"])
df["Employee Count"] = df["Employee Count"].astype(str).str.strip()
df["Employee Count"] = df["Employee Count"].astype(float).astype(int)

# Separate data for Male and Female
df_female = df[df["Gender"] == "Female"]
df_male = df[df["Gender"] == "Male"]

# Create Donut Chart for Female
fig_female = go.Figure(go.Pie(
    labels=df_female["Category"],
    values=df_female["Employee Count"],
    hole=0.7,  # Creates the donut effect
    marker=dict(colors=["tan", "black"]),  # Custom colors
    textinfo="none"  # Hides labels inside the chart
))

# Add custom labels outside the chart
fig_female.add_annotation(x=0, y=1.1, text="Female", showarrow=False, font=dict(size=16))
fig_female.add_annotation(x=0.4, y=0.2, text=str(df_female[df_female["Category"] == "Attrition"]["Employee Count"].values[0]), showarrow=False, font=dict(size=14, color="tan"))
fig_female.add_annotation(x=0, y=-0.8, text=str(df_female[df_female["Category"] == "Retention"]["Employee Count"].values[0]), showarrow=False, font=dict(size=14))

# Create Donut Chart for Male
fig_male = go.Figure(go.Pie(
    labels=df_male["Category"],
    values=df_male["Employee Count"],
    hole=0.7,
    marker=dict(colors=["tan", "black"]),
    textinfo="none"
))

# Add custom labels outside the chart
fig_male.add_annotation(x=0, y=1.1, text="Male", showarrow=False, font=dict(size=16))
fig_male.add_annotation(x=0.4, y=0.2, text=str(df_male[df_male["Category"] == "Attrition"]["Employee Count"].values[0]), showarrow=False, font=dict(size=14, color="tan"))
fig_male.add_annotation(x=0, y=-0.8, text=str(df_male[df_male["Category"] == "Retention"]["Employee Count"].values[0]), showarrow=False, font=dict(size=14))


fig_female.show()
fig_male.show()
