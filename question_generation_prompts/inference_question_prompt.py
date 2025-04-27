sample = {
    0: { # news i
        "title": "title1",
        "date": "date1",
        "summary": "summary1",
        "text": "text1"
    },
    1: ["summary_sentence1", "summary_sentence2", "summary_sentence3", "summary_sentence4", "summary_sentence5"], # summary sentences i
    2: { # news j
        "title": "title2",
        "date": "date2",
        "summary": "summary2",
        "text": "text2"
    },
    3: ["summary_sentence1", "summary_sentence2", "summary_sentence3", "summary_sentence4", "summary_sentence5"], # summary sentences j
    4: ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"], # common keywords
    5: ["ner1", "ner2", "ner3", "ner4", "ner5"] # common ners
}

inference_question_template = f"""A multi-hop question is a question that is requiring multiple inferential leaps or accessing several pieces of information from different locations or sources to arrive at an answer. The following are the metadata of 2 news articles, summaries of articles, 5 summarizing sentences for each news and texts of the news. Both news are related to the same topic and have the same entity (or entities): {' ,'.join(sample[5])}. Your task is to generate one multi-hop inference question based on the news. Here are some instructions:
1. Find the Connection: The connection between news is entity (or entities): {' ,'.join(sample[5])}, which is how this key piece of information is related or how they can be combined to form a more complex idea.
2. Formulate the Question: Create a question that cannot be answered by relying on just one of the sentences but instead requires understanding and linking the information from all of the sources. The answer must be the entity (or one of the entities): {' ,'.join(sample[5])}.
3. Ensure Coherence: Make sure the question flows logically from the combined information and is clear and unambiguous.
4. Do not use the answer in the question: You must use other details from both news in the question but do not use the entity (answer) in the question.
5. Generate the answer: Generate the answer for the question, it must be the entity (or one of the entities): {' ,'.join(sample[5])}.
(the question and the answer should be in Turkish)

News 1:
Title: {sample[0]['title']}
Date: {sample[0]['date']}
Summary: {sample[0]['summary']}
Text: {sample[0]['text']}
Summary Sentences: {sample[1]}

News 2:
Title: {sample[2]['title']}
Date: {sample[2]['date']}
Summary: {sample[2]['summary']}
Text: {sample[2]['text']}
Summary Sentences: {sample[3]}

Your answer should be in the following format:
Question:
Answer:
"""