import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("cat_vs_dog_model.h5")
    return model

model = load_model()

# UI
st.title("🐶 Cat vs Dog Classifier 🐱")
st.write("Upload an image and I'll tell you if it's a cat or a dog!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocessing
    img = image.resize((256, 256))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    prediction = model.predict(img_array)[0][0]
    label = "🐶 Dog" if prediction > 0.5 else "🐱 Cat"
    st.success(f"Prediction: {label}")
