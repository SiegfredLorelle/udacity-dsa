
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

import string

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

        # MAY ALSO CREATE BUCKET DURING ADDITION OF WORD (THAT IS FASTER IF HASH TABLE IS GOING TO RESET/DELETED OFTEN)
        # Create buckets for the hash table (key is ascii value of first two letter of a word)
        # Counter for the index of the buckets
        counter = 0
        # Loop through the alphabets twice
        for i in string.ascii_uppercase:
            for j in string.ascii_uppercase:
                # Create a dictionary/bucket for each letter permutation (two letter)
                # The key is the combination of the ascii value of the two letter while the values is a list of words starting with the two letters
                self.table[counter] = {"key": str(ord(i))+str(ord(j)), "words": []}
                counter += 1

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Calculate the hash value of the given string
        hash_value = self.calculate_hash_value(string)
        # Loop through the hash table to find the correct bucket
        for bucket in self.table:
            # Some buckets are unused, so disregard if bucket is None
            if bucket:
                # If bucket's key matches the hash value of the string then add the given string to the words list of that bucket
                if bucket["key"] == hash_value:
                    bucket["words"].append(string)
                    break
        else:
            # If no matching hash value for that string then there is an error (commented print is used to submit in udacity since f string don't work there)
            print(f"ERROR: no buckets for '{string}', probably used a non alphabet character")
            # print("ERROR: no buckets for %s, probably used a non alphabet character" %string)


    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Calculate the hash value of the given string
        hash_value = self.calculate_hash_value(string)
        # Loop through the hash table to find the correct bucket
        for bucket in self.table:
            # Some buckets are unused, os disregard if bucket is None
            if bucket:
                # If bucket's key matches the hash value of the string then check if the given string is in word list of that bucket
                if bucket["key"] == hash_value:
                    if string in bucket["words"]:
                        return hash_value
                    else:
                        return -1
        else:
            # If no matching hash value for that s
            print(f"ERROR: no buckets for '{string}', probably used a non alphabet character")
            # print("ERROR: no buckets for %s, probably used a non alphabet character" %string)


    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_value = ""
        # Get the ascii value of the first two letter of the given string, then combine them
        for index, i in enumerate(string[:2]):
            hash_value += str(ord(i))
        return hash_value


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