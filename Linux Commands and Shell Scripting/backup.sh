#!/bin/bash

# This checks if the number of arguments is correct
# If the number of arguments is incorrect ( $# != 2) print error message and exit
if [[ $# != 2 ]]
then
  echo "backup.sh target_directory_name destination_directory_name"
  exit
fi

# This checks if argument 1 and argument 2 are valid directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Invalid directory path provided"
  exit
fi

# [TASK 1] Store the command-line arguments
targetDirectory=$1
destinationDirectory=$2

# [TASK 2] Print the target and destination directories
echo "Target directory is $targetDirectory"
echo "Destination directory is $destinationDirectory"

# [TASK 3] Get the current timestamp in YYYYMMDDHHMMSS format
currentTS=$(date +%Y%m%d%H%M%S)

# [TASK 4] Create a unique backup filename with the timestamp
backupFileName="backup-$currentTS.tar.gz"

# [TASK 5] Get the absolute path of the target directory
origAbsPath=$(cd "$targetDirectory" && pwd)

# [TASK 6] Temporarily change to the destination directory and store its absolute path
cd "$destinationDirectory"
destDirAbsPath=$(pwd)

# [TASK 7] Return to the original (target) directory
cd "$origAbsPath"

# [TASK 8] Get the timestamp of yesterday
yesterdayTS=$(date -d "yesterday" +%Y%m%d%H%M%S)

# Create an array to store files for backup
declare -a toBackup

# [TASK 9] Find all regular files in the target directory (and subdirectories)
for file in $(find . -type f)
do
  # [TASK 10] Check if the file was modified after yesterday
  if [[ $(date -r "$file" +%Y%m%d%H%M%S) -gt $yesterdayTS ]]
  then
    # [TASK 11] If modified recently, add the file to the backup array
    toBackup+=("$file")
  fi
done

# [TASK 12] Create a tar.gz archive of the files to be backed up
tar -czf "$backupFileName" "${toBackup[@]}"

# [TASK 13] Move the created backup file to the destination directory
mv "$backupFileName" "$destDirAbsPath"