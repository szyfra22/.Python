# #Ilość plików
#
# # import OS module
# import os
# # lokalizacja folderu w projekcie
# FOLDER = "D://pythonProject//Praca_z_plikami//dev"
#
# totalFiles = 0
# totalDir = 0
#
# for base, dirs, files in os.walk(FOLDER):
#     for directories in dirs:
#         totalDir += 1
#     for Files in files:
#         totalFiles += 1
#
#
# print('Total number of files',totalFiles)
# print('Total:',(totalDir + totalFiles))

#Struktura katalogu
#Tree

# import os
#
#
# def list_files(spath):
#     for root, directories, files in os.walk(spath):
#         level = root.replace(spath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))
#
#
# print(list_files("D://pythonProject//Praca_z_plikami"))

# import os
#
# for dirpath, dirnames, filenames in os.walk(r"D:\pythonProject\Praca_z_plikami"):
#     print(
#         f"Root: {dirpath} \n"
#         f"Sub-directories: {dirnames} \n"
#         f"Files: {filenames} \n\n"
#     )

#Konwersja rozszerzenia
# from PIL import Image
#
# image = Image.open("1.jpg")
# image.save("output.png")


