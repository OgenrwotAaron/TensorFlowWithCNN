import numpy as np
from keras_preprocessing import image
import tensorflow as tf

img = image.load_img('test_image.jpg', target_size=(150,150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

model = tf.keras.models.load_model('rps.h5')

classes = model.predict(x, batch_size=10)

print(classes[0])
