import re
from unstructured.cleaners.extract import extract_email_address


UK_PHONE_NUMBERS_PATTERN = (
    r"(?:(?:\+44\s?\(?\d{0,4}\)?)|(?:0\s?\d{0,4}))[\s-]?(\d{4})[\s-]?(\d{3})[\s-]?(\d{3})"
)

UK_PHONE_NUMBERS_RE = re.compile(UK_PHONE_NUMBERS_PATTERN)


# extract uk phone number 
def extract_uk_phone_numbers_from_contents(text: str):    
    phone_numbers = set()
    
    regex_matches = UK_PHONE_NUMBERS_RE.finditer(text)
    for match in regex_matches:
        phone_number = match.group(0).strip()
        
        phone_number = re.sub(r"\((0)\)\s+", r"(\1)", phone_number)
        phone_numbers.add(phone_number)
    
    return phone_numbers


# extract email address
def extract_emails_from_contents(text:str):
    return set(extract_email_address(text))


def transform_contents(text:str):
    ...