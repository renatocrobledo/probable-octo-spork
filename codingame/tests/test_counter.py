from src.counter import run_len_encoding
 

def test_counter():
    data = [
        'AAA',
        'BBB',
        'AAA'
    ]   

    response = '3A3B3A'
    result = run_len_encoding(data)
    assert result == response, result

    data = [
        'AAB',
        'CCC',
        'BAA'
    ]   

    response = '2AB3CB2A' 
    result = run_len_encoding(data)
    assert result == response, result

        
    data = [
        'AAAAA',
        'ABBBA',
        'ABCBA',
        'ABBBA',
        'AAAAA'
    ]   
                
    response = '6A3B2ABCB2A3B6A' 
    result = run_len_encoding(data)
    assert result == response, result

    data = [
        'ABABA',
        'CBCBC',
        'ACACA',
        'BABAB',
        'CBCBC'
    ]   
                
    response = 'ABABACBCBCACACABABABCBCBC' 
    result = run_len_encoding(data)
    assert result == response, result

    data = [
        'AAABAAA',
        'BBBABBB',
        'BBBBBBB',
        'CCCCCCC',
        'BBBBBBB',
        'BBBABBB',
        'AAABAAA'
    ]   
                
    response = '3AB3A3BA10B7C10BA3B3AB3A' 
    result = run_len_encoding(data)
    assert result == response, result