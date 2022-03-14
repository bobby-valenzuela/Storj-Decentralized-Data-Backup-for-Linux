#!/usr/bin/python3

import os
import sys

args = sys.argv
pwd = os.path.dirname(os.path.abspath(__file__))
action = 'noarg' if len(args) < 2 else args[1]
debug = '> /dev/null 2>&1' if 'debug' not in args else ''

# Make Bucket
os.system(f'cd {pwd}; uplink mb sj://mybackup {debug}')

# Main

if(action == 'backup' or action == 'noarg'):

    src_folder_exists = os.path.exists(f'tobackup/')

    if(src_folder_exists == False):
        os.system(f'mkdir tobackup {debug}')

        print('Directory \'tobackup\' is empty. Nothing to backup.')
        
    elif not os.listdir(f'{pwd}/tobackup'):
        
        print('Directory \'tobackup\' is empty. Nothing to backup.2')
    
    else:    

        # Archive and Compress
        os.system(f'tar -cvz tobackup/ -f tobackup.tar.gz {debug}')

        # Upload to Storj
        os.system(f'uplink cp tobackup.tar.gz sj://mybackup ')
        
        os.system(f'rm -r tobackup.tar.gz {debug}')

        # Show Data backed up
        os.system('uplink ls sj://mybackup')
        
        # print_usage()

        print("""
         _   _       _                 _          _ _
        | | | |_ __ | | ___   __ _  __| | ___  __| | |
        | | | | '_ \| |/ _ \ / _` |/ _` |/ _ \/ _` | |
        | |_| | |_) | | (_) | (_| | (_| |  __/ (_| |_|
         \___/| .__/|_|\___/ \__,_|\__,_|\___|\__,_(_)
              |_|
            """)

elif (action == 'recover'):
    
    # Check if we are bypassing confirmation prompt
    force_recover = 'force' if '-f' in args and args[1] == 'recover' else ''

    if (force_recover != 'force'):
        response = input("Recovering will replace the contents of 'recovered_files'. Do you wish to proceed? (y/n): ")
    else:
        response = ''

    # Action the recovery process
    if(response == 'y' or response == 'yes' or force_recover == 'force'):
    
        # Prepare destination folder
        destination_folder_exists = os.path.exists(f'recovered_files/')

        if (destination_folder_exists == True):
            os.system(f'rm -r recovered_files {debug}')
        
        os.system(f'mkdir recovered_files {debug}')

        # Download from Storj
        os.system(f'uplink cp sj://mybackup/tobackup.tar.gz tobackup.tar.gz ')

        # Extract and decompress
        os.system(f'tar -xzf tobackup.tar.gz -C recovered_files {debug}')

        os.system(f'rm -r tobackup.tar.gz {debug}')

        print("Recovery Complete!")
    else:
        print("Recovery Aborted")

elif (action == 'usage'):
    
    os.system('uplink ls sj://mybackup')

