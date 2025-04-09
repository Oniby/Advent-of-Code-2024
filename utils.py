import os

def read_full_input(day, testing):
    cwd = os.getcwd()
    if testing:
        input_path = os.path.join(cwd, '..', 'Inputs', f'Day-{day}-T.txt')
    else:
        input_path = os.path.join(cwd, '..', 'Inputs', f'Day-{day}.txt')
    with open(input_path, 'r') as file:
        file_str = file.read()
    return file_str