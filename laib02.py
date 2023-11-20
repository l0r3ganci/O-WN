#LABORATORIO 02
#pandas

#ES1
#lettura file csv di un azienda con plot di diversi grafici
#plot,scatter,bar,hist,  f,axs=plt.subplots()
import pandas as pd
import matplotlib.pyplot as plt
import json5 as js

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

#1 convert a json_obj in a python obj

json_obj='{"Name":"David","Class"="I","Age":6}'
python_obj=js.load(json_obj)
print('\n Name > ', python_obj['Name'])
print('\nClass > ', python_obj['Class'])
print('\nAge > ',python_obj['Age'])

#2 convert a python obj in a json data

python_ob={
   'name':'David',
    'class':'i',
    'age': 6
}
j_data=js.dumps(python_ob)
print(type(python_ob))
print('\nJson data : ', j_data)

#3 convert python objs in a JSON strings

python_dict = { 'name': 'David' , 'age' : 6 , 'class': 'I'}
python_list = [ 'Red' , 'Green' , 'Black']
python_str = 'Python Json'
python_int = 1234
python_float = 21.34
python_t = True
python_f = False
python_n = None
json_dict=js.dumps(python_dict)
json_list=js.dumps(python_list)
json_str=js.dumps(python_str)
json_num1=js.dumps(python_int)
json_num2=js.dumps(python_float)
json_t=js.dumps(python_t)
json_f=js.dumps(python_f)
json_n=js.dumps(python_n)

print ( 'json dict :' , json_dict )
print ( 'jason list :' , json_list )
print ( 'json string :' , json_str )
print ( 'json number1 :' , json_num1 )
print ( 'json number2 : ' , json_num2 )
print ( 'json true : ', json_t )
print ( 'json false : ' , json_f )
print ( 'json null : ' , json_n )

#4 convert Python dictonary to Json data
# sort by key and print the object members with indent level 4

j_str = {'4':5,'6':7,'1':3,'2':4}
print('Original String ',j_str)
print('\nJson data: ')
print(js.dumps(j_str,sort_key=True, indent=4))

#5 write a python programm to create a json file from an existing Json file


with open('states.json') as f:
    state_data=js.load()
    print('\nOriginal JSON keys: ',
          [state.keys() for state in state_data['states']][0])
for state in state_data['states'] :
    del state['area_codes']
with open('new_state.json','w') as f:
    js.dumps(state_data,f,indent=2)
with open('new_state.json') as f:
    state_data=js.load(f)
print('\nReload JSON keys', [state.keys()
      for state in state_data['states']][0])
