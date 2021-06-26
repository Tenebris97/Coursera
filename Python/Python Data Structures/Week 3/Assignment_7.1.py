# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for l in fh:
    la = l.rstrip()
    print(la.upper())
