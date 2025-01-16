from flask import Flask, request, send_from_directory, render_template_string, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "secret-key"  # Needed for flashing messages

# Define upload and download directories
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configurations
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload size

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload and Download</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        form { margin: 20px; }
        button { padding: 10px 20px; background-color: #008CBA; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #005f6b; }
        .message { margin-top: 20px; color: green; }
    </style>
</head>
<body>
    <h1>File Upload and Download</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" id="fileUpload" required>
        <button type="submit" id="uploadSubmit">Upload File</button>
    </form>

    {% if uploaded_file %}
    <p class="message">File uploaded successfully: <strong>{{ uploaded_file }}</strong></p>
    {% endif %}

    <h2>Download File</h2>
    <form action="/download" method="get">
        <button type="submit" id="fileDownload">Download Sample File</button>
    </form>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    """Render the upload and download form."""
    return render_template_string(HTML_TEMPLATE)


@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle file uploads."""
    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        flash("No file selected for upload.")
        return redirect(url_for("index"))

    # Save the file to the upload folder
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    flash(f"File uploaded successfully: {file.filename}")
    return render_template_string(HTML_TEMPLATE, uploaded_file=file.filename)


@app.route("/download", methods=["GET"])
def download_file():
    """Provide a sample file for download."""
    sample_file_name = "sample_file.txt"
    sample_file_path = os.path.join(app.config["UPLOAD_FOLDER"], sample_file_name)

    # Create a sample file if it doesn't exist
    if not os.path.exists(sample_file_path):
        with open(sample_file_path, "w") as f:
            f.write("This is a sample file for testing downloads.\n")

    return send_from_directory(
        directory=app.config["UPLOAD_FOLDER"],
        path=sample_file_name,
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
