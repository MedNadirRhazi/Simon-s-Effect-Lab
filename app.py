from flask import Flask, render_template, jsonify, request, session, redirect, url_for, request, send_file
import random, time
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'une_cle_secrete_tres_complexe'

@app.route('/')
def index():
    session.clear() 
    session['results'] = []
    return render_template('index.html')


@app.route('/results')
def view_results():
    return render_template('results.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/get_trials')
def get_trials():
    trials = []
    for _ in range(100):
        position = random.choice(['left', 'right'])
        correct_key = 'A' if position == 'left' else 'L'
        trials.append({'position': position, 'correct_key': correct_key})
    return jsonify(trials=trials)

@app.route('/download-excel', methods=['POST'])
def download_excel():
    data = request.json['results']
    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="results.xlsx")

if __name__ == '__main__':
    app.run(debug=True)

