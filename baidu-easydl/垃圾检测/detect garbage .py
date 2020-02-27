import requests
import base64
import json
import cv2 as cv

def get_access_token(ak, sk):
    '''
        获得访问口令
    '''
    url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=\
    client_credentials&client_id={ak}&client_secret={sk}'
    res = requests.get(url.replace(" ", ""))
    if res:
        return res.json().get('access_token')
    else:
        print('暂无法获得访问口令')
    
def get_image_result(ak, sk, img):
    '''
        获得图片识别的结果
    '''
    at = get_access_token(ak, sk)
    if at:
        url =  f'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/\
        garbage-detection?access_token={at}'
        with open(img, 'rb') as f:
            image = f.read()
            img_data = str(base64.b64encode(image), encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        params = {
        "image": img_data
        }
        res = requests.post(url=url.replace(" ", ""), headers=headers, data=json.dumps(params))
        if res:
            return res.json().get('results')
        else:
            print(f"错误码:{res.json().get('error_code')}, 错误提示:{res.json().get('error_msg')}")
           
def show_image_result(ak, sk, img):
    '''
        结果显示
    '''
    img_res = get_image_result(ak, sk, img)
    img_array = cv.imread(img)
    color = {
            "Hazardous": (255, 0, 0),
            "Residual": (0, 255, 0),
            "Recyclable": (0, 255, 0),
            "Household": (255,255,0)
            }
    if img_res:
        for i in range(len(img_res)):
            top = img_res[i].get("location").get("top")
            left = img_res[i].get("location").get("left")
            height = img_res[i].get("location").get("height")
            width = img_res[i].get("location").get("width")
            name = img_res[i].get("name")
            score = round(img_res[i].get('score'), 2)
            cv.rectangle(img_array, (left, top), (left+width,top+height), color.get(name), 2)
            cv.putText(img_array, f"{name},score:{score}", (left, top-10), cv.FONT_HERSHEY_COMPLEX, 0.5, color.get(name), 1)
        cv.imshow('image result', img_array)
        cv.waitKey()
        
if __name__ == "__main__":
    ak = 'xxxxxxxxxxxxxxxxxxxxxxx' 
    sk = 'xxxxxxxxxxxxxxxxxxxxxxx'
    image_path = "./new_data/00043.jpg"
    show_image_result(ak, sk, image_path)