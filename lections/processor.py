import os


def create_files_with_dirs(paths):
    for path_inout in paths:
        for path in path_inout:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, 'w') as file:
                    pass


def create_paths(problem, module, tests):
    paths = []
    for i in range(tests):
        test = i+1
        input = f"../inputs/{str(module)}/{problem}/{'input'}_5_{str(module)}_{problem[0]}_test{str(test)}.txt"
        output = f"../inputs/{str(module)}/{problem}/{'output'}_5_{str(module)}_{problem[0]}_test{str(test)}.txt"
        paths.append((input,output))
    return paths

def return_input_output(module, problem, tests, num_of_test):
    paths = create_paths(module=module, problem=problem, tests=tests)
    input, output = paths[num_of_test-1]
    create_files_with_dirs(paths)
    return input, output


# read file
def read_int_arr_line(file):
    return int(file.readline().strip())

def read_list_of_tuple(file, len_tupels):
    result_list = []
    for _ in range(len_tupels):
        x, y = file.readline().strip().split()
        result_list.append((float(x),float(y)))
    return result_list

# scan input 
def scan_file_input(input, func):
    file = open(input, 'r')
    parameters = func()
    file.close()
    return parameters

# scan output 
def scan_file_output(output, func):
    file = open(output, 'r')
    parameters = func()
    file.close()
    return parameters