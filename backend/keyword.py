import re

def extract_keywords_from_text(text, keyword, context_window=1, related_keywords=None):
    if related_keywords is None:
        related_keywords = [keyword]  # Default to the provided keyword if no related terms are given

    # Split text into sentences using regex that identifies punctuation marks like . ! ?
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # List to store sentences containing the keyword or related terms
    relevant_sentences = []
    seen_sentences = set()  # Set to track duplicates
    
    # Loop over the sentences
    for i, sentence in enumerate(sentences):
        # Check if any related keyword is in the sentence (case insensitive)
        if any(keyword.lower() in sentence.lower() for keyword in related_keywords):
            
            # Normalize sentence (lowercase and remove punctuation) for duplicate check
            normalized_sentence = re.sub(r'[^\w\s]', '', sentence.lower())
            
            # Only add sentence if it has not been added before (i.e., no duplicates)
            if normalized_sentence not in seen_sentences:
                relevant_sentences.append(sentence)
                seen_sentences.add(normalized_sentence)
                
                # Optionally, capture context around the sentence
                # Capture previous sentences within the window
                for j in range(i - 1, max(i - context_window, -1), -1):
                    context_sentence = sentences[j]
                    normalized_context_sentence = re.sub(r'[^\w\s]', '', context_sentence.lower())
                    
                    if normalized_context_sentence not in seen_sentences:
                        relevant_sentences.insert(0, context_sentence)  # Add to the beginning (preceding context)
                        seen_sentences.add(normalized_context_sentence)

                # Capture following sentences within the window
                for j in range(i + 1, min(i + context_window + 1, len(sentences))):
                    context_sentence = sentences[j]
                    normalized_context_sentence = re.sub(r'[^\w\s]', '', context_sentence.lower())
                    
                    if normalized_context_sentence not in seen_sentences:
                        relevant_sentences.append(context_sentence)  # Add to the end (following context)
                        seen_sentences.add(normalized_context_sentence)
    
    return relevant_sentences

