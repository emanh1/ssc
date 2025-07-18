from .user import user_bp
from .auth import auth_bp
from .course import course_bp
from .enrollment import enrollment_bp
from .assignment import assignment_bp
from .submission import submission_bp
from flask import Flask

def register_routes(app: Flask) -> None:
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(enrollment_bp)
    app.register_blueprint(assignment_bp)
    app.register_blueprint(submission_bp)
