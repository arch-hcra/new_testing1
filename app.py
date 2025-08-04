from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

users = {
    "admin": {
        "admin1": "12345",
        "admin2": "12345",
        "admin3": "12345",
    },
    "tech": {
        "tech1": "12345",
        "tech2": "12345",
        "tech3": "12345",
    },
    "user": {
        "user1": "12345",
        "user2": "12345",
        "user3": "12345",
    }
}

LOG_FILE = "login.log"

def log_login(username, group, success):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "SUCCESS" if success else "FAIL"
    with open(LOG_FILE, "a") as f:
        f.write(f"{now} - {username} - {group} - {status}\n")


HTML_TEMPLATE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Login</title>
</head>
<body>
  <h2>Enter in system</h2>
  <form method="post">
    <label>Login: <input type="text" name="username" required></label><br><br>
    <label>Password: <input type="password" name="password" required></label><br><br>
    <button type="submit">Enter</button>
  </form>

  {% if result %}
    <p><strong>{{ result }}</strong></p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        for group_name, group_users in users.items():
            if username in group_users and group_users[username] == password:
                log_login(username, group_name, True)
                result = f"Login Yes. Group: {group_name}"
                break
        else:
            log_login(username, "unknown", False)
            result = "Login No"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

