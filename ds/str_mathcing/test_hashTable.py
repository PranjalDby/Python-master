# test_hashtable.py

# ...
import unittest
from HashMap import HashMap
def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert "hello" in hash_table.values

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert "hello" not in hash_table.values

if __name__ == "__main__":
    hash_table = HashMap(size=100)
    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True
    test_should_delete_key_value_pair(hash_table)
    unittest.main()