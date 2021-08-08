from src import polygon_angles
from tests import mock_input

def test_all_cases():
    mock_input.inyect_all_files_and_assert_condition_with_last_line(f"./tests/polygon_angles_data", polygon_angles.calculate_sides)    