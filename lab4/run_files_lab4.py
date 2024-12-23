import os
import subprocess

list_tasks = ["2","3","6","7","10","13_1","13_2"]

print('#' * 85 + '\n')

for i in list_tasks:
    os.chdir(f'task{i}/src/')
    print(f'\033[36mRUNNING TASK #{i}\033[0m')
    path_test = f'task{i}.py'
    result = subprocess.run(['python',path_test], capture_output=True, text=True).stderr
    if result:
        print()
        print(f"\033[31m{result}\033[0m", end='')
    print()
    print('#'*85+'\n')
    os.chdir(f'../..')