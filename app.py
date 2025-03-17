import os
import numpy as np
import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Set up model path and load the model
model_path = os.path.join(os.getcwd(),'model')
os.makedirs(model_path, exist_ok=True)
model_name = 'PNEUMONIA_Detection_model.h5'
model = load_model(os.path.join(model_path, model_name))

# Define a function to make predictions
def predict_pneumonia(img):
    # Load and preprocess the image
    img = img.resize((224, 224))  # Resize the image to the target size
    x = image.img_to_array(img)    # Convert the image to an array
    x = np.expand_dims(x, axis=0)   # Expand dimensions to match model input
    img_data = preprocess_input(x)  # Preprocess the image

    # Make prediction
    classes = model.predict(img_data)
    result = int(classes[0][0])

    # Return the result
    if result == 0:
        return 'Person is Affected with PNEUMONIA'
    else:
        return 'Person is not Affected with PNEUMONIA'

# Create a Gradio interface
iface = gr.Interface(fn=predict_pneumonia, 
                     inputs=gr.Image(type="pil"), 
                     outputs="text",
                     title="Pneumonia Detection",
                     description="Upload a chest X-ray image to check if the person is affected by pneumonia.")

# Launch the interface
iface.launch()