import streamlit as st

st.set_page_config(
    page_title="Skin Cancer",
    page_icon="♋",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Find a dermatologist")

city = (
    st.text_input(
        label="Enter your city",
        placeholder="City (e.g. New Delhi)",
        help="Enter the name of the city where you want to find a dermatologist",
    )
    .strip()
    .title()
)


dermatologists = [
    {"name": "Skin 360", "address": "Near sharada vidyalaya, sai sharada building, Kodailbail, Mangaluru, Karnataka 575003, India"},
    {"name": "Belaku Skin Clinic", "address": "Belaku clinic, Bejai, Mangaluru, Karnataka 575004, India"},
    {"name": "Dr. Pramod Kumar's Skin Clinic. Skin Specialist, Mangalore", "address": "City Plaza, 209-210, KRR Road, near PVS circle, Tilak Nagar, Boloor, Kodailbail, Mangaluru, Karnataka 575003, India"},
    {"name": "The Skin Clinic", "address": "Vyasa Rao Road, Kadri Kambla Rd, Mallikatte, Kadri, Mangaluru, Karnataka 575002, India"},
    {"name": "Pulse Skin & Hair Clinic", "address": "Ground Floor, Inland Avenue, MG Rd, opposite Sanjeeva Shetty Silks, Ballalbagh, Lalbagh, Mangaluru, Karnataka 575003, India"},
    {"name": "Dr. Kashinath Nayak | Best Dermatologist in Mangalore", "address": "Room no.2, 1st floor,KMC Hospital Dr.B R Ambedkar Circle, Hampankatta, Mangaluru, Karnataka 575002, India"},
    {"name": "Dr Vijetha Rai", "address": "2 nd floor mak park square, near father Muller convention centre, Pumpwell, Mangaluru, Karnataka 575002, India"},
    {"name": "Dr Sayeeda Mogral", "address": "1, Skin Clinic, Millennium Towers, opposite Highland Hospital, Tower, Kankanady, Mangaluru, Karnataka 575002, India"},
    {"name": "Dr. Akshata C Alva", "address": "Maurishka Towers, near vas bakery, Mallikatte, Kadri, Mangaluru, Karnataka 575001, India"},
    {"name": "Dr Mahesh Nair", "address": "Medical Chamber, Don Bosco Hall Cross Rd, near Don Bosco Hall, Falnir, Mangaluru, Karnataka 575001, India"},
    {"name": "Skin Code by Dr Snigdha Hegde", "address": "202, 2nd Floor, Lotus Paradise Plaza, beside St Theresa School, Bendoor, Mangaluru, Karnataka 575002, India"},
    {"name": "The First Layer - Female Dermatologist in Mangalore", "address": "1st floor, Lotus Dham, Mannagudda Rd, near Ghandi park, Gandhinagar, Mangaluru, Karnataka 575003, India"},
    {"name": "Dr Shyam Raj Rao", "address": "Silver springs, Bejai New Rd, Bejai, Mangaluru, Karnataka 575004, India"},
    {"name": "VISH Skin Clinic", "address": "1st Floor, Milestone 25 collectors gate circle, Mallikatte, Balmatta, Mangaluru, Karnataka 575002, India"},
    {"name": "Dr. K Narendra Kamath", "address": "CUTIS' 2nd Floor, 2nd Floor, Manasa Tower, MG Rd, near pvs circle, Kodailbail, Mangaluru, Karnataka 575003, India"},
    {"name": "UVA Skin, Hair & Cosmetology Clinic - Dr Myfanwy Dsouza", "address": "Shop 23, First Floor, Essel Willcon, Circle, above Radha Medicals, Bendoorwell, Kankanady, Mangaluru, Karnataka 575002, India"},
    {"name": "Derma-Care", "address": "The Trade Center, Bunts Hostel Rd, opposite Hotel Goldfinch, Hampankatta, Mangaluru, Karnataka 575003, India"},
    {"name": "Dr. Ganesh S. Pai-Dermatologist", "address": "The Trade Center, Bunts Hostel Rd, Jothi, Mangaluru, Karnataka 575003, India"},
    {"name": "Dr Anand Consultant Dermatologist", "address": "Light House Hill Rd, Hampankatta, Mangaluru, Karnataka 575003, India"},
    {"name": "Dr. Anusha Pai Mangalore", "address": "Ground Floor, The Trade Center, opposite Gold Finch Hotel, near Jothi Circle, Hampankatta, Mangaluru, Karnataka 575003, India"},
]


if st.button("Find a dermatologist"):
    if not city:
        st.error("Please enter a city")
    else:
        
        st.header("Results")
        for i, dermatologist in enumerate(dermatologists, start=1):
            st.markdown(
                f"""
                {i}. **{dermatologist['name']}**
                > **Address:** {dermatologist['address']}
                """
            )
