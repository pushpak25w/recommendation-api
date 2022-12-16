from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api,Resource, reqparse
from model import predictCategory
import json
from getTitle import get_video_title

app= Flask(__name__)
api=Api(app)
args=reqparse.RequestParser()
args.add_argument("title",action='append',help="send title",required=True)


class Category(Resource):
    def put(self,curr_room):
        print(curr_room)
        tmpArgs=args.parse_args()
        title=tmpArgs['title'][0]
        return {'category':str(predictCategory(title)[0])}

api.add_resource(Category,"/category/<string:curr_room>")

if __name__=="__main__":
    app.run(debug=True)
