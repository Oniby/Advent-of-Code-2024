import os

def read_full_input(day, step):
    cwd = os.getcwd()
    with open(os.path.join(cwd, '..', 'Inputs', f'Day-{day}-{step}.txt'), 'r') as file:
        file_str = file.read()
    return file_str