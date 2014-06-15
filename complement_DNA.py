print "Enter DNA sequence for  complementation:"
sequence = raw_input(">>> ")

sequence = sequence.lower()

rev_comp = ""

for letter in sequence:
	if letter == "a":
		char = "T"
	elif letter == "t":
		char = "A"
	elif letter == "g":
		char = "C"
	elif letter == "c":
		char = "G"
	else:
		print "Fail! Input is not DNA!"
		quit()
	rev_comp = rev_comp + char

print rev_comp