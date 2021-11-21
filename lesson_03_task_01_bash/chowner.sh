#!/bin/bash

### SoftServe DevOps Autumn School ###
# Lesson 3 Home Task
# Title: Create scenario to change the owner of files and folders
# Parameters: 
# $1 <username>
# $2 <directory>

# Requirements:
# $1 - should be existing user in your OS (in your script the checking block should be present)
# $2 - should be only the directory (also need to be checked in your script)


user=$1
folder=$2

print_usage() {
    echo "# USAGE:"
    echo "sudo ./chowner.sh username folder"
    echo "where:"
    echo "     username - a user that should exist in the system"
    echo "     folder - a folder that should be a folder (have the 'd' attribute)"
    echo "Note: the script requires root privileges to be executed!\n"
}

# Check is the script started as root
if [ $EUID -ne 0 ]; then
    echo "ERROR: please run the script as root!"
    print_usage
    exit 1
fi

# Check if the user exists in the system
if ! id -u "$user" &> /dev/null; then
    echo "ERROR: the indicated user $user doesn't exist!"
    print_usage
    exit 1
fi

# Check if the second parameter is a folder
if [ ! -d "$folder" ]; then
    echo "ERROR: the indicated $folder path - is not a folder (or does not exist/accessible)!"
    print_usage
    exit 1
fi

# Now run the recursive chown
sudo chown -R $user:$user $folder &>/dev/null
echo "User $user now owns the $folder folder, including subfolder/files!"