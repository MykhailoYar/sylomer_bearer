import re
lis='H:/Version 4 Sylomer choice and pics/12 установок заповнені.xlsx'
out=re.split(r'/?',lis)
print(out)
out2=''
for i in out[0:-1]:
    out2+=i+'/'
print(out2)