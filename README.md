# Keyword_Focused_AI_Summarization
Developed an intelligent AI summarization system that extracts content based on user-specified keywords from PDFs and web articles, streamlining the information retrieval process.

This is an open-source AI-driven summarization tool designed to autonomously select between summarization and extraction tasks based on user-defined keywords. The system uses the Mistral-7B model (via Hugging Face) for text generation and LangChain’s agent framework for decision-making. The tool is designed to work with both PDFs and web articles, providing flexible content extraction and summarization capabilities.

The project leverages optimization techniques to reduce inference costs, achieving an approximate 30% cost reduction, while maintaining high performance and accuracy. The tool has been successfully tested on over 10 real-world documents, including PDFs and web articles.

## Features
- **Keyword-Based Extraction**: Extracts content relevant to user-defined keywords from text sources (PDFs and web articles).
- **Autonomous Task Selection**: Decides whether to perform summarization or content extraction based on the input and user’s needs.
- **Cost Optimization**: Reduced inference costs by ~30% using optimized LLM (Large Language Model) selection.
- **Real-World Applicability**: Successfully tested on 10+ real-world PDFs and web articles.

## Requirements
To run the project locally, ensure you have the following:
- Python 3.8+
- `pip`
- Hugging Face API token (for accessing Mistral-7B model) - free to create one!

How It Works
1. Extract Text from Source
The tool allows users to either upload a PDF or provide a URL. The system will extract the relevant text from these sources.

2. Keyword-Based Filtering
The user provides a keyword, and the tool will filter out relevant paragraphs or sections from the extracted text that match the keyword.

3. Summarization or Extraction
Once the content is filtered, users can choose whether they want to summarize the extracted content or simply extract the relevant text.

4. Agentic Decision-Making
The LangChain agent evaluates the text and autonomously chooses between summarization and extraction based on the user input, optimizing the process for relevance and efficiency.
  

