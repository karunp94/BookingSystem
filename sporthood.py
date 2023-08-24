#ENTER YOUR OWN PASSWORD
#OPEN SQL AND CREATE DATABASE CALLED 'grounds' AND A TABLE CALLED 'grounds'
#copy this for sql: create database grounds;    and then 
#use grounds;
#create table grounds and then run this 

import sys
from datetime import date


import mysql.connector as mysqltor
mycon=mysqltor.connect(host='localhost',user='root',passwd='crash123',database='grounds')
if mycon.is_connected():
    print('yes')
else:
    print('no')



cursor=mycon.cursor()

numbers = [1,2,3,4,5,6,7,8,9,10]
NAMES = [ "Turf Park", "Velo CT", "Simba Sports", "Play Arena", "Green Park",'Cult Sports','Bull Ring','Kicks On Grass','Falcon Sports','Rex Sports']
ADDRESS = [ "HSR Layout", "HSR Layout", "Sarjapur Road", "Sarjapur Road", "MG Road",'MG Road','Whitefield','Whitefield','Silkboard','Silkboard']
FEES=[1500,700,900,600,1800,850,700,1200,1250,1100]
CAPACITY=['5X5','11X11','7X7','8X8','9X9','4x4','5x5','10x10','9x9','8x8']
No = [9632445772, 9108526754, 9986533456, 9972473453, 9263450090,9021370900,8790191163,7103997632,9921378090,7108325742]
NUM=[201,202,203,204,205,206,207,208,209,210]
for i in range(0,10) :
    a1 = numbers[i]
    a2 = NAMES[i]
    a3 = ADDRESS[i]
    a4 = FEES[i]
    a5 = CAPACITY[i]
    a6 = No[i]
    a7 =NUM[i]
    str2 = "INSERT INTO grounds(Sno, NAME, ADDRESS,FEES,CAPACITY,CONTACT,Ground_ID) VALUES({}, '{}', '{}', {},'{}',{},{})".format(a1,a2,a3,a4,a5,a6,a7)
    cursor.execute(str2)
    mycon.commit()
print('*************************************************************************************************************************************************')
print('                                                   SPORTHOOD GROUND BOOKING SERVICES')
print('*************************************************************************************************************************************************')
print()
print('WELCOME TO SPORTHOOD GROUND BOOKING SERVICES!!!!')
print()
print('Here are the list of locations in Bangalore where our services are provided:')
print(


    )
code=['LOCATION       :PIN','HSR Layout     :101','Sarjapur Road  :102','MG Road        :103','Whitefield     :104','Silkboard      :105']
for i in code:
    print(i)
print(


    )
print('Enter pin of desired booking location from the list above.   ')
location=int(input('Choose your pin from above:  '))
if location ==101:
    print(





        )
    print('Given below are the details of grounds in HSR Layout:')
    print(

        )
    cursor.execute('select * from grounds where (Sno=1 or Sno=2)')
    data=cursor.fetchall()
    for i in data:
        print(i)
    print(



        )
    print('Choose your desired ground after reading through the details.')
    
    num1=int(input('Enter your ground code(last coloumn of above table):   '))
    print(



        )
    while num1:
        if num1==201:
            print('Thank You for choosing Turf Park.')
            break
        elif num1==202:
            print('Thank You for choosing Velo Ct.')
            break
        else:
            print('''          ERROR!!!
          Please enter a valid ground code''')
            print()
            num1=int(input('Enter your ground code(last coloumn of above table):   '))
    

elif location ==102:
    print(






        )
    print('Given below are the details of grounds in Sarjapur Road:')
    print(

        )
    cursor.execute('select * from grounds where (Sno=3 or Sno=4)')
    data=cursor.fetchall()
    for i in data:
        print(i)
    print(




        )
    print('Choose your desired ground after reading through the details.')
    
    num1=int(input('Enter your ground code(last coloumn of above table):   '))
    print(



        )
    while num1:
        if num1==203:
            print('Thank You for choosing Simba Sports.')
            break
        elif num1==204:
            print('Thank You for choosing Play Arena.')
            break
        else:
            print('''          ERROR!!!
          Please enter a valid ground code''')
            print()
            num1=int(input('Enter your ground code(last coloumn of above table):   '))
   




