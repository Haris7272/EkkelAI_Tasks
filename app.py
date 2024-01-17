from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m")

@app.route('/api/completion', methods=['POST'])
def completion():
    try:
        data = request.get_json()
        input_text = data['text']

        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        with torch.no_grad():
            output_ids = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2)

        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        response = {
            'input_text': input_text,
            'output_text': output_text
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
