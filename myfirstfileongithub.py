s=input('Enter a string to check its number of occurances: ')
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occurs {} times'.format(ch,s.count(ch)))
