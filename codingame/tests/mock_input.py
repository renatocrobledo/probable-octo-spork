import mock
import builtins
import os


def inyect(entries, callback, expected_result, test_file = '', debug_test = False, ):
    
    def input_generator(entries):
        for n in entries:
            yield n

    _input = input_generator(entries)

    with mock.patch.object(builtins, 'input', lambda: next(_input)):
        
        if debug_test:
            result = callback(debug_test)
        else:
            result = callback()

        assert result == expected_result, f'result: {result} != {expected_result}, testfile: {test_file}'


def inyect_file_and_assert_condition(file_path, condition_function):

    f = open(file_path, "r") # its expected to be executed from the root   
    entries = f.read().split('\n')[:-1] # [:-1] ->  getting rid of the last empty tring

    inyect(entries, condition_function, True, file_path)


def inyect_all_files_and_assert_condition_with_last_line(file_path_folder, condition_function, debug_test_number = None):

    for filename in sorted(os.listdir(file_path_folder)):
        f = open(f'{file_path_folder}/{filename}', "r")  
        entries = f.read().split('\n')
        expected_result = entries.pop() # the last entry will be the expected result...
        
        if expected_result == '':
            expected_result = entries.pop() # maybe is a new empty line at the bottom of the file...

        debug_test = False
        if filename == debug_test_number or debug_test_number:
            debug_test = True 
        inyect(entries, condition_function, expected_result, filename, debug_test)