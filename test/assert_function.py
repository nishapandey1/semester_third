

def test_sum():
    assert sum ([1,4,5,6])==16, "should be 16"

def test_tuple_sum():
    assert sum ((1,2,3,4))==10, "Must be 10"

if __name__=="__main__":
    test_sum()
    test_tuple_sum()
    print("successfully executed")