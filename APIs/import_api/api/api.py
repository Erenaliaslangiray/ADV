import os
from datetime import datetime

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
allowed_file_types=["csv"]

# Can add endpoint later.
@app.route("/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if file.filename.rsplit('.', 1)[1] in allowed_file_types:
        filename = secure_filename(file.filename)
        filename_formatted = filename.rsplit('.', 1)[0] + str(datetime.now())+ "." + filename.rsplit('.', 1)[1]
        file.save(os.path.join("./files", filename_formatted))
        # TODO send req to next part.
        #  .
        resp = jsonify({"message" : "File imported successfully."})
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({"message" : "Error while importing file. Wrong input file type.",
                        "details" : "Allowed file types are {0}".format(allowed_file_types)})
        resp.status_code = 400
        return resp
