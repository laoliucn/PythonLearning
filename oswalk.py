import os

print(os.getcwd())

for folderName, subfolders, filenames in os.walk('/Users/travisliu/Documents'):
    print('The current folder is: ', folderName)

    for subfolder in subfolders:
        print('Subfolder of ', folderName, ': ', subfolder)
    for filename in filenames:
        print('File inside ', folderName, ': ', filename)
    print()
