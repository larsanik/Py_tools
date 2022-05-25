f_r = open('T_Nev_PS.txt','r', encoding='UTF8')
f_w = open('text.txt', 'w')
i = 1
s= '1'
l=[]
out=''
while s:#True:
	s = f_r.readline()
	'''s1=s.split("'")

	if len(s1)>1:
		s2 = s1[0].replace('APS_SHUD_MK150.', '')
		s2 = s2.replace('_Str', '')
		s2 = s2.replace(' :=', '')
		s2 = s2.strip()
		s3 = s1[1].strip()
		if not (s3.startswith('ALM') or s3.startswith('EMG')):
			print(s3 + ';' + s2)
			f_w.write(s3 + ';' + s2 + '\n')
	'''
	if s.find('Variable="Name"') > -1 or s.find('Variable="NameAlg"') > -1:
		s4 = s.strip()
		s4 = s4.split('"')
		s4 = s4[3].replace('&apos;','')
		s4 = s4.strip()
		#print(s4)
		l.append(s4)
	i+=1
#print(int(len(l)/2))
for i in range(int(len(l)/2)):
	out = l[i*2] + ';' + l[i*2+1]  + '\n'
	print(out)
	f_w.write(out)

f_r.close
f_w.close