def cypher(string_in, page):
		base = ['a', 'b', 'c', 'd', 'e', ' ', 'f', 'g', 'h', 'i', '.', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', ',', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		string_out = list(string_in)
		place = 0
		for a in string_out:
			st = 0
			while a != base[st]:
				st = st + 1
			en = ((st + page) % len(base))
			print(en)
			string_out[place] = base[en]
			place = place + 1
		for b in string_out:
			print(b, end='')
		print()