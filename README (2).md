
# 🐱🐶 Cat vs Dog Classifier


This project utilizes deep learning techniques to classify images as either cats or dogs. Leveraging Convolutional Neural Networks (CNNs), the model achieves high accuracy in distinguishing between the two categories

## 🔗 Live Demo
Check out the live demo here:

👉 https://catvsdogclassifier-4levsrjudzkxpgjfgbgvvw.streamlit.app/

```Try uploading an image to see the classifier in action!```


## 📝 Overview
The Cat vs Dog Classifier is a deep learning model built to identify whether an input image contains a cat or a dog. It's trained on a labeled dataset of cat and dog images and can be used for various applications, including pet identification systems and educational purposes.
## ✨ Features


- Binary image classification: Cat or Dog​
- Utilizes Convolutional Neural Networks (CNNs) for feature extraction​
- Trained on a substantial dataset for high accuracy​
- Includes a pre-trained model (cat_vs_dog_model.h5) for immediate use​
- Simple and intuitive interface for predictions​





## ⚙️ Installation
1. Clone the repository:

```bash
  git clone https://github.com/bhardwaj2-6/cat_vs_dog_classifier.git
  cd cat_vs_dog_classifier

```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1. Ensure the pre-trained model file cat_vs_dog_model.h5 is in the project directory.

2. Run the application:


```bash
python app.py
```
3. Follow the on-screen prompts to input the path of the image you wish to classify.



## 🧠 Model Architecture
The model is built using a Convolutional Neural Network (CNN) architecture, which includes:​

- Multiple convolutional layers for feature extraction​
- Pooling layers to reduce spatial dimensions​

- Fully connected layers for classification​

- Dropout layers to prevent overfitting​

The final layer uses a sigmoid activation function to output probabilities for binary classification.​



## 📂 Dataset

The model is trained on a dataset comprising thousands of labeled images of cats and dogs. The dataset is preprocessed to standardize image sizes and normalize pixel values.​


## 📊 Results
The trained model achieves high accuracy on both training and validation datasets, demonstrating its effectiveness in distinguishing between cat and dog images. For detailed performance metrics and training logs, refer to the training notebook (if available).​


## 🤝 Contributing


Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.​

- Fork the repository​

- Create a new branch (git checkout -b feature/YourFeature)​

- Commit your changes (git commit -m 'Add your feature')​

- Push to the branch (git push origin feature/YourFeature)​

- Open a pull request
