# Dillinger

# Govtech1
![Screenshot1][screenshot1]

The above screenshot shows a series of letters that only contain ABCD.
We can infer that this might be an encoding of base4
> A = 00, B = 01, C = 10, D = 11

lets confirm our suspicion by inserting "f".

![Screenshot2][screenshot2]
From this, we can infer that 4 letters correspond to a single ascii character.
With some python scripting, we can confirm our hypothesis.
```python
d = {"A":"00", "B":"01", "C":"10", "D":"11"}
enc = "BCBC"
tmp = ''
for char in enc:
    tmp += d[char]
print "binary: ", tmp
print "integer: ", int(tmp, base=2)
print "ascii: ", chr(int(tmp, base=2))
```
From this, we can see that "BCBC" forms "01100110" which is 102 and 'f' in ascii.
Now we can write our python script to decode the entire message

```python
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
```
The decoded message is `fLaG{tech_Base4}`

[screenshot1]: https://raw.githubusercontent.com/0x0ffff5ec/crossctf-2017/master/final/web/screenshots/govtech-web1_i.JPG

[screenshot2]: https://github.com/0x0ffff5ec/crossctf-2017/raw/master/final/web/screenshots/govtech-web1_ii.JPG
