# DemoRepo

[![codecov](https://codecov.io/gh/JBEI/DemoRepo/branch/main/graph/badge.svg?token=ZOXSD5WM3G)][1]

Maintaining Code health is fundamental if you want someone else to understand and use your code.
In this repository we intend to demonstrate best practices with respect to code health and
shareability. We will mainly focus on two practices that will make your code more likely to be used
by other people: tests and pre-commit hooks. [Tests][2] are meant to ensure that, if someone
modifies the code, they can check they did not break any of its main functionality. Pre-commit
hooks are preprocessing scripts that ensure that your file conforms to a more readable code format
([Black][3] in an [example of this][4]). Most of the configurations were copied from the
[EDD repository][5].

The repo has two simple python modules, _counter.py_ and _service.py_, which are meant only
to illustrate use of the styling and testing approaches and tools.

We would like to keep the styling configs up-to-date so that as many people as possible are
all using the same styles to improve readability of code across projects. Feel free to
contribute suggestions for modifying these configs.

This repo is designated as a **template** so that **you can create a new repo based on this one**.
See the _Using DemoRepo as a Template_ section below to get more info on this process.

## Tests

Unit tests for a module are placed in the same directory with the same name plus a _\_test_ suffix.
This makes unit tests easy to find and run for any given module and also makes obvious which
modules do not have unit tests.

Integration tests, those which involve use of multiple modules, are placed in their own directory.

We do not provide example end-to-end tests for this repo, but they would also have their own
directory and would run in the context of a non-production service (_eg_ a _staging_ or _dev_
service).

### Test Coverage

Install the test coverage tool:

`pip install coverage`

This tool is called in the _run_all_tests.sh_ script. It will show you a text description of the
coverage if the tests all pass, and it will generate a directory of html that gives a more
detailed description of the coverage. You can access this by running:

`open htmlcov/index.html`

This can be very useful for inspecting uncovered parts of the code. For example, in this repo we
adopt a style that all python should have an executable main(), even if it is intended to be used
as a library module. We do _not_ test this code, which you can see when you inspect the coverage
details:

![missing coverage][6]

### Testing Notebooks

DemoRepo contains two jupyter notebooks in _/notebooks_. This directory also contains a script
to run the notebooks with _runipy_. To run this script, install runipy:

`pip install runipy`

You can then run the script:

`./run_notebook_tests.sh`

Note that these tests only ensure that the notebooks can execute; they do not test correctness of
the notebook code.

For demonstration purposes, the directory contains one notebook that succeeds,
_WorkingDemoRepoNotebook.ipynb_, and one that fails, _FailingDemoRepoNotebook.ipynb_.

## Pre-commit

Setting up pre-commit is fairly straightforward. This repo includes a _.pre-commit-config.yaml_
file which sets up the hooks for tools that are run before a commit can complete. These tools help
standardize formatting and clean up code (e.g. remove unused imports) before it is submitted.

To install pre-commit in your env, run:

`pip install pre-commit`

You can then install the pre-commit script in git by running:

`pre-commit install`

If you have a _.pre-commit-config.yaml_ file in your repo, you will notice differences in your next
commit. The tools specified in _.pre-commit-config.yaml_ will run and will block the commit if any
errors are found. It may be helpful to run the tools directly when you are trying to fix these
errors.

For the python tools _black_ and _flake8_, install the tools with:

```
pip install black
pip install flake8
```

If you have errors in say _myfile.py_, you can fix the formatting errors with:

`black myfile.py`

Don't forget to add the changes to the staged area before you retry your commit.

For _flake8_ errors, you can list them by running _flake8_ directly, but you
may have to make fixes by hand.

`flake8 myfile.py`

Note that there are some helpful tips on using pre-commit in different ways on
the [ART Install page][7].

## Automated Documentation

A [separate document][8] is available describing how to set up Sphinx for auto-generation of
documents for this project. The steps should be comparable for any project using this project as a
template.

## Using DemoRepo as a Template

Follow the steps below to create a new repo using DemoRepo as a template:

1. Go to the [DemoRepo GitHub page][9] and click the _Use this template_ button. Pick a name for
   your new template and create it.
2. Clone the new repo for editing.
3. Remove the notebooks in _/notebooks/_.
4. Remove the images in _/images/_.
5. Remove the python files in _/demo_repo/_ and _/demo_repo/integration_tests/_.
6. Rename the _/demo_repo/_ source directory to the name of your repo. Update the directory name
   in _run_all_tests.sh_.
7. Modify _setup.py_ as needed for your repo.
8. Go to [CodeCov repository page][10] and add your new repo.
9. Go to the _Settings_ your repo in CodeCov and copy the _Repository Upload Token_. Edit the
   _codecov.yml_ file in your local repo and replace the token with the one you copied.
10. Update the markdown README file for your repo. Note that you will want to get a new code
    coverage badge which is available in _Settings_ under the _Badge_ section (left-hand panel).
    For example, the link to the badge for the DemoRepo project is available [here][11].
11. Double check set up instructions in the DemoRepo README to ensure that pre-commit is ready to
    go.

---

[1]: https://codecov.io/gh/JBEI/DemoRepo
[2]: https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
[3]: https://github.com/psf/black
[4]: https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARUAmtdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTRFyNsHRkoRBLruYzynsdQIZlZ2M2AAAE3z3tcACOrHAAGHBdUIAADeZ5kXscRn-wIAAAAABFla
[5]: https://github.com/JBEI/EDD
[6]: images/missing_coverage.png
[7]: https://github.com/JBEI/AutomatedRecommendationTool/blob/master/docs/Installing.md
[8]: https://docs.google.com/document/d/1xT5Ay4Ua7F5cX_-tG9iEuOd7B0yTREuAh47GkKAlZt8/edit
[9]: https://github.com/JBEI/DemoRepo
[10]: https://codecov.io/gh/JBEI
[11]: https://app.codecov.io/gh/JBEI/DemoRepo/settings/badge
