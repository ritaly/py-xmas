from datetime import datetime

# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)



#let's say to "user gimme data in format day-month-year & time"
user_input = '03-10-2019 13:00'

input_to_date = datetime.strptime(user_input, '%d-%m-%Y %H:%M')
print('typ: ', type(input_to_date))
print('user_input:', user_input)
print('input_to_date:',input_to_date)

date_to_timestamp =  datetime.timestamp(input_to_date)
print("timestamp =", date_to_timestamp)


#let's say to user "gimme data in format day-month-year"
user_input = '03-10-2019'

input_to_date = datetime.strptime(user_input, '%d-%m-%Y')
print('typ: ', type(input_to_date))
print('user_input:', user_input)
print('input_to_date:',input_to_date)

date_to_timestamp =  datetime.timestamp(input_to_date)
print("timestamp =", date_to_timestamp)