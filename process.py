import hashlib
import os
import compare2image as compare

MAX = 1000000
folder_path = "E:\\myproject\\Tool Pass CP\\phpsource\\storage\\app\\public\\friends"

def md5(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()

#**
#uid: uid của clone
#name: tên trong list tên cần xác định
#
def get_file_name_by_name(uid, name):
    #mã hóa md5 tên
    name_md5 = md5(name)
    uid_folder_path = folder_path  + '/' + uid

    #danh sách filename
    filenames = os.listdir(uid_folder_path)

    for filename in filenames:
        if name_md5 in filename:
            return filename

#đọc nội dung theo dòng từ đường dẫn
def read_file(path):
    with open(path) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content

# chẻ 1 dòng thành 3 thành phần
# link
# width
# height
# @param : link . ex: https://scontent.xx.fbcdn.net/v/t1.0-9/44332922_1393499684086489_4827443584577830912_n.jpg?_nc_cat=105&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=e498120cec227af29bc40e7805eee18f&oe=5C4E2664|960|720
def convert_a_line_to_array(line):
    return line.split("|")

# tính độ sai khác giữa 2 link ảnh
# nếu ảnh không cùng kích thước trả về false
# nếu ảnh cùng kích thước trả về độ sai khác
def error_square_of_2link(link, link_source):
    return compare.compare_images2(link, link_source)

# tính độ sai khác nhỏ nhất danh sách ảnh của 1 tên với ảnh cần so sánh
def error_square(uid, name, image_link):
    #lấy tên của file backup ảnh
    filename = get_file_name_by_name(uid, name)

    #đường dẫn file
    path = folder_path + "/" + uid + "/" + filename

    #đọc nội dung file
    lines = read_file(path)

    #kết quả
    #ban đầu gán = MAX
    result = MAX

    #lặp từng dòng của của lines
    for line in lines:
        #lấy thông tin ảnh
        info_of_photo = convert_a_line_to_array(line)

        #link ảnh
        link = info_of_photo[0]

        #tính độ sai khác
        try:
            error_square = compare.compare_images2(link, image_link)
            #error_square_of_2link(link, image_link)

            # nếu độ sai khác nhỏ hơn result
            if error_square < result:
                # gán cho resutl
                result = error_square
        finally:
            pass


    return result

# tính độ sai khác của list name
def error_square_of_list_name(uid, list_name, image_link):
    result = MAX
    result_name = ''

    for name in list_name:

        try:
            error_square_tmp = error_square(uid, name, image_link)

            if error_square_tmp < result:
                result = error_square_tmp
                result_name = name
        except Exception as e:
            pass

    return result_name