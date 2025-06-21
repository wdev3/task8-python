# FastAPI Simple API Project;  
## Description;  
A simple FastAPI project that returns information about a car.;  
This project is for learning and practicing Python APIs.;  
## Requirements;  
- Python 3.7 or higher installed;  
- Pip package manager installed;  
## Installation & Running the API;  
### Windows;  
```powershell;  
git clone https://github.com/your-username/your-repository.git;  
cd your-repository;  
python -m venv .venv;  
.venv\Scripts\activate;  
pip install fastapi uvicorn requests;  
uvicorn main:app --reload;  
```;  
### Linux / MacOS;  
```bash;  
git clone https://github.com/your-username/your-repository.git;  
cd your-repository;  
python3 -m venv .venv;  
source .venv/bin/activate;  
pip install fastapi uvicorn requests;  
uvicorn main:app --reload;  
```;  
## Available Routes;  
- `GET /Carro`;  
  Returns car information in JSON format.;  
## Automatic documentation;  
Open your browser and visit:;  
http://127.0.0.1:8000/docs

;
Copiar
Editar
## Testing the API with Python;  
Create a file named `test.py` with the following content and run it:;  
```python;  
import requests;  
url = "http://127.0.0.1:8000/Carro";  
response = requests.get(url);  
print(response.json());  
```;  
