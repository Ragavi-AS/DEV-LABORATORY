import pandas as pd

data = {
    'city': ['Delhi','Delhi','Mumbai','Mumbai','Delhi','Mumbai'],
    'date': ['2025-01-03','2025-01-10','2025-02-07','2025-02-14','2025-07-05','2025-07-12'],
    'temperature': [15, 18, 25, 28, 35, 33]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly = df.groupby(['city', 'month'])['temperature'].sum().reset_index()
pivot_monthly = monthly.pivot(index='city', columns='month', values='temperature').fillna(0)

print("Monthly sum pivot:\n", pivot_monthly)

# Check which summer months exist in the data
summer_months = [6, 7, 8]
available_summer = [month for month in summer_months if month in pivot_monthly.columns]

if available_summer:
    pivot_monthly['summer_sum'] = pivot_monthly[available_summer].sum(axis=1)
    top_summer_city = pivot_monthly['summer_sum'].idxmax()
    print(f"City with highest summer temperature sum: {top_summer_city}")
else:
    print("No summer month data available to compute summer temperature sum.")
