import pandas as pd
import matplotlib.pyplot as plt

# Data for BioArctic
BAdata_SEK = {
    "Revenue (kSEK)": [140706, 713970, 281772, 62347, 23146, 228291, 615995, 257352],
    "Operating_income (kSEK)": [159750, 730229, 296598, 65943, 26688, 229861, 620077, 257352],
    "Net_income (kSEK)": [15157, 381602, 88468, -68517, -119789, -11179, 229249, -177079],
    "Operating_cash_flow (kSEK)": [-135327, -200057, 327165, -92341, -140457, -31638, 309694, -316332],
    "investing_cash_flow (kSEK)": [-2813, -3080, -3273, -12524, -4412, -12763, -507485, 205633],
    "financing_cash_flow (kSEK)": [560218, 0, -138506, -6598, -7389, -2808, 14064, 5686],
    "cash_and_equivalents (kSEK)": [1110367, 917307, 1112770, 999940, 848405, 805386, 611567, 512927],
}
years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

BAdf_SEK = pd.DataFrame(BAdata_SEK, index=years)
print(f'BioArctic Financial Data (kSEK):\n{BAdf_SEK}')

# Calculate additional financial metrics
BAdf_SEK['Profit_Margin'] = (BAdf_SEK['Net_income (kSEK)'] / BAdf_SEK['Revenue (kSEK)']) * 100
BAdf_SEK['Cash_Burn_Rate'] = BAdf_SEK['Operating_cash_flow (kSEK)'] + BAdf_SEK['investing_cash_flow (kSEK)']
BAdf_SEK['R&D_Spending (kSEK)'] = BAdf_SEK['Operating_income (kSEK)'] - BAdf_SEK['Net_income (kSEK)']

metrics_df = BAdf_SEK[['Profit_Margin', 'Cash_Burn_Rate', 'R&D_Spending (kSEK)']]
print(f'\nAdditional Metrics:\n{metrics_df}')

# Revenue Growth Rate
revenue_growth = BAdf_SEK['Revenue (kSEK)'].pct_change() * 100
print(f'\nRevenue Growth Rate:\n{revenue_growth}')

# Plotting Revenue and Net Income over the years
BAdf_SEK.plot.line(y=['Revenue (kSEK)', 'Net_income (kSEK)'], color=["blue", "red"],
                   title='BioArctic Revenue and Net Income Over Years')

# Graph plots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Revenue vs R&D Spending
axes[0, 0].plot(BAdf_SEK.index, BAdf_SEK['Revenue (kSEK)'], marker='o', label='Revenue(kSEK)')
axes[0, 0].plot(BAdf_SEK.index, BAdf_SEK['R&D_Spending (kSEK)'], marker='s', label='R&D Spending(kSEK)')
axes[0, 0].set_title('Revenue vs R&D Investment')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Cash flow analysis
axes[0, 1].bar(BAdf_SEK.index, BAdf_SEK['Operating_cash_flow (kSEK)'], label='Operating CF(kSEK)')
axes[0, 1].set_title('Cash Flow Trends(SEK)')
axes[0, 1].legend()

# Profitability
axes[1, 0].plot(BAdf_SEK.index, BAdf_SEK['Profit_Margin'], marker='o', color='green')
axes[1, 0].set_title('Profit Margin %')
axes[1, 0].axhline(y=0, color='r', linestyle='--')

# Cash position
axes[1, 1].fill_between(BAdf_SEK.index, BAdf_SEK['cash_and_equivalents (kSEK)'], alpha=0.3)
axes[1, 1].plot(BAdf_SEK.index, BAdf_SEK['cash_and_equivalents (kSEK)'], marker='o')
axes[1, 1].set_title('Cash & Equivalents')

plt.tight_layout()
plt.show()