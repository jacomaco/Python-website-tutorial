from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/homer')
def homer():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                text-align: center;
                background-color: #f0f0f0;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 20px;
            }
            main {
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            footer {
                background-color: #333;
                color: white;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Homepage</h1>
        </header>
        <main>
            <h2>About This Page</h2>
            <p>This is a simple homepage created with HTML and CSS. Feel free to explore and modify it to suit your needs!</p>
            <p><a href="#contact">Contact Us</a></p>
        </main>
        <footer>
            <p>© 2025 My Homepage. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """