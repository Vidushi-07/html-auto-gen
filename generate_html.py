import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auto-Generated Page</title>
</head>
<body>
    <h1>Welcome to My Auto-Generated Page!</h1>
    <p>This HTML page was generated using Python and published via GitHub Actions.</p>
</body>
</html>
"""

# Ensure the output directory exists
output_dir = "public"
os.makedirs(output_dir, exist_ok=True)

# Write the HTML file
with open(f"{output_dir}/index.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully!")
