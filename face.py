import requests
import os
import sys
import argparse
import json
import time

#constants
face_url = 'https://thispersondoesnotexist.com/image'
counter = 0
best_so_far = 0
headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
#arguments
parser = argparse.ArgumentParser(description="Find your face from the void.",epilog="You should apply for the api access from Face++, see more help in README.")
parser.add_argument("-m","--my_face_file", required = True, help = "Path to your face image file")
parser.add_argument("-k","--api_key", required = True, help = "Your api_key")
parser.add_argument("-s","--api_secret", required = True, help = "Your api_secret")
parser.add_argument("-c","--confidence", type = float, default = 80, help = "Set the similarity of your face and the faces you want to save")
parser.add_argument("-n","--how_many", type = int, default = 10, help = "Set the quantity of the faces you want to save")

args = parser.parse_args()
my_face_file = args.my_face_file
api_key = args.api_key
api_secret = args.api_secret
custom_confidence = args.confidence
how_many = args.how_many

my_face_image_file = {'image_file':('face',open(my_face_file,'rb'))}
my_face_post = {'api_key':api_key, 
                'api_secret':api_secret
                }
my_face_data = requests.post('https://api-cn.faceplusplus.com/facepp/v3/detect', data = my_face_post, files = my_face_image_file)
my_face_dict = json.loads(my_face_data.content)

#create a face set (by offical api document) to store the token id, or the token id would be deleted after 72 hours
face_set_post = {'api_key':api_key, 
                'api_secret':api_secret,
                'face_tokens':my_face_dict['faces'][0]['face_token']
                }
requests.post('https://api-cn.faceplusplus.com/facepp/v3/faceset/create', data = face_set_post)
print(my_face_dict['faces'][0]['face_token'])
while 1:
    face_image = requests.get(self.face_url,headers= self.headers)
    face_image_file = {'image_file2':('face',face_image.content)}   #post img file
    post_data = {'api_key':api_key, 
                'api_secret':api_secret,
                'face_token1':my_face_dict['faces'][0]['face_token'],
                }

    requests_data = requests.post('https://api-cn.faceplusplus.com/facepp/v3/compare', data = post_data, files = face_image_file)
    requests_dict = json.loads(requests_data.content)   #convert request data to dict
    
    if requests_dict['confidence'] > best_so_far :
        best_so_far = requests_dict['confidence']
    print(requests_dict['confidence'],"best:",best_so_far)

    if requests_dict['confidence'] > custom_confidence :
        with open(str(time.time())+'.jpeg','wb') as f:
            f.write(face_image.content)
            f.close()
        counter += 1

    if counter > how_many :
        break

