a=0
txt='yourflagis{fhke37_kdrjknbmpr_04374j}'
k='thekey'
alf='qwertyuiopasdfghjklzxcvbnm_{}1234567890'
n=''
for i in txt:
  if i in alf:
    n+=alf[(alf.find(k[a%len(k)])+\
    alf.find(i)+2)%len(alf)]
    a+=1
  else:
    n+=b
print(n)
