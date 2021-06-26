name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

text = open(name)

max = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "):
        continue

    words = line.split()
    max[words[1]] = max.get(words[1], 0)+1

l = None
lAuthor = None

for key in max:
    if l is None:
        l = max[key]

    if l < max[key]:
        l = max[key]
        lAuthor = key

print(lAuthor, l)
