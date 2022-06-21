## Start Machine Learning Project.

### Software and account Requirement

1. [Githun Account](https://github.com)
2. [Heroku Account](https://dashboard.heruku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)

### Creating Conda Environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add <file_name>
```

OR
```
git add .
```

> Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

To sceck the git status
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

OR
```
git push origin <branch_name>
```