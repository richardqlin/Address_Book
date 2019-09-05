from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask('Address_Book')
app.config['MONGO_URI'] ='mongodb://localhost:27017/address-book-db'

Bootstrap(app)
mongo = PyMongo(app)


@app.route('/', methods= ['GET' , "POST"])

def address_book():
    if request.method == 'GET':
        doc=[x for x in mongo.db.AddressCollection.find({})]
        return render_template('page.html', saveAddress=doc)

    elif request.method == 'POST':
        doc = {}
        for item in request.form:
            doc[item]= request.form[item]
        mongo.db.AddressCollection.insert_one(doc)
        return redirect('/')

@app.route('/delete/<identity>')
def delete_contact(identity):
    print(identity)
    found = mongo.db.AddressCollection.find_one({'_id': ObjectId(identity)})
    mongo.db.AddressCollection.remove(found)
    return redirect('/')



app.run(debug = True)
