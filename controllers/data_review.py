from flask import Blueprint, request
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from models.data_review import Review

from sqlalchemy import select
from decorators.role_checker import role_required
from flask_login import login_required


data_review_routes = Blueprint("data_review_routes", __name__)

#insert reviews
@data_review_routes.route("/review", methods=["POST"])
@login_required
def get_reviews():
    Session = sessionmaker(connection)
    s = Session()
    
    s.begin()
    try:
        newReview = Review(
        
            email=request.form["email"],
            rating=request.form["rating"],
            description=request.form["description"],
        )

        s.add(newReview)
        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Fail to insert"}, 501

    return {"message": "Success to insert"}, 200


#delete reviews
@data_review_routes.route("/review/<id>", methods=["DELETE"])
@role_required("user")
def delete_review(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        s.query(Review).filter(Review.id == id).delete()
        s.commit()
    except Exception as e:
        
        s.rollback()
        return {"message": "Fail to delete"}, 501

    return {"message": "Success to delete"}, 200

#update reviews
@data_review_routes.route("/review/<id>", methods=["PUT"])
@role_required("user")
def update_review(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        review = s.query(Review).filter(Review.id == id).first()
        review.email = request.form["email"]
        review.rating = request.form["rating"]
        review.description = request.form["description"]

        s.commit()
    except Exception as e:
        
        s.rollback()
        return {"message": "Fail to update"}, 501

    return {"message": "Success to update"}, 200


#get reviews
@data_review_routes.route("/review", methods=["GET"])
def get_all_reviews():
    Session = sessionmaker(connection)
    s = Session()

    reviews = select(Review)

    result = s.execute(reviews)
    review = []

    for row in result.scalars():
        review.append({
            "id": row.id,
            "email": row.email,
            "rating": row.rating,
            "description": row.description
        })

    return {
        "review": review,
        "message": "Success to get all reviews"
    }