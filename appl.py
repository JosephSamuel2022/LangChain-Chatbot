import subprocess
from flask_cors import CORS
from flask import Flask, request, render_template
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)


@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    question = request.json['question']

    # Call the chatgpt.py script and capture the output
    cmd = ['python', 'chatgpt.py', question]
    output = subprocess.check_output(cmd, universal_newlines=True).strip()

    if output == "I don't know.":
        output = "Kindly inquire about relevant topics concerning myself."

    return render_template('result.html', answer=output)


if __name__ == '__main__':
    app.run(port=5000)
