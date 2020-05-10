import os
import hashlib
from collections import defaultdict
import sys
# The CMD argument  
source_directory = sys.argv[1]

# This function returns a hash value for the given file 
def create_hash(file_path, block_size):
    hash = hashlib.md5()

    with open(file_path, "rb") as f:
        # Read the 1st block of the file
        chunk = f.read(block_size)
        # Keep reading the file until the end and update hash 
        while chunk:
            hash.update(chunk)
            chunk = f.read(block_size)

    # Return the hex checksum
    return hash.hexdigest()

# The dict will have a list as values
files_dict = defaultdict(list)

for file_name in os.listdir(source_directory):
    file_path = source_directory+'/'+file_name
    # If there are more files with same checksum append to list
    files_dict[create_hash(file_path, 1024)].append(file_name)

for key,val in files_dict.items():
    if len(val) > 1:
        print(val)
