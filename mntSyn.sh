#!/bin/bash
mount -t cifs //192.168.1.115/home /home/jim/SynologyDrive -o credentials=/home/jim/.credentials,uid=1000,gid=1000,vers=2.1
