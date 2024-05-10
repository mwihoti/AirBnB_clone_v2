#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents\
 of the web_static
"""
from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """
    function do_pack
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # create folder versions if it doesn’t exist
    local("sudo mkdir -p versions")

    # extract the contents of a tar archive
    result = local("sudo tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        f_path = f"versions/web_static_{now}.tgz"
        f_size = os.path.getsize(f_path)
        print(f"web_static packed: {f_path} -> {f_size} Bytes")

        return result


if __name__ == "__main__":
    do_pack()
