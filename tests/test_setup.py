from pymongo import MongoClient
from mongo import config


def test_required_environment_variables_are_available():
    assert config.MONGODB_ATLAS_URI


def test_connect_to_mongo():
    with MongoClient(config.MONGODB_ATLAS_URI) as mongo:
        response = mongo.admin.command("ismaster")
        assert response, "Unable to connect to MongoDB"
