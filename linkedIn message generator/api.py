import os
import google.generativeai as genai

# Set the API key for Gemini AI
os.environ["GEMINI_API_KEY"] = "Add your GEMINI_API_KEY"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", #add your AI and LLM model i my case i have "gemini-1.5-flash"
    generation_config=generation_config,
)


def generate_message(name: str, skills: list, position: str, company: str, recruiter: str = "", phone: str = "", website: str = "") -> str:
    """
    Generate a LinkedIn message using the Gemini AI API.

    Args:
        name (str): Candidate's name.
        skills (list): List of candidate's skills.
        position (str): Job position.
        company (str): Company name.
        recruiter (str): Recruiter's name and designation (optional).
        phone (str): Recruiter's phone number (optional).
        website (str): Company website link (optional).

    Returns:
        str: Generated LinkedIn message.
    """
    recruiter_info = f"My name is {recruiter} and I'm a recruiter at {company}. " if recruiter else ""
    phone_info = f"You can reach me at {phone}. " if phone else ""
    website_info = (
        f"Feel free to visit our website to learn more about {company}: [{website}]({website}). " if website else ""
    )

    jd_template = f"""
    You are a company recruiter. Write a LinkedIn message for a candidate.
    {recruiter_info}{phone_info}{website_info}
    Candidate Name: {name}
    Candidate Skills: {', '.join(skills)}
    Job Position: {position}
    Company Name: {company}
    """
    try:
        response = model.generate_content([jd_template])
        return response.text.strip()
    except Exception as e:
        return f"Error generating LinkedIn message: {str(e)}"
