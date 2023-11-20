import numpy as np
#OPEN AND VIRTUAIZED NETWORK
#LABORATORIO 01
#PARTE 1
#ES1
i1=int(input("Input the left limit range number: "))
antsum=0
currsum=0
for i in range(i1):
    antsum=currsum
    currsum=antsum+i
    print("somma antecedenti, somma attuale :",antsum,currsum)

#ES2
num1=int(input("Insert  first number :"))
num2=int(input("Insert second number: "))
product=num1*num2
if product>1000:
    result=product
else :
    result=num1+num2
print("The result is:", result)

#ES3
num_list=[10,20,30,40,10]
if num_list[0]==num_list[-1] :
    result=True
else:
    result=False
print(result)

#ES4

num_list2=[10,20,40,34,32,15,6,5]
for num in num_list2 :
    if num%5 ==0 :
        print(num)

#ES5

statement="Emma is a good developer. Emma is also a writer"
cnt=statement.count('Emma')
print("Emma appeared: ",cnt)

#ES6

list1=[10,20,23,11,17]
list2=[13,43,24,36,12]
list3=[]
for num in list1:
    if num%2!=0 :
        list3.append(num)
for num in list2:
    if num%2 == 0 :
        list3.append(num)
print("The merge list is : ", list3)

#ES7

s1='OpenNets'
s2='Optical'
middle_index=int(len(s1)/2)
print("Original Strinf are> ",s1,s2)
s3=s1[:middle_index]+s2+s1[middle_index:]
print('\nAfter appending the new string in the middle: ', s3)

#ES8

S1='America'
S2='Japan'
len1=len(S1)
len2=len(S2)
S3=(s1[:1]+s1[int(len1/2):int(len1/2)+1]+s1[len1-1]+s2[:1]+
    s2[int(len2/2):int(len2/2)+1]+s1[len2-1])
print(S3)

#ES9

print('Total count of chars, digit, and symbols >>')
input_string='P@yn26at>#4fiv35'
char_count=0
digit_count=0
symbols_count=0
for c in input_string:
    if c.islower() or c.isupper():
        char_count+=1
    if c.isnumeric():
        digit_count+=1
    else :
        symbols_count+=1
print(f'Chars={char_count}\tDigits={digit_count}\tSymbols={symbols_count}')

#ES10

input_str='Welcome to USA, Awesome usa, isn\'t it'
substr='USA'
tmp_str=input_str.lower()
tmp_cmp=substr.lower()
cnt1=tmp_str.count(tmp_cmp)
print(f'The {substr} count is: ',cnt1)

#ES11

str1='pynativepynvepynative'
sum=0
ln=len(str1)
for c in str1 :
    sum+=int(c)
average=sum/ln
print(f'The average of the sum of chars is : ',average)

#ES12

str1='pynativepynvepynative'
count_dict=dict()
for cha in str1:
    coun = str.count(cha)
    count_dict[cha]=coun
print(count_dict)

#PARTE2
#ESB3

sampleList=[11,45,8,23,14,12,78,45,89]
print('Original list > ', sampleList)
length=len(sampleList)
chuck_length=int(length/3)
start=0
end=chuck_length
for i in range (1,chuck_length+1):
    indexes=slice(start,end,1)
    list_ch=sampleList[indexes]
    print('chunk',i,list_ch)
    print('After reversing it ', list(reversed(list_ch)))
    start=end
    if i<chuck_length :
        end+=chuck_length
    else :
        end+=length-chuck_length

#ESB4

sampleTest=[11,45,8,11,45,23,45,89]
print('Original list', sampleTest)
count_dict1=dict()
for item in sampleTest :
    if item in count_dict1:
        count_dict1[item]+=1
    else :
        count_dict1[item]=1
print('Printing count of each item ', count_dict1)

#ESB5

firstList=[2,3,4,5,6,7,8,9]
secondList=[4,9,26,25,36,49,64]
result2=zip(firstList,secondList)
result_set=set(result2)
print(result_set)

#ESB6

first={23,42,65,57,78,83,29}
second={57,83,29,67,73,43,48}
intersection=first.intersection(second)
for item in intersection :
    first.remove(item)

#ESB7

rollNumber=[47,64,69,37,76,83,95,97]
dict_1={'Jhon':47,'Emma': 69,'Kelly': 76, 'Jason': 97 }

for i in range(len(rollNumber)):
    if rollNumber[i] in dict_1.values() :
        rollNumber.remove(i)

#ESB8

speed={'jan': 47,'feb': 52,'march': 47,'april': 44, 'May': 52, 'June': 54, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_list=[]
for item in speed.values():
    if  item not in speed_list :
        speed_list.append(item)

#SEB8

samList=[87,52,44,53,54,87,52,53]
print('Original list', samList)
tup =list(set(samList))
print('Tuple', tup)
print('Minimum number is :', min(tup))
print('Maximum number is :', max(tup))

#PARTE3
#ESC1

arr=np.empty((4,2),dtype=np.int16)
print('Printing array')
print(arr)
print('\n printing numpy array attributes')
print('1- Array shape',arr.shape)
print('2- Array dimension are ',arr.ndim)
print('3- Length of each element of array in bytes is ',arr.itemsize)

#ESC2

s_arr=np.arange(100,200,10)
s_arr=s_arr.reshape(5,2)
print(s_arr)

#ESC3

sa_arr=np.array([[11,22,33],[44,55,66],[77,88,99]])
print('Input array \n ' )
print(sa_arr)
arrs=sa_arr[:,2]
print('The tird column of array is ')
print(arrs)

#ESC4

sam=np.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])
print('Input array ')
print(sam)
print('Odd rows and even columns')
print(sam[::2][1::2])

#ESC5

amp1=np.array([[5, 6, 9], [21 ,18, 27]])
amp2=np.array([[15 ,33, 24], [4 ,7, 1]])
amp1+=amp2
m,n=amp1.shape()
result=np.array(amp1.shape)
j=0
i=0
for elm in amp1[::,::]:
    if i<m :
        if j>= n:
            i+=1
            j=0
        result[i][j]=np.sqrt(elm)
        j+=1

#ESC6

ample_array = np . array ([[34 , 43 , 73] , [82 , 22 , 12] , [53 , 94 , 66]])
line_array=ample_array.reshape(1, np.prod(ample_array))
sort_list_array=np.sort(line_array)
print('\n sorted array: ')
print(sort_list_array)

#ESC7

sample_array3 = np . array ([[34 , 43 , 73] , [82 , 22 , 12] , [53 , 94 , 66]])
print ( 'Printing Original array')
print ( sample_array3 )
min_of_axis1 = np . amin ( sample_array3 , 1)
print ('\ nPrinting amin Of Axis 1 ')
print ( min_of_axis1 )
max_of_axis1 = np . amax ( sample_array3 , 0)
print ( 'Printing amax Of Axis 1 ')
print ( max_of_axis1)

#ESC8

sample_array_new = np . array ([[34 , 43 , 73] , [82 , 22 , 12] , [53 , 94 , 66]])
print ( 'Printing Original array ')
print ( sample_array_new )
print ( 'Array after deleting column 2 on axis 1 ')
sample_array_new=np.delete(sample_array_new,1,axis=1)
sample_array_new=np.insert(sample_array_new,1,axis=1)
print('Array after inserting column 2 in axis 1')
print(sample_array_new)





