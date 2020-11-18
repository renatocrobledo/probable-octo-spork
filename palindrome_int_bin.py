def isPalindrome(s):
    return s == s[::-1]

n = int(input())
a=b=c=0

for i in range(10,n+1):
    if isPalindrome(str(i)): a+=1
    if isPalindrome(bin(i)[2:]): b+=1
    if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]): 
        c+= 1
        a-=1
        b-=1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(a,b,c)