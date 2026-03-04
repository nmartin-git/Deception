from flask import Flask
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Monitor</title>
    <style>
        body {
            background: #1e1e1e;
            color: #00ff00;
            font-family: monospace;
            padding: 20px;
            margin: 0;
        }
        h1 {
            text-align: center;
            color: #00ff00;
            margin-bottom: 20px;
        }
        .controls {
            text-align: center;
            margin-bottom: 20px;
        }
        .btn {
            background: #00ff00;
            color: #1e1e1e;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 5px;
            font-family: monospace;
        }
        .btn:hover {
            background: #00cc00;
        }
        .btn:active {
            background: #009900;
        }
        .status {
            display: inline-block;
            margin-left: 20px;
            font-size: 16px;
        }
        .status.active {
            color: #00ff00;
        }
        .status.paused {
            color: #ff9900;
        }
        .section {
            background: #2d2d2d;
            border: 1px solid #00ff00;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .section-title {
            color: #00ff00;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #00ff00;
        }
        th {
            background: #0d0d0d;
            color: #00ff00;
        }
        tr:hover {
            background: #3d3d3d;
        }
        .running {
            color: #00ff00;
        }
        .exited {
            color: #ff0000;
        }
        .logs {
            background: #0d0d0d;
            border: 1px solid #00ff00;
            padding: 10px;
            height: 500px;
            overflow-y: auto;
            font-size: 12px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .log-container {
            margin-bottom: 15px;
        }
        .log-header {
            color: #00ff00;
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 5px;
            padding: 5px;
            background: #0d0d0d;
        }
        .log-line {
            margin: 2px 0;
            padding-left: 10px;
            color: #cccccc;
        }
        .refresh-info {
            text-align: center;
            margin-top: 10px;
            color: #00ff00;
            font-size: 14px;
        }
    </style>
    <script>
        let autoRefresh = true;
        let refreshInterval;
        
        function toggleRefresh() {
            autoRefresh = !autoRefresh;
            const btn = document.getElementById('toggle-btn');
            const status = document.getElementById('status');
            
            if (autoRefresh) {
                btn.textContent = '⏸ Pause Auto-Refresh';
                status.textContent = '🟢 Active';
                status.className = 'status active';
                startRefresh();
            } else {
                btn.textContent = '▶ Resume Auto-Refresh';
                status.textContent = '⏸ Paused';
                status.className = 'status paused';
                stopRefresh();
            }
        }
        
        function startRefresh() {
            refreshInterval = setInterval(updatePage, 3000);
        }
        
        function stopRefresh() {
            clearInterval(refreshInterval);
        }
        
        function updatePage() {
            if (!autoRefresh) return;
            
            fetch('/data')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('content').innerHTML = data;
                    const logsDiv = document.getElementById('logs-section');
                    if (logsDiv) {
                        logsDiv.scrollTop = logsDiv.scrollHeight;
                    }
                });
        }
        
        function manualRefresh() {
            updatePage();
        }
        
        window.onload = function() {
            updatePage();
            startRefresh();
        };
    </script>
</head>
<body>
    <h1>🐳 Docker Containers Monitor</h1>
    
    <div class="controls">
        <button id="toggle-btn" class="btn" onclick="toggleRefresh()">⏸ Pause Auto-Refresh</button>
        <button class="btn" onclick="manualRefresh()">🔄 Refresh Now</button>
        <span id="status" class="status active">🟢 Active</span>
    </div>
    
    <div id="content">
        <div class="section">
            <div class="section-title">Loading...</div>
        </div>
    </div>
    
    <div class="refresh-info">
        ⏱ Auto-refresh every 3 seconds (when active)
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML

@app.route('/data')
def get_data():
    containers_table = get_containers_table()
    logs_section = get_all_logs()
    
    html = """
    <div class="section">
        <div class="section-title">📊 Running Containers</div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Status</th>
                    <th>Image</th>
                    <th>Ports</th>
                </tr>
            </thead>
            <tbody>
                """ + containers_table + """
            </tbody>
        </table>
    </div>
    
    <div class="section">
        <div class="section-title">📝 Live Logs (last 15 lines per container)</div>
        <div id="logs-section" class="logs">
            """ + logs_section + """
        </div>
    </div>
    """
    
    return html

def get_containers_table():
    try:
        result = subprocess.run(
            ['docker', 'ps', '-a', '--format', '{{.Names}}|{{.Status}}|{{.Image}}|{{.Ports}}'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        rows = ""
        for line in result.stdout.strip().split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) >= 4:
                    name = parts[0]
                    status = parts[1]
                    image = parts[2]
                    ports = parts[3] if parts[3] else '-'
                    
                    status_class = 'running' if 'Up' in status else 'exited'
                    
                    rows += '<tr>'
                    rows += '<td>' + name + '</td>'
                    rows += '<td class="' + status_class + '">' + status + '</td>'
                    rows += '<td>' + image + '</td>'
                    rows += '<td>' + ports + '</td>'
                    rows += '</tr>'
        
        if not rows:
            rows = '<tr><td colspan="4">No containers found</td></tr>'
        
        return rows
    except Exception as e:
        return '<tr><td colspan="4">Error: ' + str(e) + '</td></tr>'

def get_all_logs():
    try:
        result = subprocess.run(
            ['docker', 'ps', '--format', '{{.Names}}'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        containers = [c.strip() for c in result.stdout.strip().split('\n') if c.strip()]
        
        logs_html = ""
        
        for container in containers:
            log_result = subprocess.run(
                ['docker', 'logs', '--tail', '15', container],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            logs_html += '<div class="log-container">'
            logs_html += '<div class="log-header">▶ ' + container + '</div>'
            
            logs = log_result.stdout + log_result.stderr
            if logs.strip():
                for line in logs.strip().split('\n')[-15:]:
                    if line.strip():
                        logs_html += '<div class="log-line">' + line + '</div>'
            else:
                logs_html += '<div class="log-line" style="color: #888;">No recent logs</div>'
            
            logs_html += '</div>'
        
        if not logs_html:
            logs_html = '<div style="color: #888;">No running containers</div>'
        
        return logs_html
    except Exception as e:
        return '<div style="color: red;">Error: ' + str(e) + '</div>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)