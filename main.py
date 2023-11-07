from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
import os

email = os.environ['YOUR_EMAIL']
password = os.environ['YOUR_APP_PASSWORD']

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def send_email(name, recipient_email, subject, message):
    # Set up the server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    # Log in to your email account
    server.login(email, password)

    # Create the email message
    msg = MIMEText(f'Name: {name}\nEmail: {recipient_email}\nSubject: {subject}\nMessage: {message}')
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'New Contact Form Submission'

    # Send the email
    server.send_message(msg)

    # Quit the server
    server.quit()

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = 'success' in request.args
    if request.method == 'POST':
        # Get form data from the request object
        name = request.form['your-name']
        recipient_email = request.form['your-email']
        subject = request.form['your-subject']
        message = request.form['your-message']

        # Do something with the form data, e.g. send an email or save to a database
        # Send email with form data
        send_email(name, recipient_email, subject, message)
        # Redirect to the contact page with a success query parameter
        return redirect(url_for('contact', success=True))
    return render_template('contact.html', success=success)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/about_myself')
def about_myself():
    return render_template('about_myself.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=False)