import random
def tdobj(h,wh):
	obj = [[0 for x in range(h)] for y in range(wh)]
	return(obj)
def thdobj(h,wh,l):
	obj = [[[0 for x in range(h)] for y in range(wh)] for z in range(l)]
	return(obj)
def fdobj(h,wh,l,t):
	obj = [[[[0 for x in range(h)] for y in range(wh)] for z in range(l)] for w in range(t)]
	return(obj)
def fvdobj(h,wh,l,t,q):
	obj = [[[[[0 for x in range(h)] for y in range(wh)] for z in range(l)] for w in range(t)] for v in range(q)]
	return(obj)
def sdobj(h,wh,l,t,q,p):
	obj = [[[[[[0 for x in range(h)] for y in range(wh)] for z in range(l)] for w in range(t)] for v in range(q)] for b in range(p)]
	return(obj)
def fdcube(h):
	base = fdobj(h,h,h,h)
	return(base)
def fvdcube(h):
	base = fvdobj(h,h,h,h,h)
	return(base)
def sdcube(h):
	base = sdobj(h,h,h,h,h,h)
	return(base)
def tdcube(h):
	base = tdobj(h,h)
	return(base)
def thdcube(h):
	base = thdobj(h,h,h)
	return(base)
def ranfillt(x, r):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			x[one][two] = random.choice(range(r))
			two=two+1
		one=one+1
	return(x)
def ranfillth(x, r):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			three=0
			for c in x[one][two]:
				x[one][two][three] = random.choice(range(r))
				three=three+1
			two=two+1
		one=one+1
	return(x)
def ranfillf(x, r):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			three=0
			for c in x[one][two]:
				four=0
				for d in x[one][two][three]:
					x[one][two][three][four] = random.choice(range(r))
					four=four+1
				three=three+1
			two=two+1
		one=one+1
	return(x)
def ranfillfv(x, r):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			three=0
			for c in x[one][two]:
				four=0
				for d in x[one][two][three]:	
					five=0
					for e in x[one][two][three][four]:
						x[one][two][three][four][five] = random.choice(range(r))
						five=five+1
					four=four+1
				three=three+1
			two=two+1
		one=one+1
	return(x)
def ranfills(x, r):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			three=0
			for c in x[one][two]:
				four=0
				for d in x[one][two][three]:	
					five=0
					for e in x[one][two][three][four]:
						six=0
						for f in x[one][two][three][four][five]:
							x[one][two][three][four][five][six] = random.choice(range(r))
							six=six+1
						five=five+1
					four=four+1
				three=three+1
			two=two+1
		one=one+1
	return(x)