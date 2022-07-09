import time
from datetime import datetime
dt = datetime.now()
date = time.strftime("%Y-%m-%d")
day = time.strftime("%a")
x = dt.isoweekday()




print("Date:", date)
print("Day:", day)


if(x<=5):

  print("Fare:", 100)

elif(x==6):
  print("Fare:", 60)

elif(x==7):
  print("Fare:", 80)