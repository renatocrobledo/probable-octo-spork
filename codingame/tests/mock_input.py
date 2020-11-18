import mock
import builtins


def inyect(entries, callback, expected_result):
    
    def input_generator(entries):
        for n in entries:
            yield n

    _input = input_generator(entries)

    with mock.patch.object(builtins, 'input', lambda: next(_input)):

        result = callback()
        assert result == expected_result, result


def inyect_file_and_assert_condition(file_path, condition_function):

    f = open(file_path, "r") # its expected to be executed from the root   
    entries = f.read().split('\n')[:-1] # [:-1] ->  getting rid of the last empty tring

    inyect(entries, condition_function, expected_result=True)