# coding=utf-8

import hashlib
import process

folder_path = "E:\\myproject\\Tool Pass CP\\phpsource\\storage\\app\\public\\friends"


#print(hashlib.md5("Thắng Vũ".encode("utf-8")).hexdigest())


#94eb99514a3af4b36d58ae624e7bb00d
#94eb99514a3af4b36d58ae624e7bb00d

uid = '100028987356675'
name = 'Kiên T Đinh'
image_link = "https://scontent.fhan3-1.fna.fbcdn.net/v/t1.0-9/44444435_2059173830772568_7899369465018580992_n.jpg?_nc_cat=110&_nc_ht=scontent.fhan3-1.fna&oh=df1f789f017a8ed13333214d50934fa6&oe=5C429149"
filename = process.get_file_name_by_name(uid, name)
#print(filename)

filepath = folder_path + "/" + uid + "/" + filename
lines = process.read_file(filepath)
#print(lines)

error = process.error_square(uid, name, image_link)
print(error)