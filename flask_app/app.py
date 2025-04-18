from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user_info', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age_str = request.form.get('age', '').strip()
        
        # Error handling for empty or invalid inputs
        if not name:
            flash('Please enter your name.')
            return redirect(url_for('user_info'))
        
        try:
            age = int(age_str)
            if age <= 0 or age > 120:
                flash('Please enter a valid age between 1 and 120.')
                return redirect(url_for('user_info'))
        except ValueError:
            flash('Please enter a valid numeric age.')
            return redirect(url_for('user_info'))
        
        greeting = f"Hello, {name}! You are {age} years old."
        return render_template('greeting.html', greeting=greeting)
    
    return render_template('user_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)