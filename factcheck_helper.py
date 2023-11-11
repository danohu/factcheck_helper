from pathlib import Path
import llm
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# replace with your own key
from secrets import openai_api_key

app = FastAPI()

model = llm.get_model("gpt-4")
model.key = openai_api_key

base_prompt = '''
Your job is to assist a newspaper fact-checker. Read the following draft article, and compile a list of assertions which need to be proved.
List the assertions one per line. Write the assertion in a terse style, omitting stylistic details.
Each assertion should contain a single claim that can be checked independently.
Rewrite each assertion so that it can be understood independently -- for example, replace pronouns by the name of the person they refer to.
Write at least 20 assertions.
Do not compile multiple claims in a single line.
Do not include anything else in your response.
The article follows:

'''

def get_openai_response(user_prompt):
    full_prompt = base_prompt + user_prompt
    response = model.prompt(full_prompt, max_tokens=1000).text()
    print(response)
    return response.split('\n')

class FactCheckRequest(BaseModel):
    article: str

@app.get("/")
async def root():
    return FileResponse('index.html')
    # content = Path('index.html').read_text()
    # return HTMLResponse(content=content)

@app.post('/factcheck')
async def factcheck(request_data: FactCheckRequest):
    article_text = request_data.article
    response = get_openai_response(article_text)
    sample =   {
        'claims': response
    }
    return JSONResponse(content=sample)


app.mount('/static', app=StaticFiles(directory='static'), name='static')
