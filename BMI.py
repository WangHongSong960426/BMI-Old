kg = float (input ('your weight(KG):  '))
m = float (input ('your height(M): '))
print ('your weight: ', kg, 'your height: ', m)
BMI = kg / (m*m)
print ('your BMI: ', BMI)
if BMI < 18.5: 
	print ('過輕 請多吃點')
if 18.5 <= BMI < 25.0: 
	print ('標準 請維持身材')
if 25.0 <= BMI < 30.0: 
	print ('超重 請多做運動')
if BMI >= 30.0: 
	print ('肥胖 請少吃點')