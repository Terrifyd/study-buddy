# study-buddy

To download the needed dependencies, follow these steps:
	1. Download the repository.
	2. Open the command line and navigate to the directory where you downloaded the repo.
	3. In the command line, run 'pip install -r requirements.txt' to install the needed dependencies.


To set OPENAI_API_KEY in your enviornmental variables 
	1. download dotenv using pip
	2. make a .env file and add the line 'OPENAI_API_KEY = {key}'
	3. 'import os' and 'from dotenv import load_dotenv' in the file
	4. in the file run API_KEY = os.getenv('OPENAI_API_KEY')