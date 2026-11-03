
lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]


def clean_customer(raw):

    # Split record
    data = raw.split(';')

    if len(data) != 4:
        return None

    # Clean fields
    name = " ".join(data[0].split()).title()
    email = data[1].strip().lower()
    phone = data[2].strip()
    city = " ".join(data[3].split()).title()

    # Validate name
    words = name.split()

    if len(words) == 0:
        return None

    for word in words:
        if not word.isalpha():
            return None

    # Validate city
    if city == "":
        return None

    # Validate email
    if email.count('@') != 1:
        return None

    parts = email.split('@')

    username = parts[0]
    domain = parts[1]

    if username == "":
        return None

    if domain == "":
        return None

    if '.' not in domain:
        return None

    if domain[0] == '.' or domain[-1] == '.':
        return None

    # Clean phone
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    if phone.startswith("+91"):
        phone = phone[3:]

    elif len(phone) == 12 and phone.startswith("91"):
        phone = phone[2:]

    # Validate phone
    if len(phone) != 10:
        return None

    if not phone.isdigit():
        return None

    if phone[0] not in "6789":
        return None

    # Return dictionary
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }


# Process all records
rejected = 0

for raw in lines:

    result = clean_customer(raw)

    if result is None:
        rejected += 1

    else:
        print(result)

print("Rejected:", rejected)
