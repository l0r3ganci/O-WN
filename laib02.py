#LABORATORIO 02
#pandas

#ES1
#lettura file csv di un azienda con plot di diversi grafici
#plot,scatter,bar,hist,  f,axs=plt.subplots()
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales_data.csv')
df.head()
profit_list=df['total_profit'].values
months=df['month_number'].values
plt.figure('fig1')
plt.plot(months,profit_list,label='Mont-wise profit data of last year')
plt.xlabel('month number')
plt.ylabel('profit[$]')
plt.title('Company profit per month')
plt . yticks ([100e3 , 200e3 , 300e3 , 400e3 , 500e3 ])
plt.show()

#ES2
plt.figure('fig2')
plt.plot(months,profit_list,label='profit data of the year',color='r',
         marker='o',markerfacecolor='k', linestyle='--',linewidth=3)
plt.xlabel('Month number')
plt.ylabel('profit in dollar')
plt.title('Company sales of last year')
plt.show()

#ES3

facecream_list=df['facecream'].values
facewash_list=df['facewash'].values
toothpaste_list=df['toothpaste'].values
bathingsoap_list=df['bathingsoap'].values
shampoo_list=df['shampoo'].values
moisturizer_list=df['moisturizer'].values
plt . figure ()
plt . plot ( months , facecream_list, label = ' Face cream Sales Data ' , color='r', linewidth =3)
plt . plot ( months , facewash_list, label = ' Face wash Sales Data ' , color='g',marker = 'o' , linewidth =3)
plt . plot ( months , toothpaste_list ,label = ' ToothPaste Sales Data ' , color='y',marker ='o' , linewidth =3)
plt . plot ( months , bathingsoap_list ,label = ' Bathing Soap Sales Data ' ,color='b', marker = 'o' , linewidth =3)
plt . plot ( months , shampoo_list ,label = 'Shampoo Sales Data ',color='c',marker = 'o', linewidth =3)
plt . plot ( months , moisturizer_list,label = 'Moisturizer Sales Data ' ,color='m', marker = 'o' , linewidth =3)
plt.xlabel('Month number')
plt.ylabel('Sales units number')
plt.title('Sales data')
plt.show()

#ES4

plt.figure('figure 4')
plt.scatter(months,toothpaste_list,label='toothpaste sales data')
plt.xlabel('Month numbers')
plt.ylabel('Number of units sold')
plt.title('Toothpaste sales data')
plt.grid(True,linewidth=0.5,linestyle='--')
plt.show()

#ES5 bathing soap bar plot

plt.bar(months,bathingsoap_list)
plt.xlabel('Month numbers')
plt.ylabel('bathingsoap sales data sold')
plt.grid(True,linewidth=0.5,linestyle='--')
plt.title('bathing soap sales data')
plt.savefig('sales_data_of_bathng_soap.png',dpi=150)
plt.show()

#ES6 total profit histogram

profit_range=[150e3 , 175e3 , 200e3 , 225e3 , 250e3 , 300e3 , 350e3 ]
plt.hist(profit_list,profit_range,label='Profit data')
plt.xlabel('profit range [$]')
plt.ylabel('actual profit [$]')
plt.title('Profit data')
plt.savefig('sales_data_profit_histogram.png', dpi=150)
plt.show()

#ES7

f , axs = plt . subplots (2 , 1 , sharex = True )
axs [0]. plot ( months, bathingsoap_list , label = 'Bathing soap Sales Data' ,
color ='k', marker = 'o' , linewidth =3)
axs [0]. set_title ( 'Sales data of a Bathing soap ')
axs [0]. grid ( True , linewidth =0.5 , linestyle = '--')
axs [0]. legend ()
axs [1]. plot ( months , facewash_list , label =  'Face Wash Sales Data',
color = 'r' , marker = 'o' , linewidth =3)
axs [1]. set_title ( 'Sales data of a face wash')
axs [1]. grid ( True , linewidth =0.5 , linestyle = '--')
axs [1]. legend ()
plt . xticks ( months )
plt . xlabel ( 'Month Number')
plt . ylabel ( 'Sales units in number ')
plt . show()

#ES2
#lettura file JSON

