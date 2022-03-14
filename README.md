# Storj-Decentralized-Data-Backup-for-Linux
A python scripts that scans a folder, archives/compress the contents into a single file and uploads that file to Storj DCS (Decentralized Cloud Storage).


## Requirements:
* Linux (Ubuntu). This script was tested in Windows using WSL (Windows subsystem for Linux under the Ubuntu Distribution).
* Storage DCS account with Storj with uplink installed for ARM.

## Usage:
1. In a directory of your choosing, place this script inside and create a folder named 'tobackup'.
2. Place any files to be backed up into the 'tobackup' folder.
3. To Back Up: `python3 storj_backup.py backup` 
4. To Restore: `python3 storj_backup.py restore`
5. Show Storj Usage: `python3 storj_backup.py usage`

Note: If the script is called without an argument, it defeault to backing up the contents in the folder.

