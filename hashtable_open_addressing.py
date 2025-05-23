class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None for i in range(self.size)]

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """Computes and returns the initial location for a given key using built-in hash function"""
        return hash(key) % self.size
      
    def _rehash(self, old_location: int) -> int:
        """ Compute and returns the next location for linear probing """
        return (old_location + 1) % self.size
   	

    def setitem(self, key: str, value: dict) -> None:
        """
        adds / updates the key value as a tuple
        Raises an Exception if hashtable is full
        """
        
        start = self._hash(key)
        current = start
        while self.values[current] != None:
            if self.values[current][0] == key:
                self.values[current] = (key, value)
                return

            current = self._rehash(current)
            if current == start:
                raise Exception
                return

        self.values[current] = (key, value)
        
    def getitem(self, key: str) -> 'dict | None':
        """
        returns a value associated with the given key or
        raises a KeyError if the key is not found
        """
        start = self._hash(key)
        index = self._hash(key)

        if(self.values[index] == None):
            return 'Grr'

        _key, _value = self.values[index]
        while _key != key:
            index = self._rehash(index)
            
            if(self.values[index] == None):
                return 'Grr'

            _key, _value = self.values[index]
            if start == index:
                raise KeyError
                return 
        return _value

    def del_item(self, key: str):
        """
        Deletes item with the given key
        """
        start = self._hash(key)
        current = start
        while self.values[current] != None:
            if self.values[current][0] == key:
                self.values[current] = None
                return

            current = self._rehash(current)
            if current == start:
                raise Exception
                return

        self.values[current] = None