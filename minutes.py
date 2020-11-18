a = '15:35'
b = '16:49'

h1, m1 = a.split(":")
h2, m2 = b.split(":")


minutes_1 = int(h1) * 60 + int(m1)
minutes_2 = int(h2) * 60 + int(m2)

print(minutes_2 - minutes_1)