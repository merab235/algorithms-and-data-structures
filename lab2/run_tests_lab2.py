import subprocess
import os
import time

list_tasks = [1,3,4,5,6,7]
list_passed_tasks = []
list_failed_tasks = []

print('#' * 85 + '\n')

tests_start_time = time.perf_counter()


for i in list_tasks:
    os.chdir(f'task{i}/tests/')
    print(f'\033[36mTEST TASK #{i}\033[0m')
    path_test = f'test_task{i}.py'
    result = subprocess.run(['pytest','--tb=no',path_test], capture_output=True, text=True).stdout
    if 'passed' in result:
        print(f"\033[32m{result}\033[0m")
        list_passed_tasks.append(i)
    else:
        print(f"\033[31m{result}\033[0m")
        list_failed_tasks.append(i)
    print('#' * 85 + '\n')
    os.chdir(f'../..')

print(f'Passed tasks:', *list_passed_tasks)
print()
print(f'Failed tasks:', *list_failed_tasks)
print()
print(f'Execution Time: {round(time.perf_counter()-tests_start_time,5)} sec' )
print()
print('#'*85+'\n')