# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
c = 0
f = 0

for line in fh:
    l = line.rstrip()
    if l.startswith("X-DSPAM-Confidence:"):
        c += 1
        la = l.split(':')[1]
        f += float(la)

print("Average spam confidence:", f/c)
