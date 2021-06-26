score = input("Enter Score: ")

s = float(score)

if s < 0 or s > 1.0:
    x = "Score out of range."
elif s >= 0.9:
    x = 'A'
elif s >= 0.8:
    x = 'B'
elif s >= 0.7:
    x = 'C'
elif s >= 0.6:
    x = 'D'
else:
    x = 'F'

print(x)
