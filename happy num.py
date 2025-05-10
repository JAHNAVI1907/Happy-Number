def ishappy(num):
   seen=set()
   while num!=1 and num not in seen:
      seen.add(num)
      num=sum(int(i)**2 for i in str(num))
   return num==1
hp=[]
for i in range(1,101):
   if(ishappy(i)):
      hp.append(i)
print(hp)
