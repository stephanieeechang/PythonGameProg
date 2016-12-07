'''
this program decrypts messages
'''
import Cipher
import random

keylen = 5
key = ''
msg = '''
icwclhcq 1rs, 2016
nm ly kfscrs cxociesenm emsn sdc veki qcfkl, e wflc fwqnrr sder lyrscqentr ltrdqnnl.
es dfi hqekkefms qci ronsr fmi hqebds yckknv rsqeocr.
cfbcq sn sfjc f rflokc hfwj emsn sdc kfh anq nhrcqufsenm,
e wts nts f oecwc na es fmi okfwci es em ly zeo knwj hfb.'''
for times in range(7893600):
    for i in range(keylen):
        x = random.randrange(97,123)
        a = chr(x)
        while a in key:
            x = random.randrange(97,123)
            a = chr(x)
        key += chr(x)

    translated = Cipher.decrypt(msg, key)
    if 'this mysterious mushroom.' in translated:
        possible = translated
        possible += '\n'
        print(key)
        print(possible)
    key = ''


