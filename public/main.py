from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Load HTML file
with open("index.html", "r") as file:
    html_content = file.read()

@app.get("/", response_class=HTMLResponse)
def root():
    return HTMLResponse(content=html_content, status_code=200)