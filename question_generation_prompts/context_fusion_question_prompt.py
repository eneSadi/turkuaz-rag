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



context_fusion_question_template = f"""
You will be given 2 news articles that cover related topics but differ in some details, perspectives, or contexts.  
Your task is to create a **Contextual Fusion Question**.

This type of question requires **understanding and combining unique key information from both articles**. The question should **not** be answerable by reading just one of the articles.  
Instead, it should be based on insights gained by **fusing contextual information from both sources**.

---

### 🔍 Step-by-step Instructions:

1. **Extract one unique and key piece of factual information from each article.**  
   These should not be generic details, but core facts that are central to the articles.

2. **Connect the extracted facts** meaningfully. This connection could be:
   - Causal (one leads to another),
   - Comparative (one is larger, stronger, longer, etc.),
   - Contrastive (opposing views or outcomes),
   - Complementary (different parts of a bigger picture).

3. **Generate a question** that:
   - **Cannot be answered by looking at only one article,**
   - **Requires synthesis of both extracted key facts,**
   - **Is specific, factual, and clearly worded in Turkish,**
   - **Avoids generic or vague references** (see below).

---

### ❌ Avoid vague references such as:
- "Her iki haberde de geçen..."
- "İki haberde de bahsedilen..."
- "Bu iki makalede..."

Instead, refer to the **distinct topics, events, or entities** described in each article. Be **explicit** and **concrete**.

---

### ✅ Example Format:

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

Your output should follow this structure:

Key Fact 1 (from News 1): <write the extracted unique information from news 1>
Key Fact 2 (from News 2): <write the extracted unique information from news 2>
Question: <your contextual fusion question in Turkish>

---

### 🧠 Example (fictional content):

Key Fact 1 (from News 1): İstanbul'daki barajların doluluk oranı %30 seviyesine geriledi.  
Key Fact 2 (from News 2): Meteoroloji, gelecek haftalarda beklenen yoğun yağışların barajları doldurabileceğini bildirdi.  
Question: Baraj doluluk oranlarının kritik seviyelere indiği İstanbul'da, meteorolojinin öngördüğü yoğun yağışlar su krizini ne ölçüde hafifletebilir?

---

Now, use the structure above to analyze the following news articles and generate your output.
"""