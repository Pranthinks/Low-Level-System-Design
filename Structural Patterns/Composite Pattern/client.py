from Folder import Big_Folder
from file_leaf import File

file1 = File('Saahos File')
file2 = File('Billas File')

sub_folder = Big_Folder('Action Movies')
sub_folder.add(file2)

main_folder = Big_Folder('Hero')
main_folder.add(file1)
main_folder.add(sub_folder)

main_folder.Show_details()
