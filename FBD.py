# This is a program to find big data structures.

import os

file_name = "/Users/pankaj/abcdef.txt"

file_stats = os.stat('‪C:\\Windows\\RtlExUpd.dl')

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
