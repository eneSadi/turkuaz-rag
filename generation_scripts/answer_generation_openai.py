from tqdm import tqdm
import json
import time
import os
import openai
import random

with open("openai_key.txt", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()
openai.api_key = os.getenv("OPENAI_API_KEY")


TEMPLATES_FILE_PATH = "huggingface_dataset.jsonl"
OUTPUT_PATH = "huggingface_dataset_with_answers.jsonl"

PROMPT_FIELD_BOTH = "prompt_with_both_news"
PROMPT_FIELD_SINGLE = ["prompt_with_news1", "prompt_with_news2"]
PROMPT_FILED_FOR_FINAL_ANSWER = "prompt_for_final_answer"
ANSWER_FIELD_BOTH = "answer_with_both_news"
ANSWER_FIELD_SINGLE = "answer_with_single_news"
ANSWER_FIELD_FOR_FINAL_ANSWER = "final_answer_for_dataset"


with open(TEMPLATES_FILE_PATH, "r") as f:
    ready_templates = [json.loads(line) for line in f.readlines()]

counter = 0
checkpoint = 0

for template in tqdm(ready_templates, total=len(ready_templates)):

    if counter < checkpoint:
        counter += 1
        continue
    time.sleep(1)

    prompt = template[PROMPT_FIELD_BOTH]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
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
    print()
    print('*' * 150)
    print("Question Type: ", template["question_type"])
    print("Question: ", template["question"])
    print("Given Answer:\n", template["answer"])
    print()
    print("Generated Answer for Both News:\n", conversation_text)

    template[ANSWER_FIELD_BOTH] = conversation_text

    time.sleep(1)

    # random selection of single news
    single_news_index = random.choice([0, 1])
    prompt = template[PROMPT_FIELD_SINGLE[single_news_index]]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
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

    print("Generated Answer for Single News:\n", conversation_text)
    template[ANSWER_FIELD_SINGLE] = conversation_text

    time.sleep(1)

    # Generate final answer
    prompt = template[PROMPT_FILED_FOR_FINAL_ANSWER]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
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

    print("Generated Final Answer:\n", conversation_text)
    template[ANSWER_FIELD_FOR_FINAL_ANSWER] = conversation_text
    print('*' * 150)


    # Append result to .jsonl file
    with open(OUTPUT_PATH, "a") as f:
        f.write(json.dumps(template) + "\n")

    counter += 1
    if counter == 10000:
        print(f"Completed {counter} templates")
        break