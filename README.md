# FastAPI Car API

## Description

A simple FastAPI project that serves basic car information via an API endpoint. This is for learning and practicing Python APIs.

## Quick Start

Follow these steps to run the API locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```
    (Remember to replace `your-username/your-repository.git` with your actual repository link.)

2.  **Set up a virtual environment and install dependencies:**
    ```bash
    python3 -m venv .venv  # Use 'python' instead of 'python3' on some systems (e.g., Windows)
    source .venv/bin/activate # Use '.venv\Scripts\activate' on Windows
    pip install fastapi uvicorn
    ```

3.  **Run the API server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

## API Endpoint

-   **`GET /Carro`**: Returns car information in JSON format.
    * Example response:
        ```json
        {
          "marca": "Toyota",
          "modelo": "Corolla",
          "ano": 2023
        }
        ```

## Testing the API

Open your browser and visit `http://127.0.0.1:8000/docs` for interactive documentation, or use this Python script:

```python
import requests

url = "[http://127.0.0.1:8000/Carro](http://127.0.0.1:8000/Carro)"
response = requests.get(url)

if response.status_code == 200:
    print("Success! API Response:")
    print(response.json())
else:
    print(f"Error accessing the API. Status Code: {response.status_code}")
    print(response.text)
