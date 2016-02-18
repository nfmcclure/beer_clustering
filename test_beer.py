##------------------------------------------------------------
##
## Nose- Unit tests for Beer Clustering
##
## Created: Feb, 2016
##
##------------------------------------------------------------
import text_clustering_funs

def test_csv_to_lists(): # This is kind-of a regression test...
    data = text_clustering_funs.csv_to_lists('beer_reviews.csv')
    assert(len(data) > 0)


def test_remove_characters():
    string_seq = ['foo bar', '', 'foo bad123 bar', 'bad123']
    seq_removal = 'bad123'
    new_strings = [text_clustering_funs.remove_characters(s, seq_removal) for s in string_seq]
    assert(new_strings == ['foo r', '', 'foo  r', ''])


def test_normalize():
    string_seq = ['foo bar..()$', '   Foo   Bar   ', '123 foo bad123    ', 'This Is Good!!']
    new_strings = text_clustering_funs.normalize(string_seq, ['punctuation', 'numbers', 'stopwords', 'whitespace', 'lower'])
    assert(new_strings == ['foo bar', 'foo bar', 'foo bad', 'this is good'])
