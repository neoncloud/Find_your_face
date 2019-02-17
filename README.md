# Find_your_face
一个 Python 脚本，用于对比 https://thispersondoesnotexist.com/ 中随机生成的脸和你自己的脸，并计算相似度，会自动保存相似度超过设定值的脸。

使用 Face++ 的 API，使用之前请先注册 Face++，并获取自己的 api_key 和 api_secret


```
usage: face.py [-h] -m MY_FACE_FILE -k API_KEY -s API_SECRET [-c CONFIDENCE]
               [-n HOW_MANY]

Find your face from the void.

optional arguments:
  -h, --help            show this help message and exit
  -m MY_FACE_FILE, --my_face_file MY_FACE_FILE
                        Path to your face image file
  -k API_KEY, --api_key API_KEY
                        Your api_key
  -s API_SECRET, --api_secret API_SECRET
                        Your api_secret
  -c CONFIDENCE, --confidence CONFIDENCE
                        Set the similarity of your face and the faces you want
                        to save
  -n HOW_MANY, --how_many HOW_MANY
                        Set the quantity of the faces you want to save
```