# tip calculator App
# float division (//) : divide two numbers and return the result after rounding off to its nearest value (ie. remove the float values)

meal_Amount=float(input('Enter the meal amount: $'))
# converting percentage into decimal 
tip_Percentage=float(input('Enter the tip amount (in %) '))/100
# to add an extra line
print('\n')
print('\n')
print('\n')
print('-----------------------------------')
print(f'Food Amount: ${meal_Amount}')
tip_Amount= meal_Amount*tip_Percentage
print(f'Tip Amount: ${tip_Amount}')
total_Amount=meal_Amount+tip_Amount
# to add an extra line
print('\n')
print(f'Total pay: ${str(total_Amount)}')
print('-----------------------------------')

