import numpy as np
from keras.preprocessing import image
from keras.applications import resnet50
from pathlib import Path

# Load the pre-trained ResNet50 model
model = resnet50.ResNet50(weights='imagenet')

# Load and preprocess the image
img_path = Path('/home/zxpatric/tmp/GDiUqhaXEAA6QK5.jpeg')
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = resnet50.preprocess_input(x)

# Make predictions
predictions = model.predict(x)
decoded_predictions = resnet50.decode_predictions(predictions, top=3)[0]

# Print the top 3 predictions
for _, label, confidence in decoded_predictions:
    print(f"{label}: {confidence * 100}%")
