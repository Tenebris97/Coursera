def computepay(h, r):
    if h > 40:
        x = h * r
        y = (h - 40.0) * (r * 0.5)
        z = x + y
    else:
        z = h * r
    return z


hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h, r)
print("Pay", p)
