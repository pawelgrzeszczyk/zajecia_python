# KLASY STR
# napisUnicode = u''
# napisStr = napisUnicode.encode('utf8')
# napisUnicode2 = napisStr.decode('utf8')
# print len(napisUnicode), len(napisStr), len(napisUnicode2)

#basestring
#
# napisUnicode = u''
# napisStr = napisUnicode.encode('utf8')
# print isinstance(napisStr, basestring)
#

#formatowanie napisow
#
# napis = u' TEST '
# napis2 = u'Test Test'
# print napis.strip()
# print napis.strip().center(30)
# print napis.capitalize()
# print napis.lower().islower()
# print napis.startswith(' T')
# print napis.ljust(30)
# print napis2.swapcase()
# print 'st T' in napis2
# print napis2.replace('Test', 'Test')

#wtrazenia regularne

# import re
#
# regex_email = re.compile(
#     r'''(?P<adres>
#         (?P<login>[\w+.]+)
#         @
#         (?P<domena>\w+(\.\w+)+)
#     )''',
#     re.IGNORECASE | re.VERBOSE #komentarze
#     )
#
# tekst = u'mail@poczta.pl, "jan.nowak@wp.pl"'
# for match_object in regex_email.finditer(tekst):
#     print match_object.groupdict()

# serializacja danych
#
# import json
# slownik = {
#     'k1':'w1',
#     'k2':'w2',
#     3:[1,2,3],
# }
#
# jsonStr = json.dumps(slownik)
# print jsonStr
#
# slownik2 = json.loads(jsonStr)
# print slownik2
#
# import pickle
#
# slownikk = {
#     'k1':'w1',
#     'k2':'w2',
#     3:[1,2,3],
# }
#
# pickleStr = pickle.dumps(slownik)
# print pickleStr
#
# slownikk2 = pickle.loads(pickleStr)
# print slownik2