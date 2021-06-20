# automatefiles.py

import os

from shutil import move

# directory paths

user = os.getenv('USER')

root_dir = r'/home/redwan/Downloads'.format(user)

image_dir = r'/home/redwan/Pictures'.format(user)

documents_dir = r'/home/redwan/Documents/'.format(user)

others_dir = r'/home/redwan/Downloads/others'.format(user)

software_dir = r'/home/redwan/Downloads/Software'.format(user)

# category wise file types

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')

img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')

software_types = ('.exe', '.pkg', '.dmg')

def get_non_hidden_files_except_current_file(root_dir):
  return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]

def move_files(files):
  for file in files:
    # file moved and overwritten if already exists
    if file.endswith(doc_types):
      move(file, '{}/{}'.format(documents_dir, file))
      print('file {} moved to {}'.format(file, documents_dir))
    elif file.endswith(img_types):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(software_types):
      move(file, '{}/{}'.format(software_dir, file))
      print('file {} moved to {}'.format(file, others_dir))
    else:
      move(file, '{}/{}'.format(others_dir, file))
      print('file {} moved to {}'.format(file, others_dir))

if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)


