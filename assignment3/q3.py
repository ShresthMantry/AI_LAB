from PIL import Image
import numpy as np
import pandas as pd

img = Image.open('i.png').convert('L')  

img_matrix = np.array(img)

df = pd.DataFrame(img_matrix)
df.to_csv('image_data.csv', index=False, header=False)

df = pd.read_csv('image_data.csv', skipfooter=1, engine='python')
df = df[df.columns[:-1]]

