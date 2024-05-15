import shutil

folder_to_zip = r"C:\Users\HP\Downloads\sample-zip"
print(shutil.make_archive(r"C:\Users\HP\Downloads\zipped", "zip", folder_to_zip))

shutil.make_archive(r"C:\Users\HP\Downloads\zipped.zip", "unzipped", "zip")

# ----- @TODO Console Output -----

# C:\Users\HP\Downloads\zipped.zip
