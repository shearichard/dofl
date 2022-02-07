# DOFL
A simple [Flask](https://palletsprojects.com/p/flask/) app to be put into a [Docker](https://www.docker.com/) container for use as a testbed while doing some [Kubernetes](https://kubernetes.io/) work.  

## Dockerfile
The initial version of the Docker file is based on [this blog post](https://hasura.io/blog/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d/). 

## Development Virtenv
The name of the development vm is dofl37.

Activate like this ...

```
. ./dofl37/bin/activate
```

Using the [virtualenv.pyz](https://virtualenv.pypa.io/en/stable/installation.html#via-zipapp) instead of installing virtualenv properly due to weirdness arising from the way I have 3.7 installed on the development vm. 

The target python is 3.7 which is installed at /usr/local/bin/python3.7 on the development vm.


## Docker Cheat Sheet

```
$ docker build -t dkr-flsk .;docker image ls;
...
$ docker container ls --all
...
$ docker rm abdd314c875c
...
$ docker container ls --all
...
$ docker run -p 8080:8080 -d dkr-flsk
...
$ docker container ls --all
```


## Docker perms
When working on a new development machine for the first time remember to [add the current user to the 'docker' group](https://techoverflow.net/2017/03/01/solving-docker-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket/).

```
sudo usermod -a -G docker $USER
```

And exit your ssh session and reconnect before attempting a `docker build`.