elif location ==103:
    print(



        )
    print('Given below are the details of grounds in MG Road: ')
    print(

        )
    cursor.execute('select * from grounds where (Sno=5 or Sno=6)')
    data=cursor.fetchall()
    for i in data:
        
        print(i)
    print(



        )
    print('Choose your desired ground after reading through the details.')
    
    num1=int(input('Enter your ground code(last coloumn of above table):   '))
    print(


        )
    while num1:
        if num1==205:
            print('Thank You for choosing Green Park.')
            break
        
        elif num1==206:
            print('Thank You for choosing Cult Sports.')
            break
        else:
            print('''            ERROR!!!
          Please enter a valid ground code''')
            print()
            num1=int(input('Enter your ground code(last coloumn of above table):   '))
    




elif location ==104:
    print(



        )
    
    print('Given below are the details of grounds in Whitefield:')
    print(

        )
    cursor.execute('select * from grounds where (Sno=7 or Sno=8)')
    data=cursor.fetchall()
    for i in data:
        
        print(i)
    print(



        )
    print('Choose your desired ground after reading through the details.')
    
    num1=int(input('Enter your ground code(last coloumn of above table):   '))
    print(



        )
    while num1:
        if num1==207:
            print('Thank You for choosing Bull Ring.')
            break
        elif num1==208:
            print('Thank You for choosing Kicks On Grass.')
            break
        else:
            print('''          ERROR!!!
          Please enter a valid ground code''')
            print()
            num1=int(input('Enter your ground code(last coloumn of above table):   '))
        
    
   


elif location ==105:
    print(


        )
    print('Given below are the details of grounds in Silkboard:')
    print(

        )
    cursor.execute('select * from grounds where (Sno=9 or Sno=10)')
    data=cursor.fetchall()
    for i in data:
        print(i)
    print(




        )
    print('Choose your desired ground after reading through the details.')
    
    num1=int(input('Enter your ground code(last coloumn of above table):   '))
    print(

        )
    while num1:
        if num1==209:
            print('Thank You for choosing Falcon Sports.')
            break
        elif num1==210:
            print('Thank You for choosing REX Sports.')
            break
        else:
            print('''          ERROR!!!
          Please enter a valid ground code''')
            print()
            num1=int(input('Enter your ground code(last coloumn of above table):   '))
            
    


   
else:
    print(

        )
    print('''                         ERROR!!!!!!
                        Rerun  Code''')
    str3='delete from grounds'
    cursor.execute(str3)
    mycon.commit()
    sys.exit()



    
    
    

 


print(



    )
dat=date.today()
dat=str(dat)
name=input('Enter name of bookie:  ')
phone=int(input('Enter your 10 digit Whatsapp number:  '))
while phone:
    if len(str(phone))==10:
        break
    else:
        print(

            )
        print('''          ERROR!!!
          Please enter a 10 digit number''')
        print(
            )
        phone=int(input('Enter your 10 digit Whatsapp number:  '))

    




date=input('Enter date of booking in yyyy-mm-dd:')
while date:
    if date>=dat:
        print('Date Accepted')
        break
    else:
        print('''          ERROR!!!
          Please enter a new date as this date is invalid''')
        print(
            )
        date=input('Enter date of booking in yyyy-mm-dd:')

print()
print('Choose you time slot from below:')
print()

time=['TIMINGS:    ','1. MORNING      7:00-8:00','2. MORNING      8:00-9:00','3. EVENING      7:00-8:00','4. EVENING      8:00-9:00']
for i in time:
    print(i)
print(
    )
t=int(input('Enter desired index corresponding to time of booking from above:   '))
while t:
    if t in [1,2,3,4]:
        break
    else:
        print('''          ERROR!!!
          Please enter a valid time slot index from  above''')
        print(
            )
        t=int(input('Enter desired index corresponding to time of booking from above:   '))
        


