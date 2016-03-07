# The below algorithm is called Zeller's congruence for the Gregorian calendar that is used in Greece.
# For more info about the algorithm see https://en.wikipedia.org/wiki/Zeller's_congruence

input_date = input('Enter a date in format dd/mm/yyyy: ')

input_day = int(input_date[0:2])
input_month = int(input_date[3:5])
input_year = int(input_date[6:10])
days =['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
leapyear = 0
if (input_year % 4) == 0:
    if (input_year % 100) == 0:
        if (input_year % 400) == 0:
           # print("{0} is a leap year".format(year))
           leapyear = 1
        else:
            #print("{0} is not a leap year".format(year))
            leapyear = 0
    else:
         # print("{0} is a leap year".format(year))
         leapyear = 1

else:
    #print("{0} is not a leap year".format(year))
    leapyear = 0

if (leapyear == 0 and input_month == 2 and input_day == 29):
    print('This year is not leap "Invalid Input Date" ')
elif (input_day > 31 or input_month > 12 or input_year > 9999):
    print ('Invalid Input Date!') 
else:
    if input_month<3:
        input_month=input_month+12
        input_year=input_year-1
    day=((input_day + ((26*(input_month+1))//10) + input_year + (input_year//4) + 6*(input_year//100) + (input_year//400))%7)
    print (input_date, 'is :', days[int(day)])
