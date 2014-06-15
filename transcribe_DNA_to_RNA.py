print "Enter DNA sequence to transcribe:"
sequence = raw_input(">>> ")

sequence = sequence.lower()

transcript = ""

for letter in sequence:
	if letter == "a":
		transcript = transcript + "A"
	elif letter == "c":
		transcript = transcript + "C"
	elif letter == "g":
		transcript = transcript + "G"
	elif letter == "t":
		transcript = transcript + "U"
	else:
		print "Fail! Input sequence is not DNA."

print transcript