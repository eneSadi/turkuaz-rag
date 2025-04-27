import openai
from tqdm import tqdm
import os
import json
import time

with open("openai_key.txt", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()
openai.api_key = os.getenv("OPENAI_API_KEY")

TEMPLATES_FILE_PATH = "null_question_templates.json"
OUTPUT_PATH = "null_question_templates_outputs.jsonl"

with open(TEMPLATES_FILE_PATH, "r") as f:
    ready_templates = json.load(f)

counter = 0
checkpoint = 0

for template in tqdm(ready_templates, total=len(ready_templates)):

    if counter < checkpoint:
        counter += 1
        continue
    time.sleep(2)

    prompt = template["prompt"]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=256,
        temperature=0.3,  # Lower temperature to reduce creative/hallucinatory outputs
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    conversation_text = response["choices"][0]["message"]["content"].strip()
    print(conversation_text)

    result = {
        "news_1_id": template["news_1_id"],
        "news_2_id": template["news_2_id"],
        "prompt": prompt,
        "answer": conversation_text
    }

    # Append result to .jsonl file
    with open(OUTPUT_PATH, "a") as f:
        f.write(json.dumps(result) + "\n")

    print("Result appended to the file")

    counter += 1
    if counter % 10 == 0:
        print(f"Completed {counter} templates")