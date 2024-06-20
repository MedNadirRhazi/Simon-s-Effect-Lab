from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import random, time

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

if __name__ == '__main__':
    app.run(debug=True)

