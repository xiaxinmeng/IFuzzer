## IFuzzer: Hunting for interpreter bugs with tree-based SPE approach


### About this project

This project is for the paper "Enumerating Non-Alpha-Equivalent Programs for Interpreter Testing." In the paper, we developed a tree-based skeletal program enumeration (SPE) algorithm that can quickly detect a diversity of interpreter bugs. Our approach models the SPE on a tree structure, in which every path is associated with a derived test program. In this process, we can (1) confine the variable set for filling holes to directly generate non-alpha-equivalent programs and (2) apply dependency analysis to avoid invalid programs using undefined variables. This project presents the tool implementation of our tree-based SPE algorithm called IFuzzer.

IFuzzer is efficient as it only takes 61% of the time cost of the state-of-the-art combinatorial SPE and reveals 1.5 times more bugs with the same number of 200 testing seeds, improving the best 5.3% source code function coverage in the same 100 hours of testing. In less than two months, IFuzzer identified 136 bugs: 81 of them have been confirmed to be unique and valid, and 30 of them have been fixed. Developers gave positive responses for most of these reported bugs, e.g., "This is a real bug", "Thanks a lot for the report." Particularly, five bugs even attracted the interests of the "father of Python," Guido van Rossum. He confirmed all of them to be previously unknown, fixed two of them himself, and commented on our fuzzing work, "It's good work!" in the CPython issue trackers.




#### How to run IFuzzer 

1. Enter working directory.
   - cd IFuzzer

2. Configure Python interpreters.
   - open run.py, change the path of variable "interpreter" (i.e. line 231 in run.py) into your tested Python interpreter.
   e.g. interpreter =  '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/Python-3.9.0/python' -> interpreter = "python3.9"

3. Configure dataset.
   - put your test seed in dataset directory and open run.py, change the dataset path "tdir" (i.e. line 286 in run.py) into your dataset path.
   e.g. tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/IFuzzer/IFuzzer/dataset/'

4. run IFuzzer.
   - execute  command "python3 run.py" in command line.

5 collect the execution results
   - all log files and crash programs are stored in IFuzzer/IFuzzer/log and IFuzzer/IFuzzer/errors, automatically.
   


### How to run SPE for Python

1. Enter working directory.
   - cd SPE_python

2. Configure dataset.
   - put your test seed in dataset directory and open run.py, change the dataset path "tdir" (i.e. line 19 in run.py) into your dataset path.

3. Configure Python interpreters.
   - open SPE_Python.py, change the interpreter path "interpreter" (i.e. line 162 in SPE_Python.py) into your tested Python interpreter.
   e.g. interpreter =  '/home/xxm/Desktop/IFuzzer/Python-3.9.0/python' -> interpreter = "python3.9"

4. run SPE
   - e.g. execute "python3 run.py" in command line.

5. check the execution results
   - all log files and crash programs are stored in  /SPE/log or /SPE/errors



 



