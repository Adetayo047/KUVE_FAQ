# KUVE FAQ Chatbot

This project is an AI-powered FAQ chatbot for the KUVE Marketplace, designed to answer common questions about the platform for buyers, sellers, and logistics partners.

## Features
- Answers frequently asked questions about KUVE Marketplace
- Covers topics for buyers, sellers, and logistics partners
- Provides information on AI-powered shopping, escrow payments, KUVE Express, KUVE Lend, and more
- Uses a knowledge base from `getkuve_faq.txt`

## Project Structure
- `getkuve_faq.txt`: Main FAQ knowledge base
- `app.py`, `main.py`: Application entry points (chatbot logic)
- `vector.py`: Vector store or embedding logic
- `requirements.txt`: Python dependencies

## Getting Started
1. **Clone the repository**
      ```bash
   https://github.com/Adetayo047/KUVE_FAQ.git
   ```
2. **Set up a Python virtual environment** (optional but recommended):
   ```bash
   python3 -m venv kevenv
   source kevenv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the chatbot:**
   ```bash
   python app.py
   ```
   or
   ```bash
   python main.py
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   This will launch the chatbot in your browser using Streamlit's web interface.

## FAQ Topics Covered
- General questions about KUVE
- Buyer features (AI shopping, escrow, support)
- Seller features (storefronts, POS, lending)
- Logistics partner features (KUVE Express, API integration)
- Getting started and technical questions

## Limitations
- The chatbot relies on Ollama for local LLM inference. Ollama must be installed and running on your machine for the chatbot to function.
- Ollama currently only supports certain models and may require additional system resources.
- Internet access may be required for some features or model downloads.

## Customization
- To update or expand the FAQ, edit `getkuve_faq.txt`.
- For advanced logic, modify `app.py` or `main.py`.

## License
This project is for demonstration and internal use. Please contact the author for licensing details.
