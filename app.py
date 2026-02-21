from fastapi import FastAPI 
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

## create a new FASTAPI app instance
app = FastAPI()

# Initialize the text generation pipeline
# Load model and tokenizer directly
model_id = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Define the pipe variable so the /generate endpoint can use it
# device=-1 ensures it runs on CPU as per our requirements.txt
pipe = pipeline(
    "text2text-generation", 
    model=model, 
    tokenizer=tokenizer, 
    device=-1
)

@app.get("/")
def home():
    return {"message": "Hello World"}

# Define a function to handle the GET request at /generate
@app.get("/generate")
def generate(text: str):
    ## use the pipeline to generate text from given input text
    output = pipe(text)
    
    ## return the generate text in Json response 
    # The indentation here is now fixed to prevent the previous error
    return {"output": output[0]['generated_text']}