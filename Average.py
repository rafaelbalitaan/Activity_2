print ("Enter your grades for Prelims, Midterms, Semifinals, and Finals: ")
prelim = int(input("Prelims: "))
midterm = int(input("Midterms: "))
semifinal =int(input("Semifinals: "))
final = int(input("Finals: "))
avg = (prelim + midterm + semifinal + final)/4
print("Your average is {} " .format(avg))
if avg>=75 and avg<=100:
    print("You Are Passed")
else:
    print("You Are Failed")
    if avg>=99 and avg<=100:
	print("Your grade is A")
elif avg>=90 and avg<=98:
	print("Your grade is B")
elif avg>=80 and avg<=89:
	print("Your grade is C")
elif avg>=71 and avg<=79:
	print("Your grade is D")
elif avg>=61 and avg<=70:
	print("Your grade is E")
elif avg<60:
	print("Your grade is F")
else:
	print("INVALID")