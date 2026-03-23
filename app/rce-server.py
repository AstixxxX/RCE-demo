#!/usr/bin/env python3
import subprocess
import sys
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Authentication Form RCE</h2>
    {% if error %}
    <p style="color:red">{{ error }}</p>
    {% endif %}
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # RCE-vuln -> user input don't shielded!!!
        cmd = f"grep {username} /etc/passwd || echo 'User not found'"

        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            if 'User not found' in result:
                return render_template_string(HTML_FORM, error="Invalid credentials")
            return f"<h2>Welcome!</h2><pre>{result}</pre>"
        except subprocess.CalledProcessError as e:
            return render_template_string(HTML_FORM, error=f"Error: {e.output}")
    
    return render_template_string(HTML_FORM, error=None)

if __name__ == '__main__':
    host = "localhost"
    port = 8080

    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = sys.argv[2]

    app.run(host=host, port=port)