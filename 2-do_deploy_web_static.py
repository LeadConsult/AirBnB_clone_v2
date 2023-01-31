#!/usr/bin/python3
"""Distribute an archive to a web server
"""

import os
from fabric.api import env, put, run

env.hosts = ['100.25.223.88', '54.158.178.139']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Deploy an archive to the web server"""

    if not os.path.exists(archive_path):
        return False
    
    # Upload archive
    put(archive_path, "/tmp/")
    
    # Create target directory
    timestamp = archive_path[-18:-4]
    run(f"sudo mkdir -p /data/web_static/releases
            /web_static_{timestamp}/")
    
    # Uncompress archive and delete .tgz
    run(f"sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C 
            /data/web_static/releases/web_static_{timestamp}/")
    run(f"sudo rm /tmp/web_static_{timestamp}.tgz")
    
    # Move contents into host web_static
    run(f"sudo mv /data/web_static/releases/web_static_{timestamp}/web_static/* 
            /data/web_static/releases/web_static_{timestamp}/")
    
    # Remove extraneous web_static directory
    run(f"sudo rm -rf /data/web_static/releases/web_static_{timestamp}/web_static")
    
    # Delete pre-existing symbolic link
    run("sudo rm -rf /data/web_static/current")
    
    # Re-establish symbolic link
    run(f"sudo ln -s /data/web_static/releases/web_static_{timestamp}/ 
            /data/web_static/current")
    
    return True

