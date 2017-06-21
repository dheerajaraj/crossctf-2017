
#base 4 encoding
d = {"A":"00", "B":"01", "C":"10", "D":"11"}

enc = "BCBCBADABCABBABDBDCDBDBABCBBBCADBCCABBDDBAACBCABBDADBCBBADBABDDB"

def separate(encoded):
    tmp = []
    for i in range(0, len(encoded), 4):
            tmp.append(encoded[i:i+4])
    return tmp

def decode(part):
    global d
    combine = ''
    for char in part:
        combine += d[char]
    return chr(int(combine, base=2))

array = separate(enc)

tmp = ''
for item in array:
    tmp += decode(item)

print "encoded: ", enc
print "decoded: ", tmp
