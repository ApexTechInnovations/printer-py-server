from flask import Flask, request, jsonify
import os
import subprocess

from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])

@app.route('/print', methods=['POST'])
def print_pdf():
    try:
        # Get the file name from the request body
        file_name = request.json.get('fileName')

        if file_name is None:
            raise ValueError('File name is missing in the request.')

        # Get the relative file path
        rel_file_path = os.path.relpath(file_name)

        subprocess.run(['C:\\Users\\PROY\\AppData\\Local\\SumatraPDF\\sumatrapdf.exe', '-print-to-default', rel_file_path])

        return jsonify({'message': 'Print job submitted successfully.'}), 200
    except Exception as e:
        # Print the exception details
        print(str(e))
        return jsonify({'error': 'Error submitting print job.'}), 500

    
@app.route('/delete', methods=['OPTIONS', 'DELETE'])
def delete_data():
    if request.method == 'OPTIONS':
        # Respond to preflight request
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Methods'] = 'DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    try:
        # Get the file name from the request body
        file_name = request.json.get('fileName')

        if file_name is None:
            raise ValueError('File name is missing in the request.')

        # Implement the logic to delete the file or perform any other necessary actions
        # For example, you can use os.remove to delete a file
        os.remove(file_name)

        return jsonify({'message': f'File {file_name} deleted successfully.'}), 200
    except Exception as e:
        # Print the exception details
        print(str(e))
        return jsonify({'error': 'Error deleting file.'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
