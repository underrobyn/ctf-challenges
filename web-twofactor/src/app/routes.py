from flask import render_template, send_from_directory, Blueprint, redirect, url_for, request, abort, flash
from . import static_folder, login_manager, db
from flask_login import login_required, logout_user, current_user, login_user
from .forms import CreateUserForm, LoginUserForm
from .models import User

main = Blueprint("main", __name__)


@main.route('/robots.txt')
@main.route('/security.txt')
def static_from_root():
    return send_from_directory(static_folder, request.path[1:])


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(static_folder, 'img/')


@main.route('/')
@login_required
def index():
    return render_template('home.html', current_user=current_user)


@main.route('/auth/', methods=['GET', 'POST'])
def auth():
    login_form = LoginUserForm(prefix="login")
    create_form = CreateUserForm(prefix="create")

    active_pane = 'login' if request.form.get('form_name') is None else request.form.get('form_name')

    if current_user.is_authenticated:
        flash('You are already logged in!', 'warning')
        return redirect(url_for('user_bp.account'))

    if request.method == 'POST':
        if request.form.get('form_name') == 'create' and create_form.validate_on_submit():
            active_pane = 'create'
            user = User.query.filter_by(email=create_form.email.data).first()

            if user is None:
                new_user = User(
                    name=create_form.name.data,
                    email=create_form.email.data,
                    password=create_form.password.data,
                    active=0,
                    account_type=1
                )

                db.session.add(new_user)
                db.session.flush()
                db.session.commit()

                flash('Account has been created however it must be activated by an administrator', 'success')
            else:
                flash('Email address cannot be used', 'warning')

            return redirect(url_for('auth_bp.auth'))

        if request.form.get('form_name') == 'login' and login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()

            if user is None:
                flash('Could not log you in, please try again.', 'danger')
            elif not user.verify_password(login_form.password.data):
                flash('Could not log you in please try again.', 'danger')
            elif user.active == 0:
                flash('Your account is not active', 'danger')
            else:
                login_user(user, remember=True)
                next_url = request.args.get('next')

                return redirect(next_url or url_for('main_bp.index'))

    return render_template('auth.html', login_user=login_form, create_user=create_form, active_pane=active_pane)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.auth"))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)

    return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("main.auth", next=request.path))
