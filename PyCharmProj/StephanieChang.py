'''
The program prints my basic information (name, email, grade) and the lyrics of a song I like.
'''

name = 'Fgrcunavr Punat'

email = 'fgrcunavrpunat@cnpvsvpnzrevpna.bet'

grade = 11

lyrics = '''ung vs Jung vs jr eha njnl
Jung vs Jung vs jr yrsg gbqnl
Jung vs Jr fnvq tbbqolr gb fnsr naq fbhaq
Jung vs Jung vs jr'er uneq gb svaq
Jung vs Jung vs jr ybfg bhe zvaqf
Jung vs Jr yrg gurz snyy oruvaq, naq gurl'er arire sbhaq

Naq jura gur yvtugf fgneg synfuvat yvxr n cubgb obbgu
Naq gur fgnef rkcybqvat
Jr'yy or svercebbs

Zl lbhgu Zl lbhgu vf lbhef
Gevccva' ba fxvrf, fvccva' jngresnyyf
Zl lbhgu Zl lbhgu vf lbhef
Eha njnl abj naq sberirezber
Zl lbhgu Zl lbhgu vf lbhef
Gur gehgu fb ybhq lbh pna'g vtaber
Zl lbhgu, zl lbhgu, zl lbhgu
Zl lbhgu vf lbhef

Jung vs Jung vs jr fgneg gb qevir
Jung vs Jung vs jr pybfr bhe rlrf
Jung vs Jr'er fcrrqvat guebhtu erq yvtugf vagb cnenqvfr
'Pnhfr jr'ir ab gvzr sbe trggvat byq
Zbegny obqvrf, gvzryrff fbhyf
Pebff lbhe svatref, urer jr tb
Bu, bu, bu

Naq jura gur yvtugf fgneg synfuvat yvxr n cubgb obbgu
Naq gur fgnef rkcybqvat
Jr'yy or svercebbs

Zl lbhgu Zl lbhgu vf lbhef
Gevccva' ba fxvrf, fvccva' jngresnyyf
Zl lbhgu Zl lbhgu vf lbhef
Eha njnl abj naq sberirezber
Zl lbhgu Zl lbhgu vf lbhef
Gur gehgu fb ybhq lbh pna'g vtaber
Zl lbhgu, zl lbhgu, zl lbhgu
Zl lbhgu vf lbhef
Zl lbhgu vf lbhef

Zl lbhgu Zl lbhgu vf lbhef
Gevccva' ba fxvrf, fvccva' jngresnyyf
Zl lbhgu Zl lbhgu vf lbhef
Eha njnl abj naq sberirezber
Zl lbhgu Zl lbhgu vf lbhef
Gur gehgu fb ybhq lbh pna'g vtaber
Zl lbhgu, zl lbhgu, zl lbhgu
Zl lbhgu vf lbhef
Bu, bu, bu
Zl lbhgu vf lbhef
Bu, bu, bu
Zl lbhgu vf lbhef'''
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print('Name: ')
print("".join([d.get(c, c) for c in name]))
print('Email: ')
print("".join([d.get(c, c) for c in email]))
print('Grade: ' + str(grade))
print('The lyrics of Youth by Troye Sivan: ')
print("".join([d.get(c, c) for c in lyrics]))
