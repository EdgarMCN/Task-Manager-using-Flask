import hmac
import werkzeug.security
werkzeug.security.safe_str_cmp = hmac.compare_digest

from todo_project import app

if __name__ == '__main__':
    app.run(debug=True)
