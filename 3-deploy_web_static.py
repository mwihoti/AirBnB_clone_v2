#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers, using\
the function do_deploy
"""
from fabric.api import put, run, env
import os.path
from datetime import datetime
env.hosts = ['52.3.254.102', '100.26.247.157']
env.user = "ubuntu"

def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        print("Failed to create archive from web_static")
        return False


    return do_deploy(archive_path) archive_path = do_pack()
    if archive_path is None:
        print("Failed to create archive from web_static")
        return False

    # Call do_deploy function, using the new path of the new archive and
    # return the return value of do_deploy
    return do_deploy(archive_path)

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        # extract the contents of a tar archive
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output

def do_deploy(archive_path):
    """
    function that distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
    return False
    # Uncompress the archive to the folder,
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create new directory for release
        run("mkdir -p {}".format(folder_path))

        # Untar archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))

        # Move extraction to proper directory
        run("mv {}web_static/* {}".format(folder_path, folder_path))

        # Delete first copy of extraction after move
        run("rm -rf {}web_static".format(folder_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        success = True

    except Exception:
        success = False
        print("Could not deploy")
    return success
