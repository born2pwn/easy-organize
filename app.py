#!/usr/bin/python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import mimetypes
import os
import pathlib
import json
import sys
import shutil
import time

from file_types import get_folder_by_ext

class MyHandler(FileSystemEventHandler):
  i = 1

  def on_modified(self, event):
    for filename in pathlib.Path(folder_to_track).iterdir():
      if filename.is_file(): # only work with files for now
        f_ext = filename.suffix # file extension
        f_type = get_folder_by_ext(f_ext)

        if f_type:
          path = os.path.join(folder_to_track, f_type)

          if os.path.exists(path) and os.path.isdir(path):
            if os.path.exists(os.path.join(path, filename.name)):
              orig_filename = filename.name.split('.')[0]
              path = '%s.2%s' %(orig_filename, f_ext)

          else:
            os.makedirs(path)

          shutil.move(str(filename), path)

folder_to_track = '/home/born2pwn/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(3)
except KeyboardInterrupt:
  observer.stop()

observer.join()
