# Delete large files from git history

`git filter-branch --tree-filter 'rm -f $FILE_NAME' HEAD`

or

`git filter-branch --force --index-filter "git rm --cached --ignore-unmatch -r research/data/" --prune-empty --tag-name-filter cat -- --all`

`git push origin --force --all`

`git push origin --force --tags`

# Set git name and email according to project

https://github.com/DrVanScott/git-clone-init

# Git always asking for password even if you have ssh keys well set

ssh-add ~/.ssh/id_rsa 

If there is an issue wth ssh-agent, do:

ssh-agent bash

