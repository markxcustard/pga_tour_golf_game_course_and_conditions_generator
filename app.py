from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Logic to fetch data from the database or perform some computation
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)


@app.route('/api/more-data', methods=['GET'])
def get_more_data():
    # Return some sample data as a JSON response
    data = {'message': 'Hello again from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
