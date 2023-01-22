s=input('ENTER SOME STRING TO CHECK ITS OCCURANCE: ')
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occurs {} times'.format(ch,s.count(ch)))
