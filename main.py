from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.post("/analizeaza")
def analizeaza(body: TextInput):
    text = body.text
    char_count = len(text)
    word_count = len(text.split())
    vowels = sum(1 for c in text.lower() if c in "aeiouăîâ")

    if char_count == 0:
        comment = "Ai trimis... nimic. Filosof detectat."
    elif char_count < 10:
        comment = "Scurt si la obiect. Respect."
    elif char_count < 50:
        comment = "Nici prea mult, nici prea putin. Perfect."
    else:
        comment = f"Wow, {char_count} caractere! Esti un scriitor in devenire."

    return {
        "caractere": char_count,
        "cuvinte": word_count,
        "vocale": vowels,
        "comentariu": comment,
    }
