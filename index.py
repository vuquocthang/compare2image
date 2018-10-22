from flask import Flask, request, jsonify
app = Flask(__name__)
import json
import requests
import compare2image
import process

@app.route('/')
def index():
    return 'Hmm , Hello '

@app.route('/process', methods = ['POST'])
def params():
    if request.method == 'POST':
        data = json.loads(request.form["data"])
        image_link = request.form["image_link"]

        print(image_link)
        print(data[0])

        #so sánh 2 bức ảnh từ 2 url
        name_result = ""
        square_error = -1

        for item in data:
            for photo in item['photos']:
                try:
                    print("===========================================================")

                    #kiểm tra
                    check = compare2image.compare_images2(image_link, photo['link'])

                    #nếu ảnh không cùng kích thước nghĩa là check is False
                    if check is False:
                        pass
                    #nếu ảnh cùng kích thước
                    else:
                        #nếu square_error đang là khởi tạo
                        if square_error == -1:
                            name_result = item['name']
                            square_error = check
                        else:
                            #nếu check < square_error thì gán tên và square_error mới
                            if check < square_error:
                                name_result = item['name']
                                square_error = check
                    print("name : {}".format(name_result) )
                    print("square error : {}".format(square_error))
                except Exception as e:
                    print(e)
        return name_result
    return 'Done'

@app.route('/process2', methods = ['POST'])
def process2():
    if request.method == 'POST':
        list_name = json.loads(request.form["listName"])
        uid = request.form["uid"]
        image_link = request.form["imageLink"]

        result = process.error_square_of_list_name(uid, list_name, image_link)

        return result

if __name__ == '__main__':
   app.run(host='0.0.0.0')