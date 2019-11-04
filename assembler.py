import check as err
x=[]
errlist=[]
reg=['eax','ebx','ecx','edx','esi','edi','esp','ebp']
keyw=['main','mov','jmp','inc','add']
fp=open("my.asm","r")
dsize=0
i=fp.readlines()
j=0
while j<len(i):	
	if i[j].rstrip().lstrip()=="section .data":
		j+=1
		while j<len(i) and (i[j].rstrip().lstrip()!="section .bss" and i[j].rstrip().lstrip()!="section .text"):
			str1=i[j].split()
			a=[]
			sym=str1[0]
			a.append(str1[0])
			a.append("d")
			if "db"not in str1[1] and "dd" not in str1[1] :
				e=[]
				e.append(j+1)
				e.append('')
				e.append(2)
				errlist.append(e)
				j+=1
			elif "db" in str1[1] and err.dupsym(x,sym,j+1,errlist,keyw):
				if '"' in i[j]:
					ds=0
					str2=i[j].split('"')
					for k in str2[1]:
						ds=ds+1
					ds=ds+len(str2[2].split(","))-1
				a.append(dsize)
				a.append(1)
				a.append(ds)
				a.append("D")
				x.append(a)
				dsize=dsize+ds
				j+=1

			elif "dd" in str1[1] and err.dupsym(x,sym,j+1,errlist,keyw):
				str2=str1[2].split(",")
				a.append(dsize)
				a.append(4)
				a.append(len(str2))
				a.append("D")
				x.append(a)
				dsize=dsize+4*len(str2)
				j+=1
		
			else:
				j+=1
	elif i[j].rstrip().lstrip()=="section .bss":
		j+=1
		bsize=0
		while j<len(i) and i[j].rstrip().lstrip()!="section .text":
			str1=i[j].split()
			a=[]
			sym=str1[0]
			a.append(str1[0])
			a.append("b")
			if "resb"not in str1[1] and "resd" not in str1[1] :
				e=[]
				e.append(j+1)
				e.append('')
				e.append(2)
				errlist.append(e)
				j+=1
			elif "resb" in str1[1]and err.dupsym(x,sym,j+1,errlist,keyw):
				a.append(bsize)
				a.append(1)
				a.append(1*int(str1[2]))
				a.append("D")
				x.append(a)
				j+=1
			elif "resd" in str1[1]and err.dupsym(x,sym,j+1,errlist,keyw):
				a.append(bsize)
				a.append(4)
				a.append(4*int(str1[2]))
				a.append("D")
				x.append(a)
				j+=1
			else :
				j+=1
	
	elif i[j].rstrip().lstrip()=="section .text":
		j+=1
		while j<len(i):
			str1=i[j].split()
			if "extern" in str1[0]:
				str2=str1[1].split(",")
				for k in str2:
					a=[]
					a.append(k)
					a.append('t')
					a.append('')
					a.append('')
					a.append('')
					a.append("U")
					x.append(a)
				j+=1

			elif ":" in i[j]:
				a=[]
				str2=i[j].split(":")
				a.append(str2[0])
				x.append(a)
				a.append('t')
				a.append('')
				a.append('')
				a.append('')
				a.append("U")
				j+=1
			
			elif "mov" in str1[0]:
				a=[]
				str2=str1[1].split(',')
				if str2[0] not in reg:
					a.append(j+1)					
					a.append('')
					a.append(3)
					errlist.append(a)
					j+=1
				elif str2[1].isdecimal()==False and str2[1] not in reg:
					err.undsym(x,str2[1],j+1,errlist,keyw)
					j+=1
				else:
					j+=1
			elif "add" in str1[0]:
				a=[]
				str2=str1[1].split(',')
				if str2[0] not in reg:
					a.append(j+1)
					a.append('')
					a.append(3)
					errlist.append(a)
					j+=1
				elif str2[1].isdecimal()==False and str2[1] not in reg:
					err.undsym(x,str2[1],j+1,errlist,keyw)
					j+=1
				else:
					j+=1
			else:
				j+=1
print("symbol table:")			
for k in x:
	print(k)
print("error table:")
for k in errlist:
	print(k)
for k in errlist:
	if k[2]==1:
		print("line:%d error:'%s'symbol redefined"%(k[0],k[1]))
	if k[2]==2:
		print("line:%d error: parser: instruction expected"%(k[0]))
	if k[2]==3:
		print("line:%d error:invalid combination of opcode and operands"%(k[0]))
	if k[2]==4:
		print("line:%d error:'%s' error: symbol undefined"%(k[0],k[1]))
	if k[2]==5:
		print("line:%d error:'%s' error: keyword used as identifier"%(k[0],k[1]))


