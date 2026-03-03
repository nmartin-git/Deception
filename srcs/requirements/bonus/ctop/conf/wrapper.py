from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Docker Monitor</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body { background: #1e1e1e; color: #00ff00; font-family: monospace; padding: 20px; }
            pre { background: #2d2d2d; padding: 20px; border: 1px solid #00ff00; }
        </style>
    </head>
    <body>
        <h1>🐳 Docker Containers</h1>
        <pre>{}</pre>
        <p>Auto-refresh every 5 seconds</p>
    </body>
    </html>
    '''.format(get_containers())

def get_containers():
    try:
        result = subprocess.run(
            ['docker', 'ps', '--format', 'table {{.Names}}\t{{.Status}}\t{{.Image}}'],
            capture_output=True,
            text=True
        )
        return result.stdout
    except:
        return "Error getting containers"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)