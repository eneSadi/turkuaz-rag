import requests
import datasets
from tqdm import tqdm
import pickle
import json

base_url="https://....hf.space/ask"

OUTPUT_PATH = "inference_question_NER_keyword_extraction_outputs.jsonl"

with open("mlsum_similar_news.pkl", "rb") as f:
    mlsum_similar_news = pickle.load(f)

def get_text_with_max_500_words(text):
    words = text.split()
    if len(words) > 500:
        return " ".join(words[:500])
    return text

def get_response(prompt):
    data = {"prompt": prompt}
    response = requests.post(base_url, json=data)
    print(f"Response: {response.json()['answer']}")

    if response.status_code == 200:
        print('Request successful!!')
        return response.json()['answer']
    else:
        response.raise_for_status()

dataset = datasets.load_from_disk("mlsum_train_dataset")


counter = 0
checkpoint = 0

for idx in tqdm(mlsum_similar_news, total=len(mlsum_similar_news)):
    if counter < checkpoint:
        counter += 1
        continue
    news = mlsum_similar_news[idx]
    similar_news_ids = news['similar_indices']

    similar_news = [dataset[i] for i in similar_news_ids]
    similar_news_ids = []
    for similar in similar_news:
        if news['date'] != similar['date']:
            similar_news_ids.append(similar['index'])

        if len(similar_news_ids) >= 5:
            break

    if len(similar_news_ids) <= 0:
        continue

    merged_news_ids = [idx] + similar_news_ids

    for id in merged_news_ids:
        news = dataset[id]
        news_text = get_text_with_max_500_words(news["text"])
        prompt = news["title"] + "\n" + news["summary"] + "\n" + news_text
        print("Prompt:\n", prompt)

        answer = get_response(prompt)
        print("Answer:\n", answer)

        result = {
            "news_id": id,
            "prompt": prompt,
            "answer": answer
        }

        # Append result to .jsonl file
        with open(OUTPUT_PATH, "a") as f:
            f.write(json.dumps(result) + "\n")

    counter += 1
