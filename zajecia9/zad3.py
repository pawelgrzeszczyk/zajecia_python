import liczby

class Testy(object):
    def test_answer_type(self):
        assert isinstance(liczby.num2text(1), basestring)
    def test_zero_text(self):
        assert liczby.num2text(0) == 'zero'
    def test_one_text(self):
        assert liczby.num2text(1) == 'jeden'
    def test_two_text(self):
        assert liczby.num2text(2) == 'dwa'
    def test_tree_text(self):
        assert liczby.num2text(3) == 'trzy'