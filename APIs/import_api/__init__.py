import os

try:
    os.mkdir("import_api/files")
except:
    pass

from . import api

api.api.app.run(host='0.0.0.0', port=5000)
