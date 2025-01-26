from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

model_name = os.getenv("MODEL_NAME", "mistralai/Mistral-7B")
faq_dataset_path = os.getenv("FAQ_DATASET", "dataset/faq.csv")

app = Flask(__name__)

# Load the Mistral 7B model and tokenizer
model_name = "mistralai/Mistral-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load FAQ dataset
faq_df = pd.read_csv("dataset/faq.csv")

# Helper function to find the best matching FAQ
def get_faq_response(user_question):
    for _, row in faq_df.iterrows():
        if row["question"].lower() in user_question.lower():
            return row["answer"]
    return "I'm sorry, I couldn't find an answer to that question. Please contact the college directly."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "")
    # Search for FAQ response
    faq_response = get_faq_response(user_input)
    if faq_response != "I'm sorry, I couldn't find an answer to that question. Please contact the college directly.":
        return jsonify({"response": faq_response})
    
    # Use Mistral 7B model if no FAQ matches
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_new_tokens=100, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
