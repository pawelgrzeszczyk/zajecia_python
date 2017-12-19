#LOGGERY
# import logging
#
#
#
# def main():
#     logging.basicConfig(filename='app.log', level=logging.INFO)
#     logging.info("start")
#
#
# if __name__ == '__main__':
#     main()
#
# #
# import logging
# import other
# def fun():
#     logging.basicConfig(filename='app.log', level=logging.INFO)
#     logging.info("start")
#     other.fun()
#     logging.info("koniec")
#     logging.debug("debug")
#
# if __name__ == '__main__':
#     fun()
#DEBUGOWANIE
# import pdb
#
#
# def fun():
#     d = 'd'
#     print d
#
# a = 'a'
# pdb.set_trace()
# b = 'b'
# pdb.set_trace()
# c = 'c'
# pdb.set_trace()
# fun()
# res = a+b+c
# print res

# import pdb
#
# list = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','b','c','d']
# pdb.set_trace()
# print list

#TESTY
#liczby.py
# def num2text(n):
#     return {
#         0: 'zero',
#         1: 'jeden',
#         2: 'dwa',
#         3: 'trzy'
#     }.get(n)
#
# #nowy plik
# import liczby
#
# class Testy(object):
#     def test_answer_type(self):
#         assert isinstance(liczby.num2text(1), basestring)
#     def test_zero_text(self):
#         assert liczby.num2text(0) == 'zero'
#     def test_one_text(self):
#         assert liczby.num2text(1) == 'jeden'
#     def test_two_text(self):
#         assert liczby.num2text(2) == 'dwa'