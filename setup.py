# setup.py

from setuptools import setup, find_packages

setup(
    name='resume-parser-ai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pdfplumber',
        'python-docx',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'resume-parser=resume_parser.core:ResumeParser',
        ],
    },
    author="ResumeUp.AI",
    author_email="accounts@resumeup.ai",
    description="A package to parse resumes and extract structured data using OpenAI API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/resumeupai/resume-parser-ai",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
