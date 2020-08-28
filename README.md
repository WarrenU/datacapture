## Steps to Run:
I used python 3.8.2 to run my project. I used type hinting within my project so it will only work with python 3 atleast.

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

 - #5 In your terminal (in your datacapture directory), run: 
`python main.py`

 - #6 Edit `main.py` If you want to try out other data points, or add to the `src/tests.py` file to add more testing criteria. (I have one test case for a dataset of numbers, 1 to 1000.

## Run Tests
To run the testing suite, call:
`python3 -m unittest src/tests.py`
or alternatively:
`python3 -m unittest src.tests`
