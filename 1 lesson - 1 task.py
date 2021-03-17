number = int(input("Enter duration: "))

if number < 60:
   print(f"{number} second")
elif 60 < number < 3600:
   minute=number//60
   second=number-(60*minute)
   print(f"{minute} minutes, {second} seconds")
elif number >= 3600:
   hour = number // 3600
   minute = ((number-(hour*3600))//60)
   second = (number-(hour*3600))-(minute*60)
   if hour > 24:
      day=hour//24
      hour=hour-day*24
      print(f"{day} days, {hour} hours, {minute} minutes, {second} seconds")
   else:
      print(f"{hour} hours, {minute} minutes, {second} seconds")


