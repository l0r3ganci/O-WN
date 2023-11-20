#LABORATORIO 02
#pandas
import csv

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales_data.csv')
profit_list=df['total_profit'].values
months=df('month_number').values
plt.figure()
plt.plot(months,profit_list,label='Mont-wise profit data of last year')
plt.xlabel('month number')
plt.ylabel('profit[$]')
plt.xticks('Month')
plt.title('Compan profit per month')
plt.show()




