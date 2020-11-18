from src import robber
from tests import mock_input

'''
 Just run "pytest" and this will look for files which beggins with test_ or ends with _test then will execute all functions starting by test_
'''

def run_with_log_and_expect_result(log_index, result):

    condition = lambda: robber.look_for_robber() == result

    mock_input.inyect_file_and_assert_condition(f"./tests/robber_data/log_{log_index}", condition)


def test_all_robber_cases():
    run_with_log_and_expect_result('1','9651')
    run_with_log_and_expect_result('2','5637')
    run_with_log_and_expect_result('3','9651')
    run_with_log_and_expect_result('4','4477')
    run_with_log_and_expect_result('5','6996')


test_all_robber_cases()
