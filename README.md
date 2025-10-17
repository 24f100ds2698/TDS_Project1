# TDS_Project1

## Project Summary

This project is part of the IIT Madras TDS Sep 2025 LLM Code Deployment assignment. It automates the process of receiving a task brief, generating an app, deploying to GitHub Pages, and reporting results for evaluation.

## Setup Instructions

1. Clone the repository

2.(Optional) Create and activate a virtual environment

3. Install dependencies
4. 
## Usage

- Start the FastAPI server:
- The API endpoint will be available at `http://127.0.0.1:8000/api-endpoint`.
- Use the `/docs` page for interactive API testing.

## Code Explanation

- `api.py`: Main FastAPI app. Receives POST requests, validates the secret, and automates repo creation and deployment.
- Uses PyGithub to create and manage GitHub repositories.
- Handles all required project automation steps.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Next step:**  
Let me know when you’ve updated your README.md, and I’ll give you the `.gitignore` file to add!






