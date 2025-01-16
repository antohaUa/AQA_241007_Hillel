from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, template_folder='templates')

# Define allowed user-agent and cookie values
ALLOWED_USER_AGENT = "MyCustomAgent/1.0"
ALLOWED_COOKIE_VALUE = "12345"


@app.route('/')
def home():
    # Retrieve user-agent and cookies
    user_agent = request.headers.get('User-Agent')
    visit_id = request.cookies.get('visit_id', 'None')

    # Check if the user-agent and cookie match the allowed values
    if user_agent != ALLOWED_USER_AGENT or visit_id != ALLOWED_COOKIE_VALUE:
        return "Access Denied: Invalid user-agent or cookie", 403

    # Create a response
    response = make_response(render_template(
        'home.html',
        user_agent=user_agent,
        visit_id=visit_id
    ))

    return response


@app.route('/clear_cookies', methods=['GET', 'POST'])
def clear_cookies():
    response = make_response("Cookies cleared! Redirecting back to home...")
    response.set_cookie('visit_id', '', max_age=0)  # Delete the cookie
    response.headers['Refresh'] = '2; url=/'  # Redirect to home after 2 seconds
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
