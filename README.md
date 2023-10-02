# Sync
College project for Project Exhibition - I.

## About This Branch
### General Info
This is the testing branch. <br>
The base branch which is also the default branch for this repository is 'main' which is locked. <br>

### Branch Functionality
This branch is also responsible for hosting the website. Hence any changes made to this branch would be reflected on the website.
Once the website is complete, the testing branch will be fully merged with the main branch. Hence all pull requests would 
first be made only to the testing branch. In other words <br>

### About Sub-Branches
The testing branch has two sub-branches, 'front' and 'back'. The front end would be coded on the front branch while the back end would be integrated on the back branch. Once any changes are made the front branch will open a pull request to the testing branch, once approved the testing branch will have the latest front end code. This latest code would then be pulled by atharv sathe on his local machine who will then push the back branch to the testing branch, this would then be merged to the testing branch on the remote repo. The testing will thus have the latest front and back code. Once entire website is finished the testing branch would be merged back to main branch.<br>

### Branch Protection Rules for this Branch
1. No Collaborator other than the owner(Atharv-Sathe) can directly push any changes to this branch.
2. Collaborators need to push changes to either front or back branche and then open a pull request in order to get approval for merging changes(commits) to testing branch.
3. Pull Request thus created can only be approved upon reviewing by the owner (Atharv-Sathe).
4. Other collaborators are expected not to approve any pull request to the testing branch, however they can very well review the pull request, comment or request for changes. In fact collaborators are encouraged to do so(review, comment or request changes).