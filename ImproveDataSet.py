import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'Transaction_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Store_ID': [101, 101, 101, 999, 101, 101, 101, 999],
    'Transaction_Date': ['2023-10-10', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-17', '2023-10-17', '2023-10-18', '2023-10-19'], 
    'Product_Category': ['Iced Products', 'Hot Lattes', 'Iced Products', 'Hot Lattes', 'Iced Products', 'Hot Lattes', 'Hot Lattes', 'Iced Products'],
    'Weather_Condition': ['Rainy', np.nan, 'Clear', 'Clear', 'Rainy', 'Rainy', 'Clear', np.nan], 
    'Daily_Revenue': [15.0, 45.0, 50.0, -10.0, 12.0, 60.0, 40.0, -5.0] 
}

df = pd.DataFrame(data)
print("--- Temizlenmemiş Ham Veri ---")
print(df.head())


df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
df['Day_of_Week'] = df['Transaction_Date'].dt.day_name()

df['Weather_Condition'] = df['Weather_Condition'].fillna('Clear')

df_clean = df[(df['Store_ID'] != 999) & (df['Daily_Revenue'] > 0)].copy()

print("\n--- Temizlenmiş ve Zenginleştirilmiş Veri (ETL Sonrası) ---")
print(df_clean.head())


plt.figure(figsize=(8, 5))
sns.barplot(data=df_clean, x='Weather_Condition', y='Daily_Revenue', hue='Product_Category', palette='Set2')
plt.title('Chart 1: Revenue by Weather Condition & Product Category', fontsize=14)
plt.ylabel('Daily Revenue ($)')
plt.xlabel('Weather Condition')
plt.show()

tuesdays = df_clean[df_clean['Day_of_Week'] == 'Tuesday']

plt.figure(figsize=(8, 5))
tuesday_sales = tuesdays.groupby(['Transaction_Date', 'Product_Category'])['Daily_Revenue'].sum().unstack()
tuesday_sales.plot(kind='line', marker='o', figsize=(8,5), colormap='coolwarm')

plt.title("Chart 2: Sales Velocity on Rainy Tuesdays", fontsize=14)
plt.ylabel("Revenue ($)")
plt.xlabel("Date (Tuesdays)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Product Category")
plt.show()  