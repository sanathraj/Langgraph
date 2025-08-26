# DHS 2025: Agentic RAG & Adaptive Retrieval

This repository contains advanced Retrieval-Augmented Generation (RAG) workflows and agentic architectures using LangChain, LangGraph, and OpenAI models. The notebooks demonstrate how to build adaptive, agentic systems for document retrieval, grading, and answer generation, with support for web search and vector database integration.

## Features
- **Adaptive RAG Pipeline**: Dynamically routes queries to vectorstore or web search based on topic relevance.
- **Document Retrieval & Grading**: Uses LLMs to assess document relevance and filter results.
- **Answer Generation**: Generates answers grounded in retrieved documents, with hallucination and answer grading.
- **Question Rewriting**: Improves user queries for better retrieval performance.
- **Graph-Based Workflow**: Utilizes LangGraph for flexible, stateful workflow orchestration.
- **Web Search Integration**: Supports external search via Tavily API.

## Folder Structure
- `Agentic RAG.ipynb`, `5_Agentic_Rag.ipynb`: Main notebooks demonstrating the agentic RAG pipeline.
- Other notebooks: Experiments and demos for async processing, human-in-the-loop, observability, and more.
- `requirements.txt`: List of required Python packages.

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DHS-2025.git
   cd DHS-2025
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with API keys (OpenAI, Tavily, etc):
   ```
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

## Usage
- Open the notebooks in Jupyter or VS Code.
- Run cells to load documents, build vectorstores, and execute the agentic RAG workflow.
- Modify the input question to test different retrieval and generation scenarios.

## Technologies Used
- LangChain
- LangGraph
- OpenAI API
- FAISS
- Tavily Search
- Python, Jupyter

## License
MIT License

## Author
Sanat (and contributors)
