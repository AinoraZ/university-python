import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
restaurants_collection = mongo_client["restaurants-db"]["restaurants"]


# Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
def all_rows_from_collection():
    return restaurants_collection.find()


# Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
def all_rows_specific_fields():
    return restaurants_collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})


# Parašykite užklausą, kuri ayvaizduotų laukus - restaurant_id, name, borough ir cuisine -,
# bet nerodytų lauko field_id visiems dokumentams
def all_rows_specific_fields_without_id():
    return restaurants_collection.find({}, {"_id": 0, "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})


# Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
def all_restaurants_in_bronx():
    return restaurants_collection.find({"borough": "Bronx"})


# Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.
def all_restaurants_with_good_score():
    return restaurants_collection.find({"grades": {"$elemMatch": {"score": {"$gte": 80, "$lte": 100}}}})


def dump(header, collection):
    print(header)
    for row in collection:
        for key, value in row.items():
            print(f"{key}:", value)
        print("----------------")
    print("=======================")


def dump_grades(header, collection):
    print(header)
    for row in collection:
        for grade in row["grades"]:
            print(grade)
        print("----------------")
    print("=======================")


# dump("All rows from collection:", all_rows_from_collection())
# dump("All rows with fields (_id, restaurant_id, name, borough, cuisine):", all_rows_specific_fields())
# dump("All rows with fields (restaurant_id, name, borough, cuisine):", all_rows_specific_fields_without_id())
# dump("All restraurants in district bronx", all_restaurants_in_bronx())

# dump("All restraurants with score >=80 <=100", all_restaurants_with_good_score())
dump_grades("All restraurants with score >=80 <=100", all_restaurants_with_good_score())
