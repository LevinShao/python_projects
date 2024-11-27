from io import BytesIO
from tkinter import Image
import requests

response = requests.get('https://zenquotes.io/api/image')

if requests.status_codes == 200:
    image_data = BytesIO(response.context)
    image = Image.open(image_data)
    image.show()
else:
    print('failed')