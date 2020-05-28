# DOFL
A simple [Flask](https://palletsprojects.com/p/flask/) app to be put into a [Docker](https://www.docker.com/) container for use as a testbed while doing some [Kubernetes](https://kubernetes.io/) work.  

## Dockerfile
The initial version of the Docker file is based on [this blog post](https://hasura.io/blog/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d/). 

## Development Virtenv
The name of the development vm is dofl37.

Using the [virtualenv.pyz](https://virtualenv.pypa.io/en/stable/installation.html#via-zipapp) instead of installing virtualenv properly due to weirdness arising from the way I have 3.7 installed on the development vm. 

The target python is 3.7 which is installed at /usr/local/bin/python3.7 on the development vm.


