import plotly.graph_objects as go

data = [
    {"Job Title": "Data Visualization Technician", "Attrition": 62, "Retention": 197},
    {"Job Title": "Sales Executive", "Attrition": 57, "Retention": 269},
    {"Job Title": "Research Scientist", "Attrition": 47, "Retention": 245},
    {"Job Title": "Sales Representative", "Attrition": 33, "Retention": 50},
    {"Job Title": "Human Resources", "Attrition": 12, "Retention": 40},
]

# Create a list of dictionaries, where each dictionary represents a row
rows = []
for item in data:
    rows.append(
        dict(
            Job_Title=item["Job Title"],
            Attrition=item["Attrition"],
            Retention=item["Retention"],
        )
    )

# Create the table using Plotly's `Table` trace
fig = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=["Job Title", "Attrition", "Retention"],
                align=["left", "center", "center"],  # Align columns
                font=dict(color="black", size=14),  # Style header font
                fill=dict(color="#eee"),  # Light gray header background
            ),
            cells=dict(
                values=[
                    [row["Job_Title"] for row in rows],
                    [row["Attrition"] for row in rows],
                    [row["Retention"] for row in rows],
                ],
                align=["left", "center", "center"],  # Align columns
                font=dict(color="black", size=12),  # Style cell font
                height=30,  # Set row height for spacing
                fill=dict(color=[["white", "#f2f2f2"] * len(data)]),  # Alternate row colors
            ),
        )
    ]
)


# Improve table layout for better appearance
fig.update_layout(
    title="Employee Data",
    title_x=0.5,  # Center the title
    title_font=dict(size=18),
    margin=dict(l=20, r=20, t=50, b=20),  # Adjust margins
    height=400,  # Set a fixed height if needed
    width=800, # Set a fixed width if needed
)


fig.show()