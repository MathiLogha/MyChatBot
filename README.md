**# MyChatBot**
Created a chatbot with database connection and hosting in streamlit - Chatbot using Streamlit & LangChain
Visit hosted chatbot = **https://mychatbot-mathilogha.streamlit.app/**
![image](https://github.com/user-attachments/assets/1d79938b-733e-4480-b376-413e3a1cd712)

This repository contains a chatbot built using **Streamlit** for the frontend and **LangChain** for natural language processing (NLP). The chatbot leverages an **LLM-based pipeline** to generate responses dynamically.  

## **🚀 Features**  
- ✅ **Interactive UI:** Built using Streamlit for a smooth user experience.  
- ✅ **NLP Processing:** Uses LangChain to process queries and retrieve responses.  
- ✅ **LLM-Powered:** A lightweight, space-efficient open-source model for generating responses.  
- ✅ **Database Integration:** Queries an SQLite database for employee-related information.  
- ✅ **Customizable Pipeline:** The LLM pipeline can be easily modified to include more functionalities.  

---

## **🛠️ How the Assistant Works**  
1. **User Input:** The user enters a query into the chatbot interface.  
2. **LangChain Processing:**  
   - The input is processed using a conversational pipeline created with LangChain.  
   - The query is passed to the LLM for response generation.  
   - The response is formatted for better readability.  
3. **Database Querying:** If necessary, the chatbot retrieves information from an **SQLite database**.  
4. **Response Generation:** The assistant provides a structured, user-friendly response.  
5. **Chat History:** Maintains a session-based conversation history for context-aware responses.  

---

## **🖥️ Steps to Run the Project Locally**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/MathiLogha/MyChatBot.git
cd your-repo-name
```
### **2️⃣ Set Up a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate      # On Windows
```
### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```
### **4️⃣ Run the Application**  
```bash
streamlit run app.py
```
This will start a local server, and you can access the chatbot at http://localhost:8501 in your browser.
## **📌 Folder Structure**  
📂 your-repo-name/
│-- 📂 utils/            # Helper functions (LangChain pipeline, DB queries, etc.)
│-- 📂 data/             # SQLite database files
│-- app.py               # Main Streamlit app
│-- requirements.txt     # Python dependencies
│-- README.md            # Project documentation
│-- chatbot.png          # UI logo/image

---

## **⚠️ Known Limitations & Suggestions for Improvement**  

### **Limitations**  
- ❌ **Limited Storage:** Uses a lightweight model due to storage constraints.  
- ❌ **External APIs:** The chatbot works on advanced cloud-based LLMs.  
- ❌ **Basic Query Handling:** Currently supports **employee data lookup**, but complex NLP tasks may require fine-tuning.  

### **Future Enhancements**  
- 🚀 **Multi-Model Support:** Allow switching between multiple LLMs.  
- 🚀 **Fine-tuning:** Optimize the model for better response accuracy.  
- 🚀 **User Authentication:** Add login support for personalized responses.  
- 🚀 **Vector Database:** Use **FAISS** or **ChromaDB** for improved search capabilities.  

---

## **🤝 Contributing**  
Feel free to **fork** this repo and submit **pull requests**! Any improvements or suggestions are welcome.  

---

## **📧 Contact**  
For any questions or suggestions, reach out via:  
📩 **Email:** your-email@example.com  
🐦 **Twitter:** [@yourusername](https://twitter.com/yourusername)  
🔗 **GitHub:** [your-username](https://github.com/your-username)  

