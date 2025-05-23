from flask import Blueprint, request, jsonify
from utils.summarizer import summarize_with_gpt, summarize_with_gemini, chat_with_gemini
from utils.parser import extract_text_from_pdf

summarize_bp = Blueprint('summarize', __name__)

@summarize_bp.route('/pdf', methods=['POST'])
def summarize_pdf():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    text = extract_text_from_pdf(file)
    summary = summarize_with_gemini(text)
    return jsonify({'summary': summary, 'pdf_text': text})

@summarize_bp.route('/chat', methods=['POST'])
def chat():
    question = request.json['question']
    pdf_text = request.json['pdf_text']
    summary = chat_with_gemini(pdf_text, question)
    return jsonify({'summary': summary})