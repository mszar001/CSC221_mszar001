import final

def test_MinMaxSum2():
    result = final.func.MinMaxSum2(5,1,8,17,2,5)
    assert result == (1, 17, 38)

def test_funct():
    result = final.func.funct(45)
    assert result == '45 is between 5 and 50'

def test_SieveOfEratosthenes():
    result = final.func.SieveOfEratosthenes(20)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19]