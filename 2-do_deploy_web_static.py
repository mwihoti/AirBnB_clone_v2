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
    if not exists(archive_path):
        print("Archive '{}' does not exist.".format(archive_path))
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        no_ext = archive_file.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the /tmp directory on the server
        put(archive_path, '/tmp/')

        # Create necessary directory structure and deploy
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_file, path, no_ext))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        print("Deployment successful.")
        return True

    except Exception as e:
        print("An error occurred during deployment:", e)
        return False
