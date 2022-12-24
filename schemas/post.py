from operator import itruediv


def postEntity(item) -> dict:
    
    return {
        "id": str(item["_id"]),
        "usr": item["usr"],
        "mens": item["mens"],
        "imgs": item["imgs"],
    }

def postEntityA(item) -> dict:
    
    return {
        "id": str(item["_id"]),
        "usr": item["usr"],
        "mens": item["mens"],
        "imgs": item["imgs"],
        "autor": item["author"],
    }
    
def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]

def postsEntityA(entity) -> list:
    return [postEntityA(item) for item in entity]

def serializeDict(a) -> dict:
    return {
        **{i: str(a[i]) for i in a if i == "_id"},
        **{i: a[i] for i in a if i != "_id"},
    }


def serializeList(entity) -> list:

    return [serializeDict(a) for a in entity]
