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


temporal_question_template = f"""
The following are the metadata of 2 news articles and summaries of articles. The articles are related to a similar topic.
Your task is to generate a **Temporal Question** based on these articles.

A **Temporal Question** involves a **time-related comparison** between the events, entities, or facts presented in the two articles.
The question should **highlight chronological differences**, event sequences, durations, or trends over time, ensuring that answering it requires information from both articles.

### **Requirements for the question:**
1. **Your question should be like one of these categories (choose one randomly, do not always generate the same type):**
   - **Duration Comparison:** *"Which event lasted longer?"*
   - **Chronological Order:** *"Which event happened earlier or later?"*
   - **Time Gap Analysis:** *"How much time passed between these events?"*
   - **Event Evolution Over Time:** *"How did the situation change between these two periods?"*
   - **Frequency Comparison:** *"Which event happened more frequently?"*
   - **Impact of Time:** *"How did external factors change between the two events?"*
2. **You must rotate between these categories. Do not generate the same type of question repeatedly.**
3. **Avoid using explicit dates (years, months, days) in the question.**
   - ❌ *Yanlış:* “2010 yılında gerçekleşen X olayı ile 2012’de yaşanan Y olayı...?”
   - ✅ *Doğru:* “X olayının yaşandığı dönem ile Y olayının yaşandığı süreç...?”
   - **Use event descriptions instead of numerical dates.**
4. **Avoid vague references** such as:
   - ❌ *"Her iki haberde de geçen..."*
   - ❌ *"İki haberde de bahsedilen..."*
   - ❌ *"Bu iki makalede..."*
5. **Instead, explicitly refer to the events, topics, or entities from each article.**
   ✅ **Correct format examples:**
   - *"X olayının yaşandığı süreç, Y olayına kıyasla daha uzun mu sürmüştür?"* (**Duration Comparison**)
   - *"İlk olarak X olayının yaşandığı süreç mi başlamış, yoksa Y olayı mı daha erken gerçekleşmiştir?"* (**Chronological Order**)
   - *"X olayının yaşandığı dönem ile Y olayının gerçekleştiği dönem arasında ne kadar zaman farkı bulunmaktadır?"* (**Time Gap Analysis**)
   - *"X olayının yaşandığı süreçte alınan önlemler, Y olayının yaşandığı süreçte nasıl değişmiştir?"* (**Event Evolution Over Time**)
   - *"X olayının yaşandığı süreçte benzer olaylar ne kadar sıklıkla gerçekleşmiştir? Y olayına kıyasla daha mı sık meydana gelmiştir?"* (**Frequency Comparison**)
   - *"X olayının yaşandığı dönem ile Y olayının yaşandığı dönem arasında hangi faktörler değişmiş ve olayların gelişimini nasıl etkilemiştir?"* (**Impact of Time**)
6. **Your question must be written in Turkish.**
7. Be as creative as possible while generating the question, you don't have to stick to the examples above.

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

**Format your output as follows:**
Question:
"""
