import dns.resolver

res = dns.resolver.Resolver()

arquivo = open("/usr/share/wfuzz/wordlist/general/common.txt", "r")
subdominios = arquivo.read().splitlines()

alvo = "bancocn.com"

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + alvo
		resultado = res.resolve(alvo, "A")
		for info in resultado:
			print(sub_alvo, "->",info)
	except:
		pass
