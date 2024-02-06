from flask import Flask, request, render_template

# Import your generativeAI script
import google.generativeai as g

app = Flask(__name__)

# Configure generativeAI with your API key
g.configure(api_key="AIzaSyA3ObDZcifPFy-QJojBhqdYAvSVUDcJnKU")  # key looks like this



# Your generativeAI script
def generate_response(prompt):
    response = g.GenerativeModel(model_name="gemini-pro").generate_content([prompt]).text
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    prompt = request.form['query']
    response = generate_response(prompt)
    return response

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
