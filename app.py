from flask import Flask, request, jsonify
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
@app.route('/print', methods=['POST'])
def print_text():
    try:
        # Get the text from the request body
        text = request.json.get('text')

        # Write the text to a temporary file
        file_path = 'C:\\Users\\PROY\\ANGULAR\\holamundo.txt'
        with open(file_path, 'w') as file:
            file.write(text)

        # Print the text file
        os.system(f'notepad /p {file_path}')  # You can use another program or command to print

        # Optionally, you can delete the temporary file
        os.remove(file_path)

        return jsonify({'message': 'Print job submitted successfully.'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error submitting print job.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Change the port if needed
