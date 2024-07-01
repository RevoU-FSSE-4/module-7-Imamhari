from flask import Blueprint, request
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from models.user import User

from sqlalchemy import select

from flask_login import login_user, logout_user, login_required

from decorators.role_checker import role_required




user_routes = Blueprint("user_routes", __name__)

#register
@user_routes.route("/register", methods=["POST"])
def register():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()

    try:
        NewUser = User(
            username=request.form["username"],
            email=request.form["email"],
            role=request.form["role"],
        )

        NewUser.set_password(request.form["password"])

        s.add(NewUser)
        s.commit()

    except Exception as e:
        # print(e)
        s.rollback()
        return {"message": "Fail to register"}, 501

    return {"message": "Success to register"}, 200


#login
@user_routes.route("/login", methods=["POST"])
def login():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()

    try:
        email = request.form["email"]
        user = s.query(User).filter(User.email == email).first()

        if user is None:
            return {"message": "User not found"}, 404
        
        if not user.check_password(request.form["password"]):
            return {"message": "Wrong password"}, 401
        
        login_user(user)

        session_id = request.cookies.get("session")

        return {
            "session_id": session_id,
            "message": "Success to login"
        }, 200
    
    except Exception as e:
        s.rollback()
        return {"message": "Fail to login"}, 501
    

# get login user
@user_routes.route("/login", methods=["GET"])
@role_required("admin")
def get_login_user():
    Session = sessionmaker(connection)
    s = Session()

    try:
        Users = select(User)
        result = s.execute(Users)
        user_account = []

        for row in result.scalars():
            user_account.append({
                "id": row.id,
                "username": row.username,
                "email": row.email,
                "role": row.role
            })

        return {
            "user_account": user_account,
            "message": "Success to get login user"
        }, 200
    
    except Exception as e:
        return {"message": "Fail to get login user"}, 501
#logout
@user_routes.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return {"message": "Success to logout"}, 200


    