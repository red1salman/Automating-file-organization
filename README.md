# Automating-file-organization

First I worked on automizing the image types files, automatically transferring them from the default Downloads folder to the Pictures folder in my C drive. 

I wrote the python script in the Downloads folder. Imported two modules, os and shutil. 

os module is used to provide us with functions to interact with the operating system. The script used it to get the current user and their folder directories. 

shutil is used for copying, moving and removal of files and directories, essentially cutting files into a different directory. From shutil we import move function.

A tuple is created for image types like .jpg, .png, .gif etc

The method get_non_hidden_files_except_current_file() to get all the non-hidden files except for the python script. 
shutil.move() method is then used to move all those files to their respective folders.

In shutil.move() method I add three arguments(src, dst, copy_function = copy2)
It recurisively moves a file or directory(src) to another location(dst) and returns the destination. 

In the end the move_files() is called. When the images in the Downloads folder moved successfully, categories for document, software and other files were created.


To automate the script I used crontab to execute the program every 2 minutes. Any files moved is recorded in the log.txt inside the Log folder in Downloads. The command lines edited in the crontab file is: 

*/2 * * * * cd ~/Downloads/ && python3 automation.py >>~/Downloads/Log/log.txt
