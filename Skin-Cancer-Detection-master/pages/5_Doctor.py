import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
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

# Streamlit UI
st.set_page_config(page_title="Nearby Dermatologists", page_icon="🩺")

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

