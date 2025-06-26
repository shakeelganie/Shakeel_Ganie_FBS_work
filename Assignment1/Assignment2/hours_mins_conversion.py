# conversion of time entered in hh, mm and sec into seconds

hh=int(input("Enter the number of hours: "))
mm=int(input("Enter the numbers of minutes: "))
sec=int(input("Enter the numbers of seconds: "))
hour_seconds=hh*3600
minutes_second=mm*60
seconds_seconds=sec
total_seconds=hour_seconds+minutes_second+seconds_seconds
print("Total seconds: ",total_seconds)

