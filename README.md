# Specifications

* hash(self, key, inserting=False)
  * Given a key string return an index in the hash table.
  * Should implement double hashing.
    * If the key exists in the hash table, return the index of the existing HashNode
    * If the key does not exist in the hash table, return the index of the next available empty position in the hash table.
      * Collision resolution should implement double hashing with hash1 as the initial hash and hash2 as the step size
    * Note - There are 2 possibilities when hashing for an index:
      * When inserting a node into the hash table we want to insert into the next available bin. 
      * When performing a lookup/deletion in the hash table we want to continue until we either find the proper HashNode or until we reach a bin that has never held a value. This is to preserve the collison resolution methodology.
      * The inserting parameter should be used to differentiate between these two cases.
  * Return: type int
  * Time Complexity: Θ(1)* 
  * Space Complexity: O(1) 

* insert(self, key, value):
  * Use the key and value parameters to add a HashNode to the hash table.
  * In the event that inserting will exceed or equal a load factor of 0.5 you must grow the table to double the existing capacity.
  * Return: type None
  * Time Complexity: Θ(1)*
  * Space Complexity: O(1)*

* get(self, key)
  * Find the HashNode with the given key in the hash table.
  * Return: type HashNode
    * If no elements exist, return None
  * Time Complexity: Θ(1)*
  * Space Complexity: O(1)

* delete(self, key)
  * emoves the HashNode with the given key from the hash table .
    * If the node is found assign its key and value to None, and set the deleted flag to True
  * Return: type None
  * Time Complexity: Θ(1)*
  * Space Complexity: O(1) 

* grow(self)
  * Double the capacity of the existing hash table.
  * Do NOT rehash deleted HashNodes
  * Must update self.prime_index, the value of self.prime_index should be the index of the largest prime smaller than self.capacity in the HashTable.primes tuple.
  * Return: type None
  * Time Complexity: O(N) 
  * Space Complexity: O(N) 
