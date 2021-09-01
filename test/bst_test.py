from search.bst import Bst

def bst_one_node_test():
    assert Bst(12).deepest() == 'deepest, 12; depth, 0'

def bst_two_nodes_test():
    assert Bst(12, 11).deepest() == 'deepest, 11; depth, 1'

def bst_list_test():
    assert Bst(12, 11, 90, 82, 7, 9).deepest() == 'deepest, 9; depth, 3'

def bst_multiple_at_same_depth_test():
    assert Bst(2, 1, 3).deepest() == 'deepest, 1,3; depth, 1'

def bst_insert_test():
    assert Bst()    \
        .insert(12) \
        .insert(11) \
        .insert(90) \
        .insert(82) \
        .insert(7)  \
        .insert(9)  \
    .deepest() == 'deepest, 9; depth, 3'

def depths_test():
    assert Bst(12,13).depths() == '(None) 12:0 ((None) 13:1 (None))'

def depths_two_test():
    assert Bst(12,13).depths() == '(None) 12:0 ((None) 13:1 (None))'

def depths_list_test():
    assert Bst(12,13,14).depths() == '(None) 12:0 ((None) 13:1 ((None) 14:2 (None)))'

def depth_insert_test():
    assert Bst(12,13).insert(14).depths() == '(None) 12:0 ((None) 13:1 ((None) 14:2 (None)))'

def depth_test():
    assert Bst(12,11,90,82,7,9).depths() == \
        '(((None) 7:2 ((None) 9:3 (None))) 11:1 (None)) 12:0 (((None) 82:2 (None)) 90:1 (None))'

def bst_search_test():
    assert Bst(12,11,90,82,7,9).search(90) == 90

def bst_search_not_found_test():
    assert Bst(12,11,90,82,7,9).search(0) == None

def bst_empty_test():
    assert Bst().depths() == '(None) None:0 (None)'

def bst_duplicate_keys_test():
    assert Bst(1, 1).depths() == '(None) 1:0 (None)'

def bst_float_test():
    assert Bst(2.0, 1.0, 3.0).depths() == '((None) 1.0:1 (None)) 2.0:0 ((None) 3.0:1 (None))'
