import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set seaborn style for better aesthetics
sns.set_theme(style="whitegrid")

# Generate sample data
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
regions = ['North', 'South', 'East', 'West']

data = []
for region in regions:
    base_sales = np.random.randint(10000, 30000)
    for month in months:
        sales = base_sales + np.random.randint(-5000, 15000)
        data.append({'Region': region, 'Month': month, 'Sales': sales})

df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(12, 7))

# Create a bar plot
ax = sns.barplot(x='Month', y='Sales', hue='Region', data=df, palette='viridis')

# Customize the plot
plt.title('Monthly Sales Performance by Region (H1)', fontsize=18, pad=20, fontweight='bold', color='#333333')
plt.xlabel('Month', fontsize=14, labelpad=10)
plt.ylabel('Revenue ($)', fontsize=14, labelpad=10)

# Format y-axis ticks
mean_sales = df['Sales'].mean()
plt.yticks(np.arange(0, 50001, 10000), [f'${i:,.0f}' for i in np.arange(0, 50001, 10000)])

# Add value labels on top of bars
for p in ax.patches:
    height = p.get_height()
    if not np.isnan(height) and height > 0:
        ax.text(p.get_x() + p.get_width()/2., height + 1000, 
                f'${int(height/1000)}k', 
                ha='center', va='bottom', fontsize=9, rotation=90)

# Customize legend
plt.legend(title='Region', title_fontsize='12', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))

# Layout adjustment
plt.tight_layout()

# Save the plot
output_path = 'sales_chart.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart successfully saved to {output_path}")
