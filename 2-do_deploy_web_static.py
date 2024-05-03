#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers, using\
the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.3.254.102', '100.26.247.157']


def do_deploy(archive_path):
    """
    function that distributes an archive to your web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_input = archive_path.split("/")[-1]
        no_ext = file_input.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_input, path, no_ext))
        run('rm /tmp/{}'.format(file_input))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

