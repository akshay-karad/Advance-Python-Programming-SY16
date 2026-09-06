import re

# Input text
text = """
Please contact us at support@example.com or admin@college.edu.
You can also email john.doe123@gmail.com for more information.
"""

# Regular expression pattern for email
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the email addresses
print("Email addresses found:")
for email in emails:
    print(email)
