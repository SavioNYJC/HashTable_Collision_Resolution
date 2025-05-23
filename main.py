from hashtable_open_addressing import HashTable
import csv
if __name__ == "__main__":
    ht = HashTable(30)
    """
    1. Extract the records from the student_data file
    and add them one at a time, as a Python dict, 
    containing the name, class and their associated
    data as key-value dict pairs, to the hashtable
    
    2. You can use the id as the hash table key for 
    each of the above records.
    """
    
    # Test your hashtable using appropriate methods
    # from your implementation

    with open('student_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ht.setitem(row['id'], (row['name'], row['class']))
            print(ht.getitem(row['id']))
        #f.close is called automatically
    print(ht.getitem('s0002b'))
    print(ht.getitem('s0053c'))
    print(ht.getitem('fsdaaufd'))
    ht.del_item('s0053c')
    print(ht.getitem('s0053c'))