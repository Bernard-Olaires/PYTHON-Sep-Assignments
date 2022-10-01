from flask_app import app #first new import
from flask_app.controllers import users #import from conrollers folder

# @app.route('/')
# def index():
#     return redirect('/users')

# @app.route('/users')
# def users():
#     users = User.get_all()
#     return render_template("users.html", all_users=users)

# @app.route('/users/new')
# def new():
#     return render_template("new_user.html")

# @app.route('/user/create', methods=['POST'])
# def create():
#     print(request.form)
#     User.save(request.form)
#     return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=8000)