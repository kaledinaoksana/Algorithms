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
