from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def site2():
    return render_template('site2.html')

@app.route('/thank_you', methods=['POST'])
def thank_you():
    message = request.form.get('message')
    return f"Thank you for your feedback, dear PROFESSOR: {message}"

if __name__ == '__main__':
    app.run(debug=True)
