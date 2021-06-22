from src import particles_size

from tests import mock_input

'''
 Just run "pytest" and this will look for files which beggins with test_ or ends with _test then will execute all functions starting by test_
'''
def test_all():
    mock_input.inyect_all_files_and_assert_condition_with_last_line(f"./tests/particles_size_data", particles_size.main)
