# Soundex
# Make dictionary numerics to map each letter to its group
groups = ['aehiouwy', #0
          'bfpv', #1
          'cgjkqsxz', #2
          'dt', #3
          'l', #4
          'mn', #5
          'r'] #6

numerics = {'a': '0', 'c': '2', 'b': '1', 'e': '0', 'd': '3', 'g': '2', 'f': '1',
'i': '0', 'h': '0', 'k': '2', 'j': '2', 'm': '5', 'l': '4', 'o': '0',
'n': '5', 'q': '2', 'p': '1', 's': '2', 'r': '6', 'u': '0', 't': '3',
'w': '0', 'v': '1', 'y': '0', 'x': '2', 'z': '2'}

def soundex(name):
    """ soundex module conforming to Knuth's algorithm implementation 2000-12-24 by
    Gregory Jorgensen public domain
    """
    # digits holds the soundex values for the alphabet
    sndx = ''
    firstchar = name[0].upper()
    # name = name[1:] # le reste du mot
    
    print(firstchar)

    # translate alpha chars in name to soundex digits
    for c in name.lower():
        d = numerics.get(c, '0')
        print(d)
        # duplicate consecutive soundex digits are skipped
        if not sndx or (d != sndx[-1]):
            sndx += d
            
    # replace first digit with first alpha character
    sndx = firstchar + sndx[1:]
    
    # remove all 0s from the soundex code
    sndx = sndx.replace('0','')
    
    # return soundex code padded to len characters
    sndx = sndx + '0000'
    print(sndx)
    
    return sndx[:4]


# test it
words =[ "physique", "physik", "phosphore", "fosfor", "rupert", "rubert", "smith", "schmidt", "jackson"]
for word in words :
    print('Word : ', word)
    code = soundex(word.lower())
    print('Soundex Code: ', code, end='\n\n')