print(


    )

confer=input('Can we confirm your booking ? Enter y/n   ')
if confer in ['y' , 'Y', 'Yes' , 'yes', 'YES']:
    print(

        )
    
    print('Your booking has been confirmed!!!')
    print()
    print('Booking Name: ',name)
    print('Conact Number: ',phone)
    print('Date of booking:',date)
    print('Time of booking:',time[t])
    print('')
    print('')
elif confer in ['n' , 'N','No', 'no' , 'NO']:
    print(
        )
   
    print('Lets confirm your booking details again.')
    print(
        )
    name=input('Enter name of bookie:  ')
    phone=int(input('Enter your 10 digit Whatsapp number:  '))
    while phone:
        if len(str(phone))==10:
            break
        else:
            print('''          ERROR!!!
          Please enter a 10 digit number''')
            print(
                )
            phone=int(input('Enter your 10 digit Whatsapp number:  '))
    
    
    
    date=input('Enter date of booking in yyyy-mm-dd:')
    while date:
        if date>=dat:
            print('Date Accepted')
            break
        else:
            print('''          ERROR!!!
          Please enter new date as this date is invalid''')
            print(
                )
            date=input('Enter date of booking in yyyy-mm-dd:')
            



    
    print(
        )
    
    print('Choose you time slot from below:')
    print()
    time=['TIMINGS:    ','1. MORNING      7:00-8:00','2. MORNING      8:00-9:00','3. EVENING      7:00-8:00','4. EVENING      8:00-9:00']
    for i in time:
        print(i)
    print(
        )
    t=int(input('Enter desired index corresponding to time of booking from above:   '))
    while t:
        if t in [1,2,3,4]:
            break
        else:
            print('''          ERROR!!!
          Please enter a valid time slot index from  above''')
            print(
                )
            t=int(input('Enter desired index corresponding to time of booking from above:   '))
        
            
                                                        
             
   
   
    print(


        )
    print('Your booking has been confirmed!!!')
    print('Booking Name: ',name)
    print('Conact Number: ',phone)
    print('Date of booking:',date)
    print('Time of booking:',time[t])
    print('')
    print('')
else:
    print(


        )
    print('''          Sorry !!!!!
          Data enterd is invalid
          Your session has been timed out.
          Please rerun the program''')
    str3='delete from grounds'
    cursor.execute(str3)
    mycon.commit()


    sys.exit()



print('GROUND DETAILS:')
cursor.execute('select NAME from grounds where Ground_ID = {}'.format(num1))
gname=cursor.fetchall()
cursor.execute('select ADDRESS from grounds where Ground_ID = {}'.format(num1))
gloc=cursor.fetchall()
cursor.execute('select FEES from grounds where Ground_ID = {}'.format(num1))
gfee=cursor.fetchall()
cursor.execute('select CAPACITY from grounds where Ground_ID = {}'.format(num1))
gcap=cursor.fetchall()
cursor.execute('select CONTACT from grounds where Ground_ID = {}'.format(num1))
gcont=cursor.fetchall()

print('Ground Name: ',gname)
print('Ground Location: ',gloc)
print('Ground Capacity : ',gcap)
print('Fees per hour : ',gfee)
print('Contact No. : ',gcont)


    
    



         

   


    




print('''
PLEASE NOTE THE FOLLOWING:
1)The location of the ground will be sent within 1 hour of booking to the  whatsapp number provided as above.
2)Please ensure that you reach the ground on time.
3)An otp will be sent to your number 5 mins prior to your time slot.
4)You are to enter the otp on reaching the ground
5)A maximum of 15mins will be provided as buffer for entering the otp. if otp is not entered then the booking made by you will become invalid.
6)Payment to be made by cash,card or by any upi means.
''')


print(



    )



print('ENJOY YOUR GAME!!!!')

str3='delete from grounds'
cursor.execute(str3)
mycon.commit()













    

        
    
        
