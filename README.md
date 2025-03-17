## Pneumonia Detection Using Deep Learning

This project utilizes a Convolutional Neural Network (CNN) trained on chest X-ray images to detect pneumonia. It provides an easy-to-use interface using Gradio for users to upload chest X-ray images and get results on whether the person is affected by pneumonia.

---
### Key Features:

* **Model Type** : A deep learning model based on VGG16 architecture fine-tuned for pneumonia detection.
* **User Interface** : Simple and interactive Gradio web interface to upload images and get real-time predictions.
* **Real-Time Prediction** : Upload a chest X-ray image and the model will predict whether the person has pneumonia or not.

--- 
### Requirements:

To run this project locally or deploy it, you need to install the following dependencies:

* **Python 3.7 or higher**
* **TensorFlow** (for loading the pre-trained model and prediction)
* **NumPy** (for numerical operations)
* **Gradio** (for creating the web interface)
* **Pillow** (for image processing)

You can install the dependencies using `pip`:

```bash
pip install tensorflow numpy gradio pillow
```

---

### Project Setup:

1. **Clone the Repository** :
   First, clone the repository to your local machine.

```bash
git clone https://github.com/Mangaleshwaran2002/Pneumonia-Detection-Using-Deep-Learning.git
cd Pneumonia-Detection-Using-Deep-Learning
```

2. **Place the Model File** :
   Ensure that you have the pre-trained model `PNEUMONIA_Detection_model.h5`.you can downlaod the model from here .Place the model file in the `model` directory in the root of the project.
```bash
├── model
│   └── PNEUMONIA_Detection_model.h5
├── app.py
├── requirements.txt
└── README.md
```
3. **Run the Application**: Run the Python script to launch the Gradio interface. The following command will start the web interface.
```bash
python app.py
``` 
Once the app starts, a URL will be displayed in the terminal (typically http://localhost:7860), where you can access the web interface.

4. **Using the Web Interface**:
Upload a chest X-ray image in .jpg, .jpeg, or .png format.The model will process the image and display whether the person is affected by pneumonia or not.

---

### Screenshot:
![Screenshot 1](https://raw.githubusercontent.com/Mangaleshwaran2002/Pneumonia-Detection-Using-Deep-Learning/refs/heads/master/screenshot/Screenshot%201.png)
![Screenshot 2](https://raw.githubusercontent.com/Mangaleshwaran2002/Pneumonia-Detection-Using-Deep-Learning/refs/heads/master/screenshot/Screenshot%202.png)

---
## Author
Created by K.Mangaleshwaran on **March 17, 2025**.
