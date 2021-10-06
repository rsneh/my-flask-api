users = [
    {
        "id": 1,
        "first_name": "Ron",
        "last_name": "Sneh",
        "hobby": "Pizza"
    },
    {
        "id": 2,
        "first_name": "Inbal",
        "last_name": "Rosen",
        "hobby": "Ice Cream"
    },
    {
        "id": 3,
        "first_name": "Edgar",
        "last_name": "Rahamimov",
        "hobby": "Shawarma"
    }
]


def get_users():
    return users


def get_user(id):
    user = None
    for u in users:
        if u["id"] == int(id):
            user = u
    return user


def add_user(user):
    user["id"] = get_new_id()
    users.append(user)
    return user


def delete_user(id):
    find_index = None
    for index, item in enumerate(users):
        if item['id'] == int(id):
            find_index = index

    if find_index is not None:
        user = users.pop(find_index)
        return user

    return None


def get_new_id():
    return len(users) + 1
