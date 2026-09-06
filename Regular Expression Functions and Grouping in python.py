import re
text = 'Contact: rahul@mail.com'
re.match(r'Contact', text)
  # matches — pattern is at the start
re.search(r'\w+@\w+\.com', text)
  # finds 'rahul@mail.com' anywhere
re.findall(r'\w+@\w+\.com', text)
  # ['rahul@mail.com']
pattern = r'(\d{2})-(\d{2})-(\d{4})'   # dd-mm-yyyy
match = re.search(pattern, '25-08-2026')
match.group(0)   # '25-08-2026'   (full match)
match.group(1)   # '25'           (day)
match.group(2)   # '08'           (month)
print(re.sub(r'\d{10}', 'XXXXXXXXXX', text))
print(re.sub(r'\s+', ' ', text))
print(re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\2-\1', '25-08-2026'))
