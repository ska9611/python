mem = {"KB":"kilo", 'MB':'mega', 'GB':'giga', 'TB':'tera', 'PB':'peta'}

mem['EB'] = 'exa'
mem['GB'] = 'Giga'
print(mem)

result = 'TB'  in  mem
print(result)

result2 = 'tera' in mem.values()
print(result2)

print(mem.keys())
print(mem.values())
print(mem.items())

print(mem.get('MB'))
del mem['TB']
mem.clear()
print(mem)