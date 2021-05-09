# Task1_Network_Visualization

In this repository I uploaded the following documents:
- data.json_maker.py <br />
This is the code that returns the provided data in .json format. This was necessary for the 2D force network graph I developed in JavaScript. This one can be visualised in the following Web Application [Andres_Web_Application](https://andresagdt515.github.io/Task2_Web_Development/), in my second repository [Task2_Web_Development](https://github.com/andresagdt515/Task2_Web_Development).

- 3Dgraph.ipynb <br />
This is the code to visualise the 3D network graph I developed in Python. To do it I used a library called Jgraph, which gave me problems when running it in a plain python script. Because of that I ended up coding it in a Jupyter Nottebook sheet.


## Usage

- data.json_maker.py <br />
In order to correctly run the file it is necessary:
   - install pandas
   - install json

- 3Dgraph.ipynb <br />
In order to obtain the correct simulation it is necessary:
   - to split the provided data (raan_case_study interns.xlsx) into 2 .csv files with the following names: edges.csv and nodes.csv, that store the edges and nodes corresponding data.
   - run the code in a Jupyter Notebook

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas and json libraries

```bash
pip install pandas
```
```bash
pip install json
```