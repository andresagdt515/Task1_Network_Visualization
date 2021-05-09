# Task1_Network_Visualization

In this repository I uploaded the following files:
- data.json_maker.py <br />
This is the code that returns the provided data in .json format. This was necessary for the 2D force network graph I developed in JavaScript. This one can be visualised in my Web Application [Andres_Web_Application](https://andresagdt515.github.io/Task2_Web_Development/) that is hosted in my second repository [Task2_Web_Development](https://github.com/andresagdt515/Task2_Web_Development). Please, use a computer to visit the Web Application. Platform is not entirely responsive.

- 3Dgraph.ipynb <br />
This is the code to visualise the 3D network graph I developed in Python. To do it I used a library called Jgraph, which gave me problems when running it in a plain python script. Because of that I ended up coding it in a Jupyter Notebook sheet.


## Usage

- data.json_maker.py <br />

    In order to correctly run the file install the required libraries:
    
```bash
pip install -r requirements.txt
```
- 3Dgraph.ipynb <br />

    In order to obtain the correct simulation it is necessary:
    - to split the provided data (raan_case_study interns.xlsx) into 2 .csv files with the following names: edges.csv and nodes.csv, they store the edges and nodes corresponding data.
    - run the code in a Jupyter Notebook
