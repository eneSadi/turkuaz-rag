news = {
    "title": "title1",
    "date": "date1",
    "summary": "summary1",
    "text": "text1"
}

similar_sample = {
    "title": "title2",
    "date": "date2",
    "summary": "summary2",
    "text": "text2"
}


comparison_question_template = f"""
The following are the metadata of 2 news articles and summaries of articles. The articles are related to a similar topic.
Your task is to generate a comparison question based on these articles.

**Comparison Questions**: 
A comparison question should compare factual elements explicitly stated in both articles to find where they agree or differ.
The correct answer to the question should be expressed as a comparative adjective, a statement of alignment, or a simple yes or no.
Make sure that the question requires information from both articles to be answered.
Compare factual details, numerical values, opinions, or descriptive elements in both articles without relying on time-based aspects.

**Requirements for the question:**
1. The question must require information from both articles to be answered accurately.
2. Ensure the question is coherent, flows logically, and is clear and unambiguous.
3. **Avoid vague references** such as:
   - ❌ *"Her iki haberde de geçen..."*
   - ❌ *"İki haberde de bahsedilen..."*
   - ❌ *"Bu iki makalede..."*
4. **Instead, directly reference the events, topics, or entities in each article.** The question should explicitly mention the distinguishing elements of both articles.
   ✅ **Correct format examples:**
   - *"X olayının anlatıldığı haber ile Y olayının anlatıldığı haberde..."*
   - *"A konusunun ele alındığı makale ile B konusunun ele alındığı makaleye göre..."*
5. The question must be written in Turkish.

News 1:
Title: {news['title']}
Date: {news['date']}
Summary: {news['summary']}
Text: {news['text']}

News 2:
Title: {similar_sample['title']}
Date: {similar_sample['date']}
Summary: {similar_sample['summary']}
Text: {similar_sample['text']}

Your output should be formatted as follows:
Question:
"""
