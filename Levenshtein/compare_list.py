import Levenshtein

l_rd=[]
l_po=[]
f_rd = open('part_aps_shu.txt','r', encoding='UTF8')
s = '1'
while s:#True:
	s = f_rd.readline()
	s = s.replace('\n','')
	s = s.strip()
	l_rd.append(s)
f_rd.close()

f_po = open('VSUR_426487_013_SHU_SAU_GPA_mk150.pro','r', encoding='UTF8')
s = '1'
while s:#True:
	s = f_po.readline()
	s = s.replace('\n','')
	s = s.strip()	
	l_po.append(s)
f_po.close()

f_w = open('part_aps_shu_in_po.txt', 'w')

for g in l_po:
	l_lev = []
	for res in l_rd:
		s1 = g
		s2 = res
		lev = Levenshtein.distance(s1, s2)
		l_lev.append([g,res,str(lev)])
		#print(l_rd[50] + ' *** ' + res + ' *** ' + str(lev))
		#print(l_lev[0])
	min = l_lev[0][2]
	n = 0
	for z in l_lev:
		#print(z[2] + ' *** ' + str(min))
		if z[2] < min:
			min = z[2]
			n = l_lev.index(z)

	out = ';'.join(l_lev[n])
	#f_w.write(out + '\n')
	print(out)	

f_w.close()