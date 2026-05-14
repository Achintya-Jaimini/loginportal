from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = '2444666668888888'  

users = {
    "admin": "123",
    "ajaimini": "abc",
    "user": "123456"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] in users and users[request.form['username']] == request.form['password']:
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    elif 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        flash('You must be logged in to view the dashboard.', 'warning')
        return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


app.run()