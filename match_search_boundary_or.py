import re

s=input("Hi, Are you salaried person ?:")
print (s)
#st=re.search(r"\byes\b|\bno\b",s)
st=re.match(r"\byes\b|\bno\b",s)

print (st)
