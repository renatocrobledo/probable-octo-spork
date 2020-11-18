from src import molecules
from tests import mock_input

'''
 Just run "pytest" and this will look for files which beggins with test_ or ends with _test then will execute all functions starting by test_
'''

def expect_result(log_index, result):

    method_1 = lambda: molecules.calculate_1() == result

    mock_input.inyect_file_and_assert_condition(f"./tests/molecules_data/{log_index}", method_1)

def test_all_cases():

    
    #    CO2
    # (12.011) + (15.999 * 2)
    expect_result('1', '44.009')
    #  C19 H29 COOH
    # (12.011*19) + (1.008 * 29) + (12.011) + (15.999) + (15.999) + (1.008) 313.461
    expect_result('2', '302.458')
    expect_result('3', '146.190')
    expect_result('4', '12950.217')
    
    