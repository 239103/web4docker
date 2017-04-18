from flask import render_template, request
from . import main
import docker

client = docker.from_env()

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/api/1.0/container>', methods=['GET'])
@main.route('/api/1.0/container/<name>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def container(name=None):
    if request.method == "GET":
        if name==None:
            for container in client.containers.list():
                print container.id

        if name:
            pass

    if request.method == "PUT":
        pass

    if request.method == "POST":
        pass

    if request.method == "DELETE":
        pass
