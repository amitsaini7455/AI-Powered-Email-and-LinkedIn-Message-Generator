![screenshort landing page](https://github.com/user-attachments/assets/a87c5465-86f2-42c2-bbd6-4b34191f91bb)

![output page](https://github.com/user-attachments/assets/3e8cff9e-3488-4b8c-bfda-2f59c28def95)

AI-Powered Email and LinkedIn Message Generator 🚀 
Welcome to the AI-Powered Mail and LinkedIn Message Generator! This application helps recruiters effortlessly craft professional LinkedIn messages tailored to candidates. Leverage AI to save time and focus on what matters most — connecting with talent!

Features ✨
AI-Generated LinkedIn Messages: Generate professional and personalized LinkedIn messages based on candidate details.
Multi-Format Support: Download messages as PDF or DOCX files.
Customizable Input: Input candidate name, skills, job position, and company details for a personalized output.
Streamlined UX: Built with an interactive and user-friendly interface using Streamlit.
Gemini AI Integration: Leverages Gemini AI for content generation, ensuring polished and contextually accurate messages.
How It Works 🔧
Input Fields:

Candidate Name
Skills (comma-separated)
Job Position
Company Name
Optional: Recruiter's name, phone number, and company website link.
AI Processing:

Uses Gemini 1.5 Flash model from Google Generative AI to create customized messages based on the provided details.
Output:

Displays the generated LinkedIn message on the screen.
Provides options to download the message as:
PDF
DOCX
Technology Stack 🛠
Programming Language: Python 3.11
Framework: Streamlit
AI Model: Google Generative AI (Gemini 1.5 Flash)
Libraries:
Streamlit - For building the web application.
FPDF - For generating PDF files.
python-docx - For creating DOCX files.
Google Generative AI - For generating LinkedIn messages.
Installation 🛠
Clone this repository:

bash
Copy code
git clone (https://github.com/amitsaini7455/AI-Powered-Email-and-LinkedIn-Message-Generator)
cd ai-message-generator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your Gemini API Key:

Get your API key from Google Generative AI.
Add it to your environment:
bash
Copy code
export GEMINI_API_KEY="YOUR_API_KEY"
Run the application:

bash
Copy code
streamlit run app.py
Usage 🎉
Open the application in your browser (usually at http://localhost:8501).
Fill in the required fields.
Click Generate LinkedIn Message.
Review the generated message and download it in your preferred format.
Example Output 📋
Input:

Candidate Name: John Doe
Skills: Python, Machine Learning, Data Science
Job Position: Data Scientist
Company Name: AI Solutions
Generated Message:

Dear John Doe,
I came across your impressive profile featuring expertise in Python, Machine Learning, and Data Science. At AI Solutions, we are looking for a talented Data Scientist, and your skill set aligns perfectly with the role.
I would love to discuss this opportunity further. Feel free to reach out or explore our company website for more details.
Best regards,
[Your Name]

Contributing 🤝
We welcome contributions! Feel free to submit issues or pull requests to enhance this project.

License 📜
This project is licensed under the MIT License.

Acknowledgments 🙌
Google Generative AI for their powerful text-generation model.
Streamlit for simplifying the development of interactive web apps.
