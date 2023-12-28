from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if(len(args) == 1):
        return singleParam(args)
    elif(len(args) > 1):
        return multipleParam(args)
    return USERS


def singleParam(parameter):
    returnData = USERS
    if 'id' in parameter and parameter['id']:
        returnData = list(filter(lambda item: item["id"] == parameter['id'], returnData))
    elif 'name' in parameter and parameter['name']:
        returnData = list(filter(lambda item: parameter['name'].lower() in item['name'].lower(), returnData))
    elif 'age' in parameter and parameter['age']:
        returnData = list(filter(lambda item: int(parameter["age"])+1 >= int(item['age']) and int(parameter["age"])-1 <= int(item['age']), returnData))
    elif 'occupation' in parameter and parameter['occupation']:
        returnData = list(filter(lambda item: parameter['occupation'].lower() in item['occupation'].lower(), returnData))
    return returnData

def multipleParam(parameter):
    returnData = USERS
    returnData = list(filter(lambda item: 
    ("id" in parameter and item["id"] == parameter['id']) or
    ("name" in parameter and parameter['name'].lower() in item['name'].lower()) or
    ("age" in parameter and int(parameter["age"])+1 >= int(item['age']) and int(parameter["age"])-1 <= int(item['age'])) or
    ("occupation" in parameter and parameter['occupation'].lower() in item['occupation'].lower())
    , returnData))
    return returnData