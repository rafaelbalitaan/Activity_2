print ("Enter your grades for Prelims, Midterms, Semifinals, and Finals: ")
prelim = int(input("Prelims: "))
midterm = int(input("Midterms: "))
semifinal =int(input("Semifinals: "))
final = int(input("Finals: "))
avg = (prelim + midterm + semifinal + final)/4
print("Your average is {} " .format(avg))