db = db.getSiblingDB('catalog');

db.createCollection('r44goiania');

db['r44goiania'].createIndex({"title" : 1, "description" : 1, "category": 1 }, {unique: true});
