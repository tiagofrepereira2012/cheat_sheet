# Delete large files from git history

`git filter-branch --tree-filter 'rm -f $FILE_NAME' HEAD`

# Set git name and email according to project

https://github.com/DrVanScott/git-clone-init

# Git always asking for password even if you have ssh keys well set

ssh-add ~/.ssh/id_rsa 

If there is an issue wth ssh-agent, do:

ssh-agent bash

