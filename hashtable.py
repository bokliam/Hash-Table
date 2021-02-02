'''
Hash Tables
Name: Liam Bok
'''

class HashNode:

    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'collisions', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def __setitem__(self, key, value):
        """
        Allows for the use of the set operator to insert into table
        :param key: string key to insert
        :param value: value to insert
        :return: None
        """
        return self.insert(key=key, value=value)

    def __getitem__(self, item):
        """
        Allows get operator to retrieve a value from the table
        :param item: string key of item to retrieve from tabkle
        :return: HashNode
        """
        return self.get(item)

    def __contains__(self, item):
        """
        Checks whether a given key exists in the table
        :param item: string key of item to retrieve
        :return: Bool
        """
        if self.get(item) is not None:
            return True
        return False

    def _hash_1(self, key):
        """
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value
  
    def hash(self, key, inserting=False):
        """
        Given a key string, return its associated index in the hash table
        :param key: key of type string being hashed
        :param inserting: True if hashing for insert, False if searching/deleting
        :return: index of key for hash table
        """
        i = self._hash_1(key)
        if i is None:
            return None
        temp_node = self.table[i]
        if temp_node is None:
            return i
        elif temp_node.key == key:
            return i
        elif temp_node.deleted is True and inserting is True:
            return i
        # if hash_1 is deleted and not inserting, search for node
        elif temp_node.deleted is True and inserting is False:
            cnt = 1
            while temp_node is not None:
                next_idx = (i + cnt * self._hash_2(key)) % self.capacity
                if self.table[next_idx] is None:
                    return next_idx
                elif (self.table[next_idx]).key == key:
                    return next_idx
                temp_node = self.table[next_idx]
                cnt += 1
        # if hash_1 key does not equal key parameter, search for open index
        elif temp_node.key != key and inserting is True:
            cnt = 1
            while temp_node is not None:
                next_idx = (i + cnt * self._hash_2(key)) % self.capacity
                if self.table[next_idx] is None:
                    return next_idx
                elif (self.table[next_idx]).key == key:
                    return next_idx
                temp_node = self.table[next_idx]
                cnt += 1
        # if hash_1 key does not equal key parameter and not inserting
        elif temp_node.key != key and inserting is False:
            cnt = 1
            while temp_node is not None:
                next_idx = (i + cnt * self._hash_2(key)) % self.capacity
                if self.table[next_idx] is None:
                    return None
                elif (self.table[next_idx]).key == key:
                    return next_idx
                temp_node = self.table[next_idx]
                cnt += 1
        else:
            return None


    def insert(self, key, value):
        """
        Insert a HashNode with key/value into hash table
        :param key: key parameter of HashNode
        :param value: value parameter of HashNode
        :return: None
        """
        node = HashNode(key, value)
        i = self.hash(key, True)
        if i is None:
            return None
        self.table[i] = node
        self.size += 1
        if (self.size/self.capacity) >= 0.5:
            self.grow()
        return None


    def get(self, key):
        """
        Find HashNode with given key in hash table
        :param key: key used to search for HashNode
        :return: HashNode if found, otherwise None
        """
        if self.size == 0:
            return None
        i = self.hash(key)
        if i is None:
            return None
        else:
            return self.table[i]


    def delete(self, key):
        """
        Remove HashNode with given key from hash table
        :param key: key used to find HashNode to be deleted
        :return: None
        """
        if self.size == 0:
            return None
        i = self.hash(key)
        if i is None:
            return None
        else:
            node = self.table[i]
            node.key = None
            node.value = None
            node.deleted = True
            self.size -= 1
        return None

    def grow(self):
        """
        Double the capacity of the existing hash table
        :return: None
        """
        old = self.table
        new_cap = self.capacity * 2
        new_table = [None] * new_cap
        self.capacity = new_cap
        self.size = 0
        self.table = new_table

        # get new prime index
        i = len(self.primes) - 1
        while i >= 0:
            if self.primes[i] < self.capacity:
                self.prime_index = i
                break
            i -= 1

        # populate new hash table
        for hash_node in old:
            if hash_node is not None and hash_node.deleted is False:
                self.insert(hash_node.key, hash_node.value)
        return None

def word_frequency(string, lexicon, table):
    """
    Find the frequency of the longest words in a string
    :param string: string containing words with no spaces or punctuation
    :param lexicon: list of words that are in the string parameter
    :param table: Hash table containing each word and their associated frequency
    :return: Hash table
    """
    cnt = 1
    flag = 0
    # Check if lexicon is a dictionary or list
    if type(lexicon) is list:
        # Sort lexicon with words sorted from longest to shortest
        lexicon.sort(key=len, reverse=True)
        # Loop and get frequency of each word
        for word in lexicon:
            if word in string:
                cnt = 1
                while flag == 0:
                    table.insert(word, cnt)
                    string = string.replace(word, '', 1)
                    cnt += 1
                    if word not in string:
                        break
            else:
                table.insert(word, 0)

    else:
        # Create new lexicon with words sorted from longest to shortest
        lex = []
        for key in lexicon:
            lex.append(key)
        lex.sort(key=len, reverse=True)
        # Loop and get frequency of each word
        for key in lex:
            if key in string:
                cnt = 1
                while flag == 0:
                    table.insert(key, cnt)
                    string = string.replace(key, '', 1)
                    cnt += 1
                    if key not in string:
                        break
            else:
                table.insert(key, 0)
    return table


