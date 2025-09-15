from transformers import pipeline

# Use a small model (lighter + faster)
summarizer = pipeline("summarization", model="t5-small")

text = "Hello how are you. Hope you are doing good."
words = text.split()

# Summarize with max_length relative to input
summary = summarizer(text, max_length=len(words)//2, min_length=5, do_sample=False)

print(summary[0]['summary_text'])
