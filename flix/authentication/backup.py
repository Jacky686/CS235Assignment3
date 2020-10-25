# from flask import Blueprint, render_template, redirect, url_for, session
#
# authentication_blueprint = Blueprint('authentication_bp', __name__)
#
#
# @authentication_blueprint.route('/register', methods=['GET', 'POST'])
# def register():
#     return render_template(
#         'authentication/authentication.html',
#     )
#
#
# @authentication_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template(
#         'authentication/authentication.html',
#     )
#
#
# @authentication_blueprint.route('/logout')
# def logout():
#     return redirect(url_for('home_bp.home'))
