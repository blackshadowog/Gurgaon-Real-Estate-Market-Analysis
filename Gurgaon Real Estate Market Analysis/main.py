import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

#data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.drop_duplicates()


# numeric columns cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)


# Clean Categorical Columns
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera ": True , "not approved by rera": False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()

# question 1 : which is the costliest flat in the dataset
costliest_flat = df.loc[df['price'].idxmax()]
print(costliest_flat)

print(f"The costliest flat in the dataset is a {costliest_flat['bhk_count']} BHK apartment located in {costliest_flat['locality']}, with an area of {costliest_flat['area']} sqft, priced at {costliest_flat['price']/10000000:.2f} Crores. ")
print(f"It is built by {costliest_flat['builder_name']} and is currently {costliest_flat['status']}. The rate per sqft is {costliest_flat['rate_per_sqft']}, and it is {'approved by RERA' if costliest_flat['rera_approval'] else 'not approved by RERA'}.")

# question 2 : which locality has the highest average price 
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")
print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(20))


# question 3 :Which locality has the highest rate per square foot?
highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")


# question 4 : Do ready-to-move properties cost more than under-construction properties?

ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print(f"Ready-to-move properties cost more on average ({ready_to_move_avg_price:.2f}) than under-construction properties ({under_construction_avg_price:.2f}).")
else:
    print(f"Under-construction properties cost more on average ({under_construction_avg_price:.2f}) than ready-to-move properties ({ready_to_move_avg_price:.2f}).")


# question 5 : Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print("RERA-approved properties command a price premium on average  than non-RERA-approved properties .")
else:
    print("Non-RERA-approved properties command a price premium on average  than RERA-approved properties.")

# question 6 : How does area (sqft) impact property price?
sns.scatterplot(data=df, x='area', y='price')
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price')
plt.savefig("images/area_vs_price.png")
plt.show()

# question 7 : Which BHK configuration is the most expensive based on rate per sqft?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration based on rate per sqft is {most_expensive_bhk}.")

# question 8 : Which property type (Apartment, Floor, Plot) is the costliest?
most_expensive_property_type = df.groupby('property_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest property type based on average price is {most_expensive_property_type}.")


# question 9 : Do certain builders or companies consistently price higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(10)  )
# print top 5 builders name 
print("Top 5 builders with highest average rate per sqft:")
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder, rate in top_5_builders.items():
    print(f"{builder}: {rate:.2f} per sqft")

# question 10 : Are larger homes always more expensive per square foot?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.title('Area vs Rate per Sqft')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Sqft')
plt.savefig("images/area_vs_rate_per_sqft.png", dpi=300)
plt.show()
print("no")

df.to_csv("cleaned_data.csv", index=False)

print("thank you for using this program. The cleaned data has been saved to 'cleaned_data.csv'. author - Abhishek kumar tiwari")