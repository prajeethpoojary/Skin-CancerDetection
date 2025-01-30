import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Set Page Configuration
st.set_page_config(
    page_title="Diagnose.AI - Skin Cancer Detection",
    page_icon="♋",
    layout="wide",
)

# Load Models
@st.cache_resource
def load_resnet50_model():
    return load_model(r'D:\final project\project\ResNet50\trained_model.h5')

@st.cache_resource
def load_efficientnetb5_model():
    return load_model(r'D:\final project\project\EfficientNetB5\model.h5')

# Sidebar Content
with st.sidebar:
    st.image("https://via.placeholder.com/300x150.png?text=Diagnose.AI", use_container_width=True)
    st.title("Diagnose.AI")
    st.markdown(
        """
        Diagnose.AI leverages cutting-edge AI models to predict skin cancer lesions as 
        either **Benign** or **Malignant**.  
        🩺 **Choose a model, upload an image, and let AI assist you!**  
        ⚠️ **Note:** This is not a substitute for a professional diagnosis.
        """,
        unsafe_allow_html=True,
    )

# Main Header
st.markdown(
    "<h1 style='text-align: center;'>Diagnose.AI - Skin Cancer Detection</h1>",
    unsafe_allow_html=True,
)

# Model Selection
st.markdown("### Select a Model")
model_selection = st.radio(
    "Choose a prediction model:",
    ["ResNet50 (trained_model.h5)", "EfficientNetB5 (model.h5)"],
    horizontal=True,
)

if model_selection == "ResNet50 (trained_model.h5)":
    model = load_resnet50_model()
    input_size = (224, 224)
else:
    model = load_efficientnetb5_model()
    input_size = (256, 256)

# File Upload Section
st.markdown("### Upload an Image")
pic = st.file_uploader(
    label="Upload a picture of your skin lesion",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
)

# Preprocess Image
def preprocess_image(image):
    image = image.convert('RGB')
    resized_image = image.resize(input_size)
    image_array = img_to_array(resized_image)
    image_array /= 255.0
    return np.expand_dims(image_array, axis=0)

# Initialize a flag for the doctor info display
if "show_doctor_page" not in st.session_state:
    st.session_state["show_doctor_page"] = False

# Display the results
if st.button("Predict"):
    if not pic:
        st.error("Please upload an image to proceed.")
    else:
        try:
            with st.spinner("Analyzing the image..."):
                image = Image.open(pic)
                inp = preprocess_image(image)
                prediction = model.predict(inp)

                # Results Processing
                classes = ['Benign', 'Malignant']
                pred_class = np.argmax(prediction)
                confidence, pred_class_name = prediction[0][pred_class], classes[pred_class]
                confidence_percentage = round(confidence * 100, 2)

                # Display Results
                st.markdown("---")
                st.header("Prediction Results")
                cols = st.columns([1, 2])
                with cols[0]:
                    st.image(pic, caption="Uploaded Image", use_container_width=True)
                with cols[1]:
                    st.markdown(
                        f"""
                        <div style="font-size:1.5rem; font-weight:bold;">Prediction: {pred_class_name}</div>
                        <div style="font-size:1.2rem; color:#e74c3c;">Confidence Level: {confidence_percentage}%</div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.progress(int(confidence_percentage))

                # Button to show doctor page





                # Disclaimer
                st.warning(
                    "⚠️ This is not a medical diagnosis. Please consult a dermatologist for a professional opinion.",
                    icon="⚠️",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")


# Check if session state is initialized
if "show_doctor_page" not in st.session_state:
    st.session_state["show_doctor_page"] = False

# Button to show doctor page
if st.button("Book Dermatologist Appointment Near Me", key="doctor_button"):
    st.session_state["show_doctor_page"] = True
    st.rerun()  # Trigger re-run after state change

# Show Doctor Page Content
if st.session_state["show_doctor_page"]:
    def send_email(to_email, subject, body):
        try:
            # Set up the email server (Gmail SMTP)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Secure the connection
            server.login("your_email@gmail.com", "your_password")  # Replace with your email and password

            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = "your_email@gmail.com"  # Replace with your email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail("your_email@gmail.com", to_email, msg.as_string())
            server.quit()

            st.success(f"Email successfully sent to {to_email}!")
        except Exception as e:
            st.error(f"Error sending email: {e}")


    dermatologists = [
        {"name": "Skin 360", "address": "Near sharada vidyalaya, sai sharada building, Kodailbail, Mangaluru, Karnataka 575003, India", "email": "info@skin360.com"},
        {"name": "Belaku Skin Clinic", "address": "Belaku clinic, Bejai, Mangaluru, Karnataka 575004, India", "email": "info@belakuskincare.com"},
        {"name": "Dr. Pramod Kumar's Skin Clinic. Skin Specialist, Mangalore", "address": "City Plaza, 209-210, KRR Road, near PVS circle, Tilak Nagar, Boloor, Kodailbail, Mangaluru, Karnataka 575003, India", "email": "drpramod@skinclinic.com"},
        {"name": "The Skin Clinic", "address": "Vyasa Rao Road, Kadri Kambla Rd, Mallikatte, Kadri, Mangaluru, Karnataka 575002, India", "email": "contact@theskinclinic.com"},
        {"name": "Pulse Skin & Hair Clinic", "address": "Ground Floor, Inland Avenue, MG Rd, opposite Sanjeeva Shetty Silks, Ballalbagh, Lalbagh, Mangaluru, Karnataka 575003, India", "email": "pulseclinic@mangalore.com"},
        {"name": "Dr. Kashinath Nayak | Best Dermatologist in Mangalore", "address": "Room no.2, 1st floor, KMC Hospital Dr.B R Ambedkar Circle, Hampankatta, Mangaluru, Karnataka 575002, India", "email": "drkashinath@kmcderma.com"},
    ]

    # Streamlit title and description
    st.title("Nearby Dermatologists")
    st.markdown(
        """
        Below is the list of dermatologists near you.  
        You can contact them directly via email with details about the lesion.
        """,
        unsafe_allow_html=True,
    )

    # Loop through dermatologists and show info
    for doc in dermatologists:
        st.subheader(doc["name"])
        st.text(doc["address"])

        # Email body template
        email_body = f"""
        Dear {doc['name']},

        I would like to consult with you regarding a skin lesion. Attached is an image of the lesion detected. 
        Please let me know your availability.

        Thanks,  
        [Your Name]
        """

        # Display email link (for manual email)
        st.markdown(
            f"[📧 Contact via Email](mailto:{doc['email']}?subject=Skin Lesion Consultation&body={email_body})",
            unsafe_allow_html=True,
        )

        # Send email button
        if st.button(f"Send Email to {doc['name']}"):
            # Automatically send email on button click
            send_email(doc['email'], "Skin Lesion Consultation", email_body)

        st.markdown("---")

