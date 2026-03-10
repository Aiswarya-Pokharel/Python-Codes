name = input("Enter your name: ")
headline = input("Enter a short headline: ")
bio = input("Enter a bio: ")
email = input("Enter your valid email: ")
phone = int(input("Enter your mobile number: "))
address = input("Enter your address: ")
photo = input("Enter path or URL of your photo: ")


html_content = f"""
<!DOCTYPE html>
<html>
<head>
<title>{name} Resume</title>
<style>
body {{
    background:#f4f4f4;
    padding:40px;
}}

.container {{
    background:white;
    max-width:800px;
    margin:auto;
    padding:30px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,0.1);
}}

.header {{
    text-align:center;
}}

img {{
    width:120px;
    height:120px;
    border-radius:50%;
    object-fit:cover;
}}

h1 {{
    margin:10px 0;
}}

.section {{
    margin-top:20px;
}}

a {{
    color:blue;
}}
</style>
</head>

<body>

<div class="container">

<div class="header">
<img src="{photo}" alt="Profile Photo">
<h1>{name}</h1>
<h3>{headline}</h3>
</div>

<div class="section">
<h2>Bio</h2>
<p>{bio}</p>
</div>

<div class="section">
<h2>Contact</h2>
<p><b>Email:</b> {email}</p>
<p><b>Phone:</b> {phone}</p>
<p><b>Address:</b> {address}</p>
</p>
</div>

</div>

</body>
</html>
"""

file = open("resume.html", "w", encoding="utf-8")
file.write(html_content)
file.close()

print("\n Resume created successfully!")
print("Open 'resume.html' in your browser.")