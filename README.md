🤖 Local FAQ Support Bot: BFSI Intelligence Engine
Secure, Offline, and Private AI for Banking, Financial Services, and Insurance.

📌 Project Overview
The Local FAQ Support Bot is a production-ready implementation of a Retrieval-Augmented Generation (RAG) pipeline. Designed specifically for the highly regulated BFSI sector, this tool allows institutions to query complex policy documents and FAQs locally.
The Problem: Financial data is too sensitive for cloud-based AI (like ChatGPT).
The Solution: This bot runs 100% offline, ensuring that customer data and internal bank policies never leave the local environment.

________________________________________

🏗️ System Architecture

The project follows a modular RAG workflow to ensure high accuracy and zero hallucinations:
1.	Document Ingestion: Loads BFSI datasets (PDFs, Text, CSVs).
2.	Chunking Strategy: Uses RecursiveCharacterTextSplitter with a 1000-character window and 200-character overlap to preserve financial context.
3.	Vector Embedding: Converts text into mathematical vectors using the nomic-embed-text model.
4.	Vector Storage: Saves embeddings into ChromaDB for persistent, high-speed semantic search.
5.	Contextual Retrieval: Performs a similarity search to find the most relevant policy clauses.
6.	Response Generation: Uses a Small Language Model (SLM) to generate a professional answer based only on the retrieved context.

________________________________________

🛠️ Technical Stack
•	Core Language: Python 3.10+
•	Orchestration: LangChain (Managing the RAG chain and prompt templates)
•	Local LLM Engine: Ollama (Running Phi-3 / Llama-3 locally)
•	Vector Database: ChromaDB (High-performance vector storage)
•	Embeddings: Nomic-Embed-Text (Optimized for local retrieval)
•	Frontend UI: Streamlit (Clean, interactive web interface)

________________________________________


🚀 Installation & Setup

1. Prerequisites
•	Ensure Ollama is installed.
•	Hardware: 16GB RAM recommended for smooth local inference.



2. Environment Setup
 <img width="940" height="171" alt="image" src="https://github.com/user-attachments/assets/524b3ad4-01f0-4afb-9301-ea134aca48aa" />

 


3. Data based for SLM
<img width="940" height="565" alt="image" src="https://github.com/user-attachments/assets/afeca580-71e8-4caa-956d-e4fa80d68c21" />

 



4. Model Preparation
 Run the following commands in your terminal to pull the necessary local models:
 <img width="940" height="575" alt="image" src="https://github.com/user-attachments/assets/75ee6769-a22a-4293-a226-3fb787a9d6a8" />
 <img width="940" height="555" alt="image" src="https://github.com/user-attachments/assets/15947ff8-9166-4d35-82ad-e32db773bd55" />
<img width="940" height="194" alt="image" src="https://github.com/user-attachments/assets/c0132ef6-5d7d-4e51-9d7e-1e058fe0805b" />


 
 

5. Running the Bot
<img width="940" height="170" alt="image" src="https://github.com/user-attachments/assets/714c1a1b-41bb-4dba-b114-8a4941a1c5c2" />
<img width="940" height="147" alt="image" src="https://github.com/user-attachments/assets/1b53ab15-fe1c-4f29-9e45-457a0b3609e0" />


 
 

6.	 Output of the project
   <img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/b46f1760-45cd-47c4-b5ea-55bedbdbf09b" />
   <img width="940" height="362" alt="image" src="https://github.com/user-attachments/assets/6fa2a7c9-ff87-4810-95f8-e99be819997c" />


 
 

🛡️ Key BFSI Features
•	Data Sovereignty: No API keys required. No cloud dependencies.
•	Hallucination Guardrails: The model is strictly instructed to say "I don't know" if the answer isn't in the provided FAQ.
•	Source Transparency: Every answer includes the specific document chunk used as a reference.
•	Quantized Efficiency: Optimized to run on laptops (like the Dell Inspiron 14) without needing a server-grade GPU.

📊 Performance Benchmarks
•	Indexing Speed: ~2-5 seconds per 100 pages.
•	Query Latency: <3 seconds for full response generation on 16GB RAM.
•	Accuracy: 95%+ retrieval success on standardized banking FAQs.





