
import streamlit as st
from api import generate_message
from fpdf import FPDF
from docx import Document
import io  # Needed for in-memory file generation


def generate_pdf(message: str) -> bytes:
    """
    Generate a PDF file with the provided message.

    Args:
        message (str): The LinkedIn message.

    Returns:
        bytes: PDF content as bytes.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, message)
    return pdf.output(dest="S").encode("latin1")  # Convert to bytes


def generate_docx(message: str) -> bytes:
    """
    Generate a DOCX file with the provided message.

    Args:
        message (str): The LinkedIn message.

    Returns:
        bytes: DOCX content as bytes.
    """
    doc = Document()
    doc.add_paragraph(message)
    doc_bytes = io.BytesIO()
    doc.save(doc_bytes)
    doc_bytes.seek(0)  # Reset the pointer to the start of the file
    return doc_bytes.read()


# Streamlit app title
st.title("Ai Powered Mail And LinkedIn Message Generator")

# Input fields for candidate details
name = st.text_input("Candidate Name", placeholder="Enter the candidate's name")
skills_input = st.text_input(
    "Candidate Skills (comma-separated)", placeholder="e.g., JavaScript, React, Node.js"
)
position = st.text_input("Job Position", placeholder="Enter the job position")
company = st.text_input("Company Name", placeholder="Enter the company name")
recruiter = st.text_input(
    "Recruiter's Name (Optional)", placeholder="Enter your name and designation, e.g., John Doe, Senior Recruiter"
)
phone = st.text_input(
    "Recruiter's Phone Number (Optional)", placeholder="Enter your phone number, e.g., +1-234-567-8901"
)
website = st.text_input(
    "Company Website (Optional)", placeholder="Enter your company website link, e.g., https://example.com"
)

# Generate LinkedIn message button
if st.button("Generate LinkedIn Message"):
    if not name or not skills_input or not position or not company:
        st.error("Please fill in all the mandatory fields!")
    else:
        # Process the input skills
        skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

        # Call the backend function
        with st.spinner("Generating message..."):
            message = generate_message(name, skills, position, company, recruiter, phone, website)

        # Display the generated message
        st.subheader("Generated LinkedIn Message")

        # Display message with option to copy using st.code
        st.code(message, language="text")

        # Add a button to download the message as a PDF
        pdf_data = generate_pdf(message)  # Generate the PDF bytes
        st.download_button(
            label="Download as PDF",
            data=pdf_data,
            file_name="LinkedIn_Message.pdf",
            mime="application/pdf",
        )

        # Add a button to download the message as a DOCX
        docx_data = generate_docx(message)  # Generate the DOCX bytes
        st.download_button(
            label="Download as DOCX",
            data=docx_data,
            file_name="LinkedIn_Message.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
