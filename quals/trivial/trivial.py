# uncompyle6 version 2.9.11
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.5.3 |Continuum Analytics, Inc.| (default, May 11 2017, 13:52:01) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: trivial.py
# Compiled at: 2017-05-10 17:48:32
import json
import sys

def check(flag):
    processed = flag[::-1]
    processed = processed.decode('base64')
    final = json.loads(processed)
    if final['check_code'] != 'AK4782':
        return False
    if final['flag_content']['numbers'] * 2 != 18529313:
        return False
    if final['flag_content']['change'] != 'standardisation'[::2]:
        return False
    if final['flag_content']['settled'] != 'CrossCTF{%s_%d_%s}':
        return False
    temp = final['flag_content']
    return temp['settled'] % (temp['change'], temp['numbers'], final['check_code'])


def main():
    if len(sys.argv) != 2:
        print 'No'
        sys.exit()
    result = check(sys.argv[1])
    if result:
        print result
    else:
        print 'No'


if __name__ == '__main__':
    main()
# okay decompiling trivial.pyc
