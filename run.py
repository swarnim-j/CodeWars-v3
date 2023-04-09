import subprocess
import time
import os

process0 = subprocess.Popen(["python3", "compile.py"], stdout=subprocess.PIPE)

for j in range(4):
    with open(f'./player{j}/{j}.txt', 'w') as f:
        process = subprocess.Popen(["python3", f"player{j}/{j}.py"], stdout=f)

os.chdir("Object")

n = 4

commands = [[f"./main {n} 6000"], *[[f"./client {i} 127.0.0.1 6000"] for i in range(4)]]

processes = []

for i, command in enumerate(commands):
    process = subprocess.Popen(command, shell=True)
    processes.append(process)
    if i == 0:
        time.sleep(6)