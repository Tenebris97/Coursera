fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
d = []

for line in fh:
    if line.startswith('From') and len(line.split()) > 2:
        t = line.split()
        d.append(t[1])

for w in d:
    print(w)


print("There were", len(d), "lines in the file with From as the first word")
