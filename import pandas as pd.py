import pandas as pd
import statsmodels.api as sm

# Read the data from Excel file
file_path = r'C:\Users\SkeenRH24\Downloads\Restaurant Revenue.xlsx'
data = pd.read_excel(file_path)

# Define independent variables (features)
X = data[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 
          'Average_Customer_Spending', 'Promotions', 'Reviews']]

# Add constant term for the intercept
X = sm.add_constant(X)

# Define dependent variable (target)
y = data['Monthly_Revenue']

# Fit multiple linear regression model
model = sm.OLS(y, X).fit()

# Print regression results
print(model.summary())
print("Go Brewers")
