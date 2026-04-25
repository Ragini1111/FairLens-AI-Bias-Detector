import pandas as pd
import matplotlib.pyplot as plt
from fairlearn.metrics import demographic_parity_difference

print("Loading data...")
df = pd.read_csv('german_credit_data.csv')

# Create age groups for bias testing
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 35 else 'Old')

# Fake biased AI: Favors men + young people
df['loan_approved'] = df.apply(lambda row: 
    1 if row['Credit amount'] > 1500 and row['Sex'] == 'male' and row['Age_Group'] == 'Young'
    else 1 if row['Credit amount'] > 2500 and row['Sex'] == 'male' and row['Age_Group'] == 'Old'
    else 1 if row['Credit amount'] > 3500 and row['Sex'] == 'female' and row['Age_Group'] == 'Young'
    else 1 if row['Credit amount'] > 5000 and row['Sex'] == 'female' and row['Age_Group'] == 'Old'
    else 0, axis=1)

print("Calculating bias...")
gender_bias = demographic_parity_difference(
    y_true=df['loan_approved'], y_pred=df['loan_approved'], sensitive_features=df['Sex']
)
age_bias = demographic_parity_difference(
    y_true=df['loan_approved'], y_pred=df['loan_approved'], sensitive_features=df['Age_Group']
)

print(f"\n=== BIAS REPORT ===")
print(f"Gender Bias Score: {gender_bias:.2f}")
print(f"Age Bias Score: {age_bias:.2f}")

if abs(gender_bias) > 0.1 or abs(age_bias) > 0.1:
    print("HIGH RISK – Model discriminates by gender and/or age")
else:
    print("LOW RISK – Model looks fair")

# Charts for judges
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gender chart
gender_rates = df.groupby('Sex')['loan_approved'].mean() * 100
ax1.bar(gender_rates.index, gender_rates.values, color=['#2E86C1', '#E74C3C'])
ax1.set_title(f'Gender Bias: {gender_bias:.2f}', fontweight='bold')
ax1.set_ylabel('Approval Rate (%)')
ax1.set_ylim(0, 100)
for i, v in enumerate(gender_rates.values):
    ax1.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')

# Age chart  
age_rates = df.groupby('Age_Group')['loan_approved'].mean() * 100
ax2.bar(age_rates.index, age_rates.values, color=['#27AE60', '#F39C12'])
ax2.set_title(f'Age Bias: {age_bias:.2f}', fontweight='bold')
ax2.set_ylabel('Approval Rate (%)')
ax2.set_ylim(0, 100)
for i, v in enumerate(age_rates.values):
    ax2.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')

plt.suptitle('FairLens: AI Bias Detection - Gender + Age', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('bias_chart.png', dpi=300)
print("\nChart saved as 'bias_chart.png'")
plt.show()