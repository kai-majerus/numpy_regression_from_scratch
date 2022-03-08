<!-- Add banner here -->
![Red and Black Thompson Soccer Club Logo](https://user-images.githubusercontent.com/53292276/156609919-ca361c36-85d4-46f0-81c0-ace4919d139d.png)


# Regression From Scratch

<!-- Add buttons here -->
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

This aim of this project is to build multiple regression models from scratch using NumPy rather than scikit-learn. I hope to improve my understanding of 4 regression models (namely, Linear Regression, Ridge Regression, Lasso Regression and Decision Tree Regression) and OOP in doing so.

The dataset that I will be using is a small dataset of ~ 200 football players with 12 feature variables and a target variable of the players 'score'.

Tech stack
* Language - Python
* Libraries - Pandas, NumPy

# Demo-Preview
[(Back to top)](#table-of-contents)

Follow the setup/installation instructions below to install the package and then run the command `numpy_regression_from_scratch-run`. This will run main.py, which trains and saves a model for each of linear, lasso, ridge and tree regression. The output will be the MSE and R2 Score of each model (see example output below). 

![image](https://user-images.githubusercontent.com/53292276/157235956-89a91ace-41ca-4797-bbc6-9bf307e1df5c.png)

# Table of contents

- [Project Title](#regression-from-scratch)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Startup the project](#startup-the-project)
- [Installation](#installation)
- [Footer](#footer)

# Startup the project
[(Back to top)](#table-of-contents)
The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for numpy_regression_from_scratch in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/numpy_regression_from_scratch`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "numpy_regression_from_scratch"
git remote add origin git@github.com:{group}/numpy_regression_from_scratch.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
numpy_regression_from_scratch-run
```

# Installation
[(Back to top)](#table-of-contents)

Go to `https://github.com/{group}/numpy_regression_from_scratch` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/numpy_regression_from_scratch.git
cd numpy_regression_from_scratch
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
numpy_regression_from_scratch-run
```

# Footer
[(Back to top)](#table-of-contents)

![footer_video](https://user-images.githubusercontent.com/53292276/156608882-fd58c52c-6aec-4710-9544-54529ba4eba0.gif)
