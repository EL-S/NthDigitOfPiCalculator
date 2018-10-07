k = 0

while True:
    k += 1
    value = float((16**k)*((4/((8*k)+1))-(2/((8*k)+5))-(1/((8*k)+6)))) #base 16
    print(value)
