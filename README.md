# DemoRepo

[![codecov](https://codecov.io/gh/JBEI/DemoRepo/branch/main/graph/badge.svg?token=ZOXSD5WM3G)](https://codecov.io/gh/JBEI/DemoRepo)

This repo is meant to demonstrate best practices with respect to code health and shareability.
It focuses on python code but includes tools for checking on other types of files. Most
of the configurations were copied from the EDD repository.

The repo has two simple python modules, *counter.py* and *service.py*, which are meant only
to illustrate use of the styling and testing approaches and tools.

We would like to keep the styling configs up-to-date so that as many people as possible are
all using the same styles to improve readability of code across projects. Feel free to 
contribute suggestions for modifying these configs.

This repo is designated as a template so that you can create a new repo based on this one. See the *Using
DemoRepo as a Template* section below to get more info on this process.

## Tests

Unit tests for a module are placed in the same directory with the same name plus a _\_test_ suffix. This
makes unit tests easy to find and run for any given module and also makes obvious which modules do not
have unit tests.

Integration tests, those which involve use of multiple modules, are placed in their own directory.

We do not provide example end-to-end tests for this repo, but they would also have their own directory
and would run in the context of a non-production service (_eg_ a _staging_ or _dev_ service).

### Test Coverage

Install the test coverage tool:

```pip install coverage```

This tool is called in the _run_all_tests.sh_ script. It will show you a text description of the
coverage if the tests all pass, and it will generate a directory of html that gives a more
detailed description of the coverage. You can access this by running:

```open htmlcov/index.html```

This can be very useful for inspecting uncovered parts of the code. For example, in this repo we 
adopt a style that all python should have an executable main(), even if it is intended to be used
as a library module. We do _not_ test this code, which you can see when you inspect the coverage details:

![missing coverage](images/missing_coverage.png)


### Testing Notebooks

DemoRepo contains two jupyter notebooks in */notebooks*. This directory also contains a script
to run the notebooks with *runipy*. To run this script, install runipy:

```pip install runipy```

You can then run the script:

```./run_notebook_tests.sh```

Note that these tests only ensure that the notebooks can execute; they do not test correctness of
the notebook code.

For demonstration purposes, the directory contains one notebook that succeeds, *WorkingDemoRepoNotebook.ipynb*,
and one that fails, *FailingDemoRepoNotebook.ipynb*.

## Pre-commit

Setting up pre-commit is fairly straightforward. This repo includes a _.pre-commit-config.yaml_ file
which sets up the hooks for tools that are run before a commit can complete. These tools help
standardize formatting and clean up code (e.g. remove unused imports) before it is submitted.

To install pre-commit in your env, run:

```pip install pre-commit```

You can then install the pre-commit script in git by running:

```pre-commit install```

If you have a _.pre-commit-config.yaml_ file in your repo, you will notice differences in your next commit.
The tools specified in _.pre-commit-config.yaml_ will run and will block the commit if any
errors are found. It may be helpful to run the tools directly when you are trying to fix these errors.

For the python tools _black_ and _flake8_, install the tools with:

```
pip install black
pip install flake8
```

If you have errors in say _myfile.py_, you can fix the formatting errors with:

```black myfile.py```

Don't forget to add the changes to the staged area before you retry your commit.

For _flake8_ errors, you can list them by running _flake8_ directly, but you 
may have to make fixes by hand.

```flake8 myfile.py```

Note that there are some helpful tips on using pre-commit in different ways on
the [ART Install page](https://github.com/JBEI/AutomatedRecommendationTool/blob/master/docs/Installing.md).

## Using DemoRepo as a Template

Follow the steps below to create a new repo using DemoRepo as a template:

1. Go to the [DemoRepo GitHub page](https://github.com/JBEI/DemoRepo) and click the *Use this template* button. Pick a name for your new template and create it.
2. Clone the new repo for editing.
3. Remove the notebooks in */notebooks/*.
4. Remove the images in */images/*.
5. Remove the python files in */demo_repo/* and */demo_repo/integration_tests/*.
6. Rename the */demo_repo/* source directory to the name of your repo. Update the directory name in *run_all_tests.sh*.
7. Modify *setup.py* as needed for your repo.
8. Go to [https://codecov.io/gh/JBEI] and add your new repo.
9. Go to the *Settings* your repo in CodeCov and copy the *Repository Upload Token*. Edit the *codecov.yml* file in your local repo and replace the token with the one you copied.
10. Update the markdown README file for your repo.
11. Double check set up instructions in the DemoRepo README to ensure that pre-commit is ready to go.


