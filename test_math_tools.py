from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def test_subtract():
    assert subtract(6,2) == 4
    assert subtract(-2,3) == -5
    assert subtract(-2,-8) == 6
    assert subtract(0,0) == 0
    print("test_subtract: ALL PASSED")
    
def test_max_of_three():
    assert max_of_three(1,2,3) == 3
    assert max_of_three(2,2,3) == 3
    assert max_of_three(3,3,3) == 3
    assert max_of_three(-1,-2,-3) == -1 
    assert max_of_three(0,-1,-2) == 0
    print("test_max_of_three: ALL PASSED")

def test_is_palindrome():
    assert is_palindrome("") == True 
    assert is_palindrome("a") == True
    assert is_palindrome("s  s") == True
    assert is_palindrome("yo lo to o t o l o y") == True
    assert is_palindrome("ACHhca") == True
    assert is_palindrome("This is a random line") == False
    print("test_is_palindrome: ALL PASSED")

def test_find_min():
    assert find_min([1,4,7,9,2,9]) == 1
    assert find_min([0,3,5,0]) == 0
    assert find_min([-1,-3,-2,-5,7,8,2,4,0]) == -5
    print("test_find_min: ALL PASSED")

def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1,2,3,4]) == [1,2,3,4]
    assert remove_duplicates([5,5,5,5,5,5,5,5]) == [5]
    assert remove_duplicates([1,"1",2,2.0]) == [1,"1",2]
    assert remove_duplicates(["a","A","b","B"]) == ["a","A","b","B"]
    assert remove_duplicates([2,5,2,9,5,8,6,7,9,4]) == [2,5,9,8,6,7,4]
    print("test_remove_duplicates: ALL PASSED")
    
# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print("--- All tests passed! ---")