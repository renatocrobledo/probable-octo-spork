s = list(reversed('helloworld'))

r = []
if len(s) % 2 == 0:
    
    for n in range(1,len(s),2):
        r.append(s[n])
    for n in range(0,len(s),2):
        r.append(s[n])
else:

    for n in range(0,len(s),2):
        r.append(s[n])
    for n in range(1,len(s),2):
        r.append(s[n])
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("".join(r))