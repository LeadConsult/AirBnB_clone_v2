#!/usr/bin/python3
import os
import datetime
from fabric.api import local

def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """

    # Get the current date and time
    now = datetime.datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
            now.month, now.day, now.hour, now.minute, now.second)
    archive_path = "versions/{}".format(archive_name)

    # Check if the versions folder exists, if not create it
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the tar archive
    local("tar -czvf {} web_static/".format(archive_path))

    # Return the archive path
    return archive_path

