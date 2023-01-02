
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

import string

class HashTable(object):
    def __init__(self):
        self.table = [None]*700

        # MAY ALSO CREATE BUCKET DURING ADDITION OF WORD A WORD
        # Create buckets for the hash table (First two letters of a word)
        counter = 0
        for i in string.ascii_uppercase:
            for j in string.ascii_uppercase:
                self.table[counter] = {"key": i+j, "words": []}
                counter += 1

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        for bucket in self.table:
            if bucket:
                if bucket["key"] == string[:2].upper():
                    bucket["words"].append(string)
                    # print(self.table)
                    return
        else:
            print("ERROR: probably used a non alphabet character")


            

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return -1
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
