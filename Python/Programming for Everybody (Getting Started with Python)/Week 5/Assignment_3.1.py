hrs = input("Enter Hours:")
rph = input("Enter Rate:")

h = float(hrs)
r = float(rph)

x = 0
y = 0
z = 0

if h > 40:
    x = h * r
    y = (h - 40.0) * (r * 0.5)
    z = x + y
else:
    z = h * r

print(z)