# The intent for this program is to rename files to a similar naming
# scheme and add an incremental number to the end of the names

# ##IMPORTANT## #
# This program will modify any file/folder in the files_to_rename folder.
# It will not work on sub-folders/sub-directories

import os
import time

# Only modify this upper area for file renaming
# Declare the folder directory with a "/" at the end to enable the program to search for the files
folder_directory = "files_to_rename/"
starting_file_number = 1
file_name_format = "PictureName #"


START_TIME = time.time()


def main():
    new_time = 0
    for count, filename in enumerate(os.listdir(folder_directory)):

        # Calculate and print the elapsed time to help identify if the script crashed
        current_time = int(time.time())
        elapsed = int(current_time - START_TIME)
        if elapsed == new_time:
            print("Total Time (seconds): " + str(new_time))
            new_time += 1
        else:
            pass

        # Adds the current loop number (count) to the starting file number
        file_number_temp = count + starting_file_number
        file_number_new = str(file_number_temp)

        # Obtains the files extension for the current loop (filename is an array where
        # the extension is the on the second declaration in the array)
        file_extension = os.path.splitext(filename)[1]

        # Formatting of a few fields prior to putting them together
        source = folder_directory + filename

        if starting_file_number + count < 10:
            destination = file_name_format + "000000" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count < 100:
            destination = file_name_format + "00000" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count < 1000:
            destination = file_name_format + "0000" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count < 10000:
            destination = file_name_format + "000" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count < 100000:
            destination = file_name_format + "00" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count < 1000000:
            destination = file_name_format + "0" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        elif starting_file_number + count >= 1000000:
            destination = file_name_format + "" + file_number_new + str(file_extension)
            file_name = folder_directory + destination
            os.rename(source, file_name)
        else:
            print("This program has reached an unfortunate error of some sort and we do not know why that occurred")
            exit()



if __name__ == '__main__':
    print("This program may take a while, but as long as no error is seen it is still running. Be Patient!")
    main()
