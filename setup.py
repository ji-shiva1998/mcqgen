from setuptools import find_packages, setup

setup (
    name = "mcqgenerator",
    version = "0.0.1",
    author = "shiva shaankar",
    author_email = "ji.shiva1998@gmail.com",
    install_requires = ["openai", "langchain", "streamlit", "python_dotenv", "PyPDF2"],
    pakages = find_packages()
)