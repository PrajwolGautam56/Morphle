from flask import Flask, render_template_string
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Prajwol Gautam" 
    username = 'PrajwolGautam56'
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    top_output = subprocess.check_output(['ps', 'aux']).decode('utf-8')


    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTop Output</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            pre {{ white-space: pre-wrap; }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)  
