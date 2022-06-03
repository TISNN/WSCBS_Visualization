[![DOI](https://zenodo.org/badge/498507875.svg)](https://zenodo.org/badge/latestdoi/498507875)

# WSCBS_Assignment4b_brane_Visualization

This implementation is the visualization part of Titanic Project ([Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)).

## Usage
This is the **fourth** package in our pipeline of project([Assignment 4b](https://github.com/TISNN/WSCBS_Assignment4b)). We uses visualization package: `seaborn` and `matplotlib` to generate plots.

Each package, as a part in the brane pipeline, can be run separately to produce the corresponding results (processed data, ML models, visualization)

## Requirements

- Complete installation of Brane ([manual1](https://wiki.enablingpersonalizedinterventions.nl/user-guide/software-engineers/installation.html), [manual2](https://wiki.enablingpersonalizedinterventions.nl/admins/installation/get-binaries.html))
- Brane Dependencies (also in [manual1](https://wiki.enablingpersonalizedinterventions.nl/user-guide/software-engineers/installation.html), [manual2](https://wiki.enablingpersonalizedinterventions.nl/admins/installation/get-binaries.html))

## Setup

### By source code (Git repository)

1. Download the source code by `git clone`
```shell
$ git clone https://github.com/TISNN/brane_visualization.git
$ cd brane_visualization
```
2. Build brane package by .yml file
```shell
$ brane build container.yml
```
3. Check availablity
```shell
$ brane list
```

### By brane package method

1. import brane package
```shell
$ brane import TISNN/brane_visualization
```
2. Check availablity
```shell
$ brane list
```

If you see `visual` package with version==8.0.0, it was successfully built.

## Run
```shell
$ brane --debug test --data ./data visual
```
1. Choosing the plot you'd like to generate
2. Enter "**EDA**" as source string
3. It runs correctly with output "Successful! Figure saved to <>"
4. The figure will be save to `./data` folder in your local file system.

## Tests for package
### Automated builds and running (CI/CD)
This repository is equipped with a GitHub Action workflow. 

Every time we push the code to this repository, it will automatically run the tests using branescript. The build status of the project can be viewed on the [Actions](https://github.com/TISNN/brane_visualization/actions) page.

- The `brane` is the executable compiled binary file, used for automated testing.
- The `test.txt` is the branescript used for automated testing.

### Unit pytest
You also can test for a single function by python. 

Parameters can be changed in file: `pytest.py`
```shell
$ python pytest.py
```
