from pathlib import Path
import llm
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

model = llm.get_model("gpt-3.5-turbo")
model.key = 

@app.get("/")
async def root():
    return FileResponse('index.html')
    # content = Path('index.html').read_text()
    # return HTMLResponse(content=content)

@app.post('/factcheck')
async def factcheck():
    sample =   {
        'claims': [
            'what is your name?',
            'what is your quest?',
        ]
    }
    return JSONResponse(content=sample)


app.mount('/static', app=StaticFiles(directory='static'), name='static')
