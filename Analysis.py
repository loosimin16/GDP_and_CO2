import pandas as pd
from matplotlib import style
import seaborn.objects as so
import seaborn as sns

df = pd.read_csv("wdi_small_tidy_2015.txt")

print(df.columns)
df2 = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

# Plot mortality against GDP per capita
chart = (
    so.Plot(
        df2,
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, infant (per 1,000 live births)",
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="GDP against Infant Mortality")
).show()

chart
