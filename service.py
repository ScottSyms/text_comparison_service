from fastapi import FastAPI
from pydantic import BaseModel
import evaluate
import nltk


class Text(BaseModel):
    text1: str
    text2: str
    lang: str


app = FastAPI()


@app.post("/")
async def pass_text(item: Text):
    return item


@app.post("/googlebleu")
async def pass_text(item: Text):
    e = evaluate.load("google_bleu")
    return e.compute(predictions=[item.text1], references=[item.text2])


@app.post("/meteor")
async def pass_text(item: Text):
    e = evaluate.load("meteor")
    return e.compute(predictions=[item.text1], references=[item.text2])


@app.post("/bertscore")
async def pass_text(item: Text):
    try:
        e = evaluate.load("bertscore")
        return e.compute(predictions=[item.text1], references=[item.text2], lang=item.lang)
    except:
        return '{"Not Available"}'


@app.post("/wer")
async def pass_text(item: Text):
    try:
        e = evaluate.load("wer")
        return e.compute(predictions=[item.text1], references=[item.text2])
    except:
        return '{"Not Available"}'

@app.post("/bleu")
async def pass_text(item: Text):
    try:
        e = evaluate.load("bleu")
        return e.compute(predictions=[item.text1], references=[item.text2])
    except:
        return '{"Not Available"}'

@app.post("/rouge")
async def pass_text(item: Text):
    try:
        e = evaluate.load("rouge")
        return e.compute(predictions=[item.text1], references=[item.text2])
    except:
        return '{"Not Available"}'


@app.post("/sacrebleu")
async def pass_text(item: Text):
    try:
        e = evaluate.load("sacrebleu")
        return e.compute(predictions=[item.text1], references=[item.text2])
    except:
        return '{"Not Available"}'
