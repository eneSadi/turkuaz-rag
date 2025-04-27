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
null_question_template = f"""
You will be given 2 news articles that are contextually similar but not identical.  
Your task is to generate a **Null Question**.

---

### 🧠 What is a Null Question?

A Null Question is a question that:
- Appears contextually relevant to the topic of the articles,
- Can reasonably be asked **based on the theme or key entities of both articles**,  
- But **CANNOT be answered by reading the content of either article or both together.**

It should **not** be a completely unrelated or off-topic question.  
Instead, it should sound like a valid inference, comparison, or temporal question—**but with missing key information**.

---

### ✅ Requirements:

1. The question must sound **contextually valid** based on the two articles.
2. The **answer must not be present in either article**.
3. The question should **clearly reference both articles**:
   - Each article should be **explicitly and specifically referred to**, not grouped with vague language.
   - ❌ Avoid vague expressions such as:
     - "Her iki haberde de geçen..."
     - "İki haberde de bahsedilen..."
     - "Bu iki makalede..."
   - ✅ Instead, use concrete entities or facts from both articles in the question, such as:
     - “İlk haberde söz edilen X kararı ile ikinci haberde açıklanan Y uygulaması...”

4. The question should be written in **clear and fluent Turkish**.
5. The reader should **think** the answer may exist, but ultimately realize the necessary information is missing.
6. ❌ **Do not write open-ended, opinion-based, or vague questions.**
   - The question should be **specific and factual**, where the **lack of a concrete fact** makes it unanswerable—not interpretation.
   - ✅ Example: “Hangi yıl?”, “Hangi ülke?”, “Kaç kişi?”, “Ne zaman başladı?”, “Kim tarafından?” gibi **somut bilgi eksikliği içeren** net sorular yazılmalı.

---

### 🔍 Output Format:

Question Type: Null  
Why it's null: <Explain which key info is missing from the articles that makes the question unanswerable.>  
Question: <your null question in Turkish, with specific references to both articles>

---

### ✅ Example:

**News 1 summary:** İzmir’de deprem sonrası 7 bina yıkıldı, 100'den fazla kişi kurtarıldı.  
**News 2 summary:** AFAD, Ege Denizi açıklarında gerçekleşen deprem sonrası 1200 personelin görevde olduğunu açıkladı.  

Question Type: Null  
Why it's null: Neither article provides any information about the estimated financial damage caused by the earthquake.  
Question: İzmir’de 7 binanın yıkıldığından bahsedilen ilk haberdeki zarar ile, AFAD’ın 1200 personel görevlendirdiğini açıkladığı ikinci haberdeki toplam ekonomik kayıp karşılaştırıldığında, hangi bölge daha büyük bir maddi hasar yaşamıştır?

---

Now, analyze the two articles below and generate a **Null Question** as instructed.

---

News 1:  
Title: {sample['title']}  
Date: {sample['date']}  
Summary: {sample['summary']}  
Text: {sample['text']}

News 2:  
Title: {sample['title']}  
Date: {sample['date']}  
Summary: {sample['summary']}  
Text: {sample['text']}

---

Your output should follow this format:

Question Type: Null  
Why it's null: <...>  
Question: <...>
"""