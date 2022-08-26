import base64
import cv2
from flask import Flask,render_template,request,json
import detect2
import numpy as np
app = Flask(__name__)

defaultencoding = 'utf-8'

@app.route("/testimage",methods=['GET','POST'])
def testimage():
    img =base64.b64decode(request.form.get("image"))     #队base64进行解码还原。
    with open("static/recognition.jpg","wb") as f:   #存入图片，存入地址为服务器中的项目地址。
        f.write(img)
    res = ''
    res = detect2.main()
    #img = cv2.imread("static/recognition.jpg")

    #cv2.imshow('show',img)
    #print(img)
    #cv2.waitKey(0)
    #print("返回结果为"+res)
    return json.dumps(res)

@app.route("/",methods=['GET','POST'])
def hello():
    print('yes')
    return "返回成功"

# @app.route("/YOLOv5",methods=['GET','POST'])
# def YOLOv5():


if __name__ == "__main__":
    app.run()
