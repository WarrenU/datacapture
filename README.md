# Steps to Run:
I used python 3.8.2 to run my project. This code should work with python 2 as well.

 - #1 Clone the project:
`git clone https://github.com/WarrenU/datacapture.git`

 - #2
Change to the directory of the project:
`cd datacapture`

 - #3 Make a python virtual environment
`python3 -m venv /venv`

- #4
Activate the virtual environment
`. /venv/bin/activate`

 - #5 **Run** From the main project directory, where main.py is accessible run the project by calling
`python main.py`

 - #6 Edit `main.py` If you want to try out other data points, or add to the `src/tests.py` file to add more testing criteria. (I have one test case for a dataset of numbers, 1 to 1000.

## Run Tests
To run the testing suite, call:
`python3 -m unittest src/tests.py`