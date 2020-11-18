
from src import binary_mask

def test_all_cases():
    
    result = binary_mask.binary_list('01010')
    assert result == ['01010'], result

    result = binary_mask.binary_list('?')
    assert result == ['0', '1'], result

    result = binary_mask.binary_list('??')
    assert result == ['00', '01', '10', '11'], result
    
    result = binary_mask.binary_list('???')
    assert result == ['000', '001', '010', '011', '100', '101', '110', '111'], result

    result = binary_mask.binary_list('1?')
    assert result == ['10','11'], result

    result = binary_mask.binary_list('?10??')
    assert result == ['01000', '01001', '01010', '01011', '11000', '11001', '11010', '11011'], result

    result = binary_mask.binary_list('?????')
    assert result == ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111'], result
    
    result = binary_mask.binary_list('??1??')
    assert result == ['00100', '00101', '00110', '00111', '01100', '01101', '01110', '01111', '10100', '10101', '10110', '10111', '11100', '11101', '11110', '11111'], result
