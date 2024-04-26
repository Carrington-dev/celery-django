## Running Celery On Windows With Django

Usually this is harder than described as most information outthere is not relevant to everyone's reasoning.  This provides the simplest way to run celery on windows but running on docker containers

## Items Needed
Inorder to successfully launch a celery email you need to go through these steps

1. __Redis__
There are two ways to run Redis
* Running Redis on docker
```bash
docker run -d -p 6379:6379 --name django-redis -d redis
```
* Using apt-get package on ubuntu/debian
```
sudo apt-get update
sudo apt install redis
sudo systemctl status redis

```
* If you are on windows

```
It's compilcated but very easy
use docker if you have space or this method

Install Redis on Windows
Use Redis on Windows for development

Redis is not officially supported on Windows. However, you can install Redis on Windows for development by following the instructions below.

To install Redis on Windows, you'll first need to enable WSL2 (Windows Subsystem for Linux). WSL2 lets you run Linux binaries natively on Windows. For this method to work, you'll need to be running Windows 10 version 2004 and higher or Windows 11.

Install or enable WSL2
Microsoft provides detailed instructions for installing WSL. Follow these instructions, and take note of the default Linux distribution it installs. This guide assumes Ubuntu.
```

2. __Celery installed__
```
pip install Redis
pip install celery
```
3. __Celery started__
```
celery -A proj worker -l INFO
```
4. __Redis settings__
5. __Celery files settings__
6. __Celery tasks files__