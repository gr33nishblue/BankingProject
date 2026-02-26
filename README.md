# Create a Virtual Environement

python -m venv .venv  

# Activate the virtual environment:

On Windows:  
.venv\Scripts\activate.bat  

On Unix or MacOS:  
source .venv/bin/activate  

# Install dependencies:
pip install -r requirements.txt  

# Run tests with pytest: // --headless is optional

pytest --browser=chrome --headless  
pytest --browser=firefox --headless  
pytest --browser=edge  

# Run tests and generate report:
pip install pytest-html  
pytest --html=reports/report.html --self-contained-html