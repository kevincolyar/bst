from testfixtures import LogCapture

from search.bst import Bst, Node, StdOutVisitor, DepthVisitor, DeepestVisitor, DeepestOutputVisitor, SearchVisitor

# def foo_test():
#     assert 1 == 1

# def bst_print_test():
#     bst()

# def bst_input_test():
#     assert Bst(12,11,90,82,7,9).output() == 'deepest, 9; depth, 3'

# def bst_input_one_test():
#     assert Bst(12).output() == 'deepest, 12; depth, 1'

# def bst_input_two_test():
#     assert Bst(12,11).output() == 'deepest, 12; depth, 1'

# def node_insert_less_than_test():
#     # print(Node().insert(12).insert(11).output())
#     assert Node().insert(12).insert(11).output() == '((None) 11 (None)) 12 (None)'

# def bst_test():
#     assert Bst(12, 11).output() == '((None) 11 (None)) 12 (None)'

# def node_insert_greater_than_test():
#     assert Node().insert(12).insert(13).output() == '(None) 12 ((None) 13 (None))'

def bst_visitor_test():
    assert Bst(12,11).visit(StdOutVisitor()) == '((None) 11 (None)) 12 (None)'

def bst_visitor_two_test():
    assert Bst(12,13).visit(StdOutVisitor()) == '(None) 12 ((None) 13 (None))'

def depth_visitor_two_test():
    assert Bst(12,13).visit(DepthVisitor()) == '(None) 12;0 ((None) 13;1 (None))'

def depth_visitor_three_test():
    assert Bst(12,13,14).visit(DepthVisitor()) == '(None) 12;0 ((None) 13;1 ((None) 14;2 (None)))'

def depth_visitor_insert_test():
    assert Bst(12,13).insert(14).visit(DepthVisitor()) == '(None) 12;0 ((None) 13;1 ((None) 14;2 (None)))'

def depth_visitor_three_test():
    assert Bst(12,11,90,82,7,9).visit(DepthVisitor()) == \
        '(((None) 7;2 ((None) 9;3 (None))) 11;1 (None)) 12;0 (((None) 82;2 (None)) 90;1 (None))'

def deepest_visitor_one_test():
    memo = Bst(12,11,90,82,7,9).visit(DeepestVisitor())
    depth = sorted(memo.keys())[-1]
    deepest = ', '.join({str(i) for i in memo[depth]})
    desc = f'deepest, {deepest}; depth, {depth}'

    assert desc == 'deepest, 9; depth, 3'

def deepest_output_test():
    assert Bst(12,11,90,82,7,9).visit(DeepestOutputVisitor()) == 'deepest, 9; depth, 3'

def search_visitor_test():
    assert Bst(12,11,90,82,7,9).visit(SearchVisitor(), 90) == 90

def bst_search_test():
    assert Bst(12,11,90,82,7,9).search(90) == 90

def empty_test():
    assert Bst().visit(StdOutVisitor()) == '(None) None (None)'

def duplicate_keys_test():
    assert Bst(1, 1).visit(StdOutVisitor()) == '(None) 1 (None)'

def float_test():
    assert Bst(2.0, 1.0, 3.0).visit(StdOutVisitor()) == '((None) 1.0 (None)) 2.0 ((None) 3.0 (None))'

# def bst_log_test():
#     with LogCapture() as l:
#         bst()
#         l.check(('search.bst',
#         'INFO',
#         'foo'))
