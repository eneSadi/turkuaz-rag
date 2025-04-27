from tqdm import tqdm
import json
import time
from google import genai

# Load API key
with open("google_gemini_key.txt", "r") as f:
    api_key = f.read().strip()
client = genai.Client(api_key=api_key)

# Define paths and fields
TEMPLATES_FILE_PATH = "huggingface_dataset.jsonl"
OUTPUT_PATH = "huggingface_dataset_with_answers.jsonl"

PROMPT_FIELD_BOTH = "prompt_with_both_news"
PROMPT_FIELD_SINGLE = "prompt_with_single_news"
PROMPT_FILED_FOR_FINAL_ANSWER = "prompt_for_final_answer"
ANSWER_FIELD_BOTH = "answer_with_both_news"
ANSWER_FIELD_SINGLE = "answer_with_single_news"
ANSWER_FIELD_FOR_FINAL_ANSWER = "final_answer_for_dataset"

# Load dataset
with open(TEMPLATES_FILE_PATH, "r") as f:
    ready_templates = [json.loads(line) for line in f.readlines()]

# Rate limiting: 15 RPM → 4 sec between requests
RATE_LIMIT_SECONDS = 0
NONE_RESPONSE_COUNT = 0

def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    time.sleep(RATE_LIMIT_SECONDS)
    if response.text is None:
        global NONE_RESPONSE_COUNT
        NONE_RESPONSE_COUNT += 1
        if NONE_RESPONSE_COUNT > 5:
            print("No response received. Exiting.")
            exit(1)
        return "Yetersiz bilgi".strip()
    return response.text.strip()

counter = 0
checkpoint = 0

for template in tqdm(ready_templates, total=len(ready_templates)):
    if counter < checkpoint:
        counter += 1
        continue

    # --- Generate Answer Using Both News ---
    prompt = template[PROMPT_FIELD_BOTH]
    conversation_text = get_response(prompt)

    print("\n" + "*" * 150)
    print("Question Type: ", template["question_type"])
    print("Question: ", template["question"])
    print("Given Answer:\n", template["answer"])
    print("Generated Answer for Both News:\n", conversation_text)
    template[ANSWER_FIELD_BOTH] = conversation_text

    # --- Generate Answer Using One Random News ---
    prompt = template[PROMPT_FIELD_SINGLE]
    conversation_text = get_response(prompt)
    print("Generated Answer for Single News:\n", conversation_text)
    template[ANSWER_FIELD_SINGLE] = conversation_text

    # --- Final Answer ---
    prompt = template[PROMPT_FILED_FOR_FINAL_ANSWER]
    conversation_text = get_response(prompt)
    print("Generated Final Answer:\n", conversation_text)
    template[ANSWER_FIELD_FOR_FINAL_ANSWER] = conversation_text
    print("*" * 150)

    # Save result to file
    with open(OUTPUT_PATH, "a") as f:
        f.write(json.dumps(template, ensure_ascii=False) + "\n")

    counter += 1
    if counter == 10000:
        print(f"✅ Completed {counter} templates.")
        break
