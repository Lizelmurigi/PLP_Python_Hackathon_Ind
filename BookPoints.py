book_purchase = int(input("Hey, how many books did you purchase this month?" ))

if book_purchase == 0:
  print("You have earned 0 points")

elif book_purchase == 1:
  print("You have earned 6 points!")

elif book_purchase == 2:
  print("You have earned 16 points!")

elif book_purchase == 3:
  print("You have earned 32 points!")

elif book_purchase >= 4:
  print("You have earned 60 points!")

else:
  print("Number of books can't be negative")