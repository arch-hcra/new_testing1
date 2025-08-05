from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "host": "x",
    "port":   x,
    "database": "x",
    "user": "x",
    "password": "x"
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def check_user(username, password):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT group_name FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            result = cur.fetchone()
            return result[0] if result else None
    finally:
        conn.close()

def log_login_db(username, group, success):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO login_attempts (username, group_name, success)
                VALUES (%s, %s, %s)
                """,
                (username, group, success)
            )
            conn.commit()
    finally:
        conn.close()

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Login</title>
</head>
<body>
  <h2>Enter the system</h2>
  <form method="post">
    <label>Username: <input type="text" name="username" required></label><br><br>
    <label>Password: <input type="password" name="password" required></label><br><br>
    <button type="submit">Login</button>
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

        group = check_user(username, password)
        if group:
            log_login_db(username, group, True)
            result = f"Login Yes. Group: {group}"
        else:
            log_login_db(username, "unknown", False)
            result = "Login No"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
