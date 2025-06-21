# FastAPI Simple API Project

## Description  
A simple FastAPI project that returns information about a car.  
This project is for learning and practicing Python APIs.

---

## Requirements  

- Python 3.7 or higher installed  
- Pip package manager installed  

---

## Installation & Running the API (all in one)

Open your terminal and run these commands:

### Windows

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn requests
uvicorn main:app --reload
Linux / MacOS
bash
Copiar
Editar
git clone https://github.com/your-username/your-repository.git
cd your-repository
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn requests
uvicorn main:app --reload
Available Routes
GET /Carro
Returns car information in JSON format.

Automatic documentation
Visit in browser:

arduino
Copiar
Editar
http://127.0.0.1:8000/docs
Testing the API with Python
Use the test.py script to test the /Carro endpoint:

python
Copiar
Editar
import requests

url = "http://127.0.0.1:8000/Carro"
response = requests.get(url)
print(response.json())
