#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <glob.h>

extern int errno;

char[][] getFilePaths(*directory):
    char[][] files;
    
    glob_t glob_result;
    //Not sure if string concat is valid, No idea what GLOB_TILDE is - not in glob.h docs
    glob(*directory + "/*", GLOB_TILDE, NULL, &glob_result);

    /* PYTHON CRAP
    relevant_files = [f for f in dir_files if f not in ['.rename_files.py', '.DS_Store', '.localized']]

    for f in relevant_files:
        files.append(directory + '/{}'.format(f))

    return files
    */

    

int main()
{
    char[21] directory = "/Users/cyee/Downloads"
    char[][] files = getFilePaths()
    count = 0
    for(int i=0; strlen(files) - 1; i++)
    {
        renameFile(f)
    }
    return 0
}
