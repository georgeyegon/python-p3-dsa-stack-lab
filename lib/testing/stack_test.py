import pytest
from Stack import Stack

def test_full():
    """Test Stack full() method"""
    stk = Stack([1], 1)  # Stack with 1 item and max size 1
    assert stk.full()  # Stack should be full
    assert stk.size() == 1
    
    # Pop the only item in the stack
    assert stk.pop() == 1
    
    # Push a new item into the stack
    stk.push(1)
    
    try:
        stk.push(2)  # This should raise an OverflowError because the stack is full
        assert False, "Expected OverflowError"
    except OverflowError:
        pass  # Test passes if OverflowError is raised
