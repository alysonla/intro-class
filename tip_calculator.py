# Write a function called calculate_tip that has one parameter: total_bill. calculate_tip should return 20% of the total_bill.
def calculate_tip(total_bill):
  tip = total_bill * .2
  return tip

print "%.2f" % calculate_tip(42.50)

# Write a function called calculate_tip2 that has two parameters: total_bill and tip_percent. calculate_tip2 should return the total_bill*tip_percent.
def calculate_tip2(total_bill, tip_percent):
  tip = total_bill * tip_percent
  return tip

print "%.2f" % calculate_tip2(42.50, .2)

#Write a function called tips_with_friends that has three parameters: total_bill, tip_percent, and num_friends. tips_with_friends should return (total_bill*tip_percent)/num_friends.
def tip_with_friends(total_bill, tip_percent, num_friends):
    tip = (total_bill*tip_percent)/num_friends
    return tip

print "Each person should pay $",tip_with_friends(42.50, .2, 2)


