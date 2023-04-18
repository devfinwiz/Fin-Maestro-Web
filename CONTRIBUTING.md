# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue with owner or other contributors.

## 1. Keep your Fork up to date
* Before starting development of any new feature, always check if this repo is ahead in commits as compared to your fork.
* It is a good practice to always keep your fork up-to-date before starting development of features/fixes to avoid merge conflicts.
* Create a new branch in order to make contributions.
* Update your fork using following code snippet.
```
# Add a new remote repo called as finmaestro_upstream
git remote add finmaestro_upstream https://github.com/devfinwiz/Fin-Maestro.git

# Sync your fork before starting work
git fetch finmaestro_upstream
git checkout <BRANCH_YOU_ARE_WORKING_ON>
git merge finmaestro_upstream/<BRANCH_FROM_THIS_REPO_YOU_WANT_TO_MERGE_IN_YOUR_BRANCH>
```
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 2. Install Project Dependencies

* This project uses [**TA-Lib**](https://github.com/mrjbq7/ta-lib). Please visit the hyperlink for the official guide of installation.
* Install python dependencies by running `pip install -r requirements.txt` in the root directory of this project.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 3. Create Dependency Requirements

1. Install [**pip-chill**](https://pypi.org/project/pip-chill/) by running `pip install pip-chill` which is a developer friendly version of classic `pip freeze`.
2. Update the `requirements.txt` file by running `pip-chill --all --no-version -v > requirements.txt`.
3. Ensure to **uncomment** all the dependency modules from the `requirements.txt`

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 4. Testing Code Locally

1. Make sure the changes you're making are functioning as expected. Try several test cases before pushing the changes. 
2. In case of a failure, rectify code or consider opening an issue for further discussion.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 5. Pull Request Process

1. Ensure that dependecy list have been generated in the `requirements.txt` using above section.
2. Ensure that all your test-cases are passed locally.
3. Compare your branch with the master, open a pull request and wait for it to be merged or updated with feedbacks before it is merged. 
