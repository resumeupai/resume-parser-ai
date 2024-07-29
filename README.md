# Resume Parser AI

🎉 Welcome to Resume Parser AI - your go-to package for parsing resumes and extracting structured data using the OpenAI API! 🎉

With this package, you can easily extract personal information, skills, work experience, education, and more from resumes in PDF and DOCX formats.

## Installation

You can install Resume Parser AI using pip:

```bash
pip install resume-parser-ai
```

## Usage
To parse a resume and extract data, use the parse function:

```bash
from resume_parser import ResumeParser

api_key = "your_openai_api_key"
model = "gpt-4"

parser = ResumeParser(api_key=api_key, model=model)
resume_data = parser.parse("path/to/resume.pdf")

print(resume_data)
```

## Default JSON Structure
The default JSON structure includes the following sections and fields:

```bash
{
    "personal_information": {
        "first_name": "",
        "last_name": "",
        "phone_number": "",
        "email_address": "",
        "linkedin_url": "",
        "website_url": "",
        "headline": ""
    },
    "skill": {
        "category": "",
        "skill_values": []
    },
    "work_experience": [{
        "company_name": "",
        "job_title": "",
        "city": "",
        "country": "",
        "from_date": "",
        "to_date": "",
        "description": ""
    }],
    "education": [{
        "institution_name": "",
        "field_of_study": "",
        "degree": "",
        "grade": "",
        "city": "",
        "country": "",
        "from_date": "",
        "to_date": "",
        "description": ""
    }],
    "certifications": [{
        "certification_name": "",
        "issuer": "",
        "certification_date": "",
        "certification_expiry_date": "",
        "certification_url": "",
        "description": ""
    }],
    "summary": {
        "profile": ""
    },
    "achievements": {
        "achievements": ""
    },
    "projects": [{
        "title": "",
        "project_role": "",
        "city": "",
        "country": "",
        "from_date": "",
        "to_date": "",
        "description": ""
    }]
}
```
## Links
If you want to build and analyze resumes without writing any code, check out our website [ResumeUp.ai](https://resumeup.ai). You can use our platform to generate resumes with AI and get detailed analysis of your resumes.

## Contributing
If you have any ideas or suggestions for improving this package, feel free to open an issue or submit a pull request on [GitHub](https://github.com/resumeupai/resume-parser-ai).

We appreciate your contributions! 😊
