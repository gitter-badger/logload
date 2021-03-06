import unittest

from funcparserlib.parser import NoParseError
from logload import logload

class TestTokenizer(unittest.TestCase):
    def test_name(self):
        logload.tokenize("foobar")

    def test_string(self):
        logload.tokenize("\"foobar\"")

    def test_group(self):
        logload.tokenize("[ \"foo\", \"bar\" ]")

    def test_list(self):
        logload.tokenize("( \"foo\", glorg )")

    def test_nested_group(self):
        logload.tokenize('( "foo" [ "bar", "baz" ] )')
        
    def test_empty(self):
        logload.tokenize("")

class TestParser(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(NoParseError):
            logload.parse(logload.tokenize(""))

    def test_empty_list(self):
        logload.parse(logload.tokenize("( )"))
        
    def test_list_string(self):
        logload.parse(logload.tokenize("( \"foobar\" )"))

    def test_empty_group(self):
        logload.parse(logload.tokenize('[ ]'))

    def test_nonexisting_function(self):
        with self.assertRaises(NoParseError):
            logload.parse(logload.tokenize('"foobar", blorp'))
        
    def test_simple_group(self):
        logload.parse(logload.tokenize("[ \"foobar\", randword, timestamp ]"))

    def test_nested_group1(self):
        logload.parse(logload.tokenize('( [ "bar", "baz" ] )'))

    def test_nested_group2(self):
        logload.parse(logload.tokenize('( "foo", [ "bar", "baz" ] )'))
        
if __name__ == "__main__":
    unittest.main()
