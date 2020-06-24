# GitHub workflow

To contribute content to this repository (repo), use the GitHub workflow described here.
To follow the entire contribution process, go to
[CONTRIBUTING.md](CONTRIBUTING.md).

**Note:** This workflow shows how to make changes to the repo from the command line by
using git commands. If you do not want to use the command line, you can use GitHub Desktop
or another GitHub GUI instead to accomplish the steps.


## Prerequisite

* [Generate SSH keys](https://help.github.com/articles/generating-ssh-keys/)

## Workflow

1. Create a fork of this repo.

2. In a directory (of your choice) on your computer, use the ssh URL for the
   forked repo to clone it to your local system. You can use the **Clone**
   button in the repo to copy the URL and paste it after `git clone` as shown
   in the following example:

    ```bash

    git clone git@github.com:my-github-username/docs-style-guide.git

    ```

3. Track the upstream repo by changing to the directory where you;ve cloned the Style Guide file by using the following commands:

    ```bash
    cd docs-style-guide
    git remote add --track master upstream git@github.com:rackerlabs/docs-style-guide.git

    ```
    If you want to make new changes to the Style Guide, start with the
    following steps.

4.  Bring your branch up-to-date with upstream with the following commands all
    entered on one line and separated by semicolons (;):

    ```bash
    git checkout master; git fetch upstream; git merge upstream/master; git push origin master
    ```

5. Create a branch for changes. For details about this part of the workflow, see
   [Understanding the GitHub Flow](https://guides.github.com/introduction/flow/index.html)
   guide.

    ```bash
    git checkout -b <name-of-branch>
    ```

6. In the new branch, make changes to existing files and add new files, as needed.

7. Add all files relevant to the change using the following command:

   ```
   git add .
   ```

8. Commit the changed files:

    ```bash
    git commit -m "The reason for my change"
    ```

9. Push your branch to your fork:

    ```bash
    git push -u origin <name-of-branch>
    ```

10. Create a pull request (PR) to the upstream repo for your branch

    a. Go to https://github.com/rackerlabs/docs-style-guide

    b. Click on the Create pull request button

    c. If this PR is related to an outstanding github
      [GitHub issue](https://github.com/rackerlabs/docs-cloud-files/issues), include a link to that GitHub issue in the comment

11. The Information Development team reviews your pull request.

12. If necessary, incorporate changes from the review, make updates to your PR
    by adding more commits.

    ```bash
    git add .
    git commit -m "The reason for my update"
    git push
    ```
13. Repeat step 12 as needed.

14. Resolve conflicts, if necessary.

    During your review process, someone might have already updated and merged
    a file that you are in the process of changing. . Such a conflict means
    that you can’t merge your PR. To resolve the conflict, perform the
    following steps.

    a. Bring your branch up-to-date with the upstream repo by running the
       following commands from your branch:

       ```
        git fetch upstream
        git rebase upstream/master
       ```

    b. Follow the steps to [resolve a merge conflict from the command line](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/).

15. When content is approved and you have resolved any conflicts, the
    Information Development team merges your pull request.

16. Update your repo:

    ```bash
    git checkout master; git fetch upstream; git merge upstream/master; git push origin master
    ```

## Tip

To see repository status in your prompt and to activate auto-completion,
perform the following steps:

1. Download
[git-prompt.sh](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh)
and save it in your home directory as .git-prompt.sh

1. Download
[git-completion.bash](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash)
and save it in your home directory as .git-completion.bash

1. Add the following to your .bash_profile in your home directory

```bash
GIT_PS1_SHOWDIRTYSTATE=1
GIT_PS1_SHOWUNTRACKEDFILES=1
GIT_PS1_SHOWCOLORHINTS=1
GIT_PS1_SHOWUPSTREAM=1
source ~/.git-prompt.sh
source ~/.git-completion.bash
```

## Help

* [Understanding the GitHub Flow](https://guides.github.com/introduction/flow/index.html)
* [Mastering GitHub Issues](https://guides.github.com/features/issues/)
* [GitHub Help](https://help.github.com/)
