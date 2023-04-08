from flask import Flask, jsonify, request

app = Flask(__name__)
# This config is added because Flask sorts JSON keys alphabetically, we want our order so this value is set to false
app.config['JSON_SORT_KEYS'] = False

# Person Class
class Person:
    def __init__(self, id, firstName, lastName, email, phone, createdDate):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.createdDate = createdDate

# Mock Data
persons = [
    Person(1, 'John', 'Doe', 'johndoe@example.com',
           '+90-599-99-99', '2022-03-15 12:00:00'),
    Person(2, 'Jane', 'Doe', 'janedoe@example.com',
           '+90-599-99-92', '2022-03-16 10:30:00'),
    Person(3, 'Bob', 'Smith', 'bobsmith@example.com',
           '+90-599-99-92', '2022-03-12 14:45:00'),
    Person(4, 'Alice', 'Johnson', 'alicejohnson@example.com',
           '+90-599-99-95', '2022-03-18 08:15:00'),
    Person(5, 'David', 'Lee', 'davidlee@example.com',
           '+90-599-99-90', '2022-03-20 16:00:00')
]

# This function orders persons data by created date.
def orderPersonsByCreatedDate(persons_list):
    # Uses lambda function to sort function by created date. Used sorted() function against sort() function because sort function mutates the original data
    sortedPersons = sorted(persons_list, key=lambda x: x["createdDate"], reverse=True)
    return sortedPersons

# This function excludes the selected key.
def excludeKey(lst, key):
    persons_list_excluded = [
        {k: v for k, v in d.items() if k != key} for d in lst]
    return persons_list_excluded

# Generic error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Generic error handler
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Main API endpoint
@app.route('/persons', methods=['GET'])
def getPersons():
    persons_list = []
    # Used the convertion because both orderPersonsByCreatedDate and excludeKey function uses list of dict as input
    for person in persons:
        persons_list.append(person.__dict__)
    return jsonify(orderPersonsByCreatedDate(excludeKey(persons_list,"phone")))


if __name__ == '__main__':
    app.run(debug=True)
