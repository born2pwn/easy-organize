file_types = {
  'images' : ['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'],
  'documents': ['.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wks','.wps','.wpd', '.ods','.xlr','.xls','.xlsx', '.djvu', '.epub'],
  'vidoes' : ['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'],
  'audios': ['.aif','.cda','.mid','.mp3','.mpa','.ogg','.wav','.wma','.wpl'],
  'archives' : ['.7z','.arj','.deb','.pkg','.rar','.rpm', '.gz', '.xz', '.z','.zip'],
  'disks' : ['.bin','.dmg' ,'.iso','.toast','.vcd'],
  'datas': ['.csv','.dat','.db','.log','.mdb','.sav','.sql','.tar','.xml','.dbf'],
  'articles' : ['.mhtml'],
  'torrents': ['.torrent'],
  'androids': ['.apk'],
  'shells': ['.batch', '.sh', '.bat', '.ps'],
  'windows': ['.exe', '.msi', '.cab'],
}

def get_folder_by_ext(ext):
  for folder, exts in file_types.items():
    if ext in exts:
      return folder
