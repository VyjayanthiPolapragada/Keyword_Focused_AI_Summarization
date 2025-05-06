from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


# Initialize the Mistral-7B model
model_name = "mistralai/Mistral-7B"

# Load tokenizer and model with Hugging Face token
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B", token="paste your token here")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B", token="paste your token here")


# Summarization function
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text):
    try:
        # Summarize the provided text
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Summary not available."
