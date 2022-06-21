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

To setup CI/CD pipeline in heroku we need 3 information



BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be in lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 6369ce28b197 (<IMAGE ID>)
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```
