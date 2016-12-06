#create a function tht accepts 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print and add in cheese_count
    print "You have %d cheeses" % cheese_count
    #print and add in boxes_of_crackers
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
#give the function cheese_and_crackers two variables
cheese_and_crackers(20,30)

print "OR we can use variables from our script"
#create a variable called amount_of_cheese and set it to 10
amount_of_cheese = 10
#create a variable called amount_of_crackers and set it to 50
amount_of_crackers = 50

#call the function cheese_and_crackers and take the two variables above as args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#call function cheese_and_crackers and use variables with addition, 30 and 11
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
#call function cheese_and_crackers using cheese and cracker variables, add 100 tocheese and 1000 to crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)