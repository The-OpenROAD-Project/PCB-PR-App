with open("./cache/initial_pl.pl") as f:
    orig = f.read().splitlines()

with open("./cache/999.pl") as f:
    new = f.read().splitlines()

hamming_dist = 0
for orig_line, new_line in zip(orig, new):
	if orig_line.strip() == '' and new_line.strip() == '':
		continue
	print(orig_line, new_line)
	if int(orig_line.split()[-1]) !=int(new_line.split()[-1]):
		hamming_dist +=1

print(len(orig), hamming_dist)
