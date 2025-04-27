from openai import OpenAI
from tqdm import tqdm
import json
import time

TEMPLATES_FILE_PATH = "huggingface_dataset.jsonl"
OUTPUT_PATH = "huggingface_dataset_with_answers.jsonl"

PROMPT_FIELD = "prompt_with_both_news"
ANSWER_FIELD = "answer_with_both_news"

client = OpenAI(api_key="", base_url="https://api.deepseek.com")

with open(TEMPLATES_FILE_PATH, "r") as f:
    ready_templates = [json.loads(line) for line in f.readlines()]

counter = 0
checkpoint = 0

for template in tqdm(ready_templates, total=len(ready_templates)):

    if counter < checkpoint:
        counter += 1
        continue
    time.sleep(1)

    prompt = template[PROMPT_FIELD]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=256,
        temperature=0.2,  # Lower temperature to reduce creative/hallucinatory outputs
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stream=False
    )

    conversation_text = response["choices"][0]["message"]["content"].strip()
    print(conversation_text)

    template[ANSWER_FIELD] = conversation_text

    # Append result to .jsonl file
    with open(OUTPUT_PATH, "a") as f:
        f.write(json.dumps(template) + "\n")

    print("Result appended to the file")

    counter += 1
    if counter % 10 == 0:
        print(f"Completed {counter} templates")