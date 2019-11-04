def dupsym(x,sym,line,errlist,keyw):
	for symbol in x:
		if sym==symbol[0]:
			error=[line,sym,1]
			errlist.append(error)
			return 0
	if sym in keyw and sym!="main":
		error=[line,sym,5]
		errlist.append(error)
		return 0
	return 1
 
def undsym(x,sym,line,errlist,keyw):
	for symbol in x:
		if sym==symbol[0]:
			return

	error=[line,sym,4]
	errlist.append(error)
	return
			
