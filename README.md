DISCRIPTION:
-
The code is just an implementation of the research paper under the title<br>
"A Genetic Algorithm for Solving a Container Storage Problem Using a Residence Time Strategy"
<br>
We used a normal code(with out any Metaheuristic Algorithm)<br>
and the Genetic Algorithm(GA), and the Biography Based Optimization(BBO) Algorithm ::Metaheuristics.<br>

There isn't to much to say, so please read the research paper:: <br>
paperResources/A Genetic Algorithm for Solving a Container Storage Problem Using a Residence Time Strategy.pdf

THE HIRARCHY:
-
```
Optim/
├── algorithms
│   ├── __init__.py
│   ├── bbo
│   │   ├── __init__.py
│   │   ├── bbo.py
│   │   └── init.py
│   ├── ga
│   │   ├── __init__.py
│   │   ├── ga.py
│   │   └── init.py
│   └── normal
│       ├── __init__.py
│       └── normal.py
├── benchmarks
│   ├── __init__.py
│   ├── time.py
│   └── Untitled 1.pdf
├── paperResources
│   ├── A Genetic Algorithm for Solving a Container Storage Problem Using a Residence Time Strategy.pdf
│   └── BBO_Simon.pdf
├── tests
│   ├── 10k.txt
│   ├── 1M.txt
│   ├── Bbo.txt
│   ├── __init__.py
│   ├── Ga.txt
│   ├── graphs.py
│   ├── testBbo.py
│   └── testGa.py
├── __init__.py
├── README.md
├── solution.py
└── tools.py

```
    
HOW TO READ THE SOURCE CODE:
---------------
1. solution .py
2. tools .py
3. benchmarks.*
4. algorithms
    1. algorithms.normal.*
    2. algorithms. ga.*
    3. algorithms.bbo.*
5. fitch into the test file,
   >The text files are the results of the tests performed
   using the files: test*.py
6. >The paper resources, one for the theses and the other for the
    Bbo Algorithm tutorial.


TOOLS:
-
* Language
	* Python 3.5

* Libraries
	* matplotlib
	* numpy
	* scipy
	> For the graphs
 
Contributors:
-
* HERHAR Fares, Khaled Kesmia
* DZ, Algeria
* https://github.com/HerharFares
* https://github.com/KKesmia