from math import floor

def decode(rn):
    # Dictionary mapping numeral to value
	rv = {
		'm': 1000,
		'd': 500,
		'c': 100,
		'l': 50,
		'x': 10,
		'v': 5,
		'i': 1
	      }
    # Canoncalize to list of lowercase characters without spaces
	rn = list(rn.lower().strip())
    # Loop through in reverse
	lastval = 0
	val = 0
	for ch in rn[::-1]:
	  chval = rv[ch]
	# Compare against previous encountered value
	  if chval >= lastval:
	  # When greater, we add and remember
	    val = val + chval
	    lastval = chval
	  else:
	  # Otherwise, subtract
	    val = val - chval
	return val

def encode(val):
    # Dictionary mapping values to their representations
	nv = {
		1000: 'm',
		900: 'cm',
		500: 'd',
		400: 'cd',
		100: 'c',
		90: 'xc',
		50: 'l',
		40: 'xl',
		10: 'x',
		9: 'ix',
		5: 'v',
		4: 'iv',
		1: 'i'
	      }
    # Loop through character values from lowest to highest
	rn = ''
	for chval in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
	# Calc number of these chars in output
	  ch = nv[chval]
	  cnt = int(val / chval)
	  rn = rn + (ch * cnt)
	  val = val - cnt * chval
	return rn

def rn_add(a, b):
	return encode(decode(a) + decode(b))

print 'III = ', decode('III')
print 'iv = ', decode('iv')
print 'iiv = ', decode('iiv')
print 'ix = ', decode('ix')
print 'xi = ', decode('xi')
print 'iL = ', decode('iL')
print 'mcmXLIX = ', decode('mcmXLIX')
print '110=', encode(110)
print '767=', encode(767)
print '1478=', encode(1478)
print '1888=', encode(1888)
print '1999=', encode(1999)
print '2038=', encode(2038)
print '123456=', encode(123456)
print 'III + vi=', rn_add('III', 'vi')
print 'IV + mix=', rn_add('IV', 'mix')
print 'mCDXLIX + MDCCLXIV=', rn_add('mCDXLIX', 'MDCCLXIV')
print 'CMxL + MCDXL=', rn_add('CMxL', 'MCDXL')

