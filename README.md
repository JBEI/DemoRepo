# DemoRepo

This repo is meant to demonstrate best practices with respect to code health and shareability.
It focuses on python code but includes tools for checking on other types of files. Most
of the configurations were copied from the EDD repository.

## Tests

Unit tests for a module are placed in the same directory with the same name plus a _\_test_ suffix.
So unit tests are easy to find and run for any given module.

Integration tests, those which involve use of multiple modules, are placed in their own directory.

We do not provide example end-to-end tests for this repo, but they would also have their own directory
and would run in the context of a non-production service (_eg_ a _staging_ or _dev_ service).

## Pre-commit

Setting up pre-commit is fairly straightforward. This repo includes a _.pre-commit-config.yaml_ file
which sets up the hooks for tools that are run before a commit can complete. These tools help
standardize formatting and clean up code (e.g. remove unused imports) before it is submitted.

To install pre-commit in your env, run:

```pip install pre-commit```

You can then install the pre-commit script in git by running:

```pre-commit install```

If you have a _.pre-commit-config.yaml_ file in your rep, you will notice differences in your next commit.
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

