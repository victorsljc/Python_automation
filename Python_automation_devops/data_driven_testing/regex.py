# >>>>>>>>>>>>>>>>>>>>>>  REG FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
Regular expressions (regex) are a powerful tool for pattern matching and text manipulation in Python.
They are widely used in QA automation for tasks like:

    1.Validating input data (e.g., emails, phone numbers)

    2.Extracting specific information from logs or responses

    3.Searching and replacing text

    findall	 ->   Returns a list containing all matches
    search	 ->   Returns a Match object if there is a match anywhere in the string
    split	 ->   Returns a list where the string has been split at each match
    sub	     ->   Replaces one or many matches with a string

1. re.match()
    Checks if the pattern matches at the beginning of the string.
    re.match(pattern, string, flags=0)
2. re.search()
    Searches for the pattern anywhere in the string.
    re.search(pattern, string, flags=0)
3. re.findall()
    re.findall(pattern, string, flags=0)
    Returns all non-overlapping matches of the pattern in the string as a list.
4. re.finditer()
    re.finditer(pattern, string, flags=0)
    Returns an iterator yielding match objects for all non-overlapping matches.
5. re.sub()
    re.sub(pattern, repl, string, count=0, flags=0)
    Replaces all occurrences of the pattern in the string with a replacement string.

Common Regex Patterns
        Digits: \d
        Word Characters: \w (letters, digits, underscore)
        Whitespace: \s
        Any Character: .
        Start of String: ^
        End of String: $
        Quantifiers:
        *: 0 or more [Use * when the preceding element is optional or can appear multiple times.]
        +: 1 or more [Use + when the preceding element must appear at least once.]
        ?: 0 or 1
        {n}: Exactly n times
        {n,}: n or more times
        {n,m}: Between n and m times
        ^   : starts with
        $   : ends with
        []	: A set of characters [Used to specify a set of characters that can match at a particular position in the string.]
            Key Features
                Single Character Match:
                    Matches one character from the set inside the brackets.
                        Example: [abc] matches a, b, or c.

                Ranges:
                    Use a hyphen (-) to specify a range of characters.
                        Example: [a-z] matches any lowercase letter.

                Negation:
                    Use ^ at the beginning of the character class to negate it.
                        Example: [^abc] matches any character except a, b, or c.
                Special Characters:
                        Most special characters (e.g., ., *, +) lose their special meaning inside [].

        ()  : capture and grouping
                Used to group parts of a regex pattern, apply quantifiers to groups, or extract specific parts of a match.
                Key Features
                    Capturing Group:
                        Captures the matched text for later use (e.g., extraction or backreferencing).
                        Example: (abc) captures the sequence abc.

                    Quantifiers:
                        Apply quantifiers (e.g., *, +, ?) to the entire group.
                        Example: (abc)+ matches abc, abcabc, etc.
                    Backreferences:
                        Use \1, \2, etc., to refer to captured groups within the same regex.
                        Example: (a)\1 matches aa.
                    Non-Capturing Groups:
                        Use (?:...) to group without capturing.
                        Example: (?:abc)+ matches abc, abcabc, but does not capture the group.
'''


def test_re_match():
    import re
    result = re.match('^world', 'hello world')
    if result:
        print(result.group())
    else:
        print('no match')


def test_re_search():
    import re
    result = re.search('world', 'this is the world and the bad world')
    print(result.group())


def test_re_find_all():
    import re
    result = re.findall('world', 'this is the world where bad worldly people leave')
    print(result)


def test_re_find_iter():
    import re
    s = 'this is the world where bad worldy=ly people live'
    result = re.finditer('world', s)
    for x in result:
        print(x.group(), 'at position', x.start())


def test_re_sub():
    import re
    result = re.sub('\d+', 'X', 'there are 3 apples and 4 bananas')
    print(result)


def test_verify_email():
    import re
    email = "test@example.com"
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")


def test_extract_phone_number():
    import re
    text = "Contact us at 123-456-7890 or 987.654.3210."
    pattern = r'\d{3}+[-.]+\d{3}+[-.]+\d{4}'
    phone_numbers = re.findall(pattern, text)
    print(phone_numbers)


def test_replace_multitple_spaces():
    import re
    text = 'this   is    a    text'
    pattern = r'\s+'
    print(re.sub(pattern, ' ', text))


def test_extract_url():
    import re
    text = "Visit https://example.com or http://test.org."
    pattern = r"https?://[^\s]+"
    urls = re.findall(pattern, text)
    print(urls)


def test_remove_digit_and_special_char_from_string():
    a = 'this is ba3234la vee3ra234nja3232neya;'
    pattern = r'[^0-9;]'
    import re
    print(''.join(re.findall(pattern, a)))


def test_usage_of_square_brackets():
    import re
    pattern = r"^[aeiou]+$"
    text = "aeiou"
    if re.match(pattern, text):
        print("Only vowels")


def test_usage_of_paranthesis():
    import re
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    text = "2023-10-05"
    match = re.search(pattern, text)
    if match:
        year, month, day = match.groups()
        print(f"Year: {year}, Month: {month}, Day: {day}")


def test_reading_file_and_using_regex():
    import re
    # Step 1: Open and read the file
    with open("example.txt", "r") as file:
        content = file.read()

    # Step 2: Define the regex pattern for emails
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    # Step 3: Find all matches
    emails = re.findall(email_pattern, content)

    # Step 4: Print the results
    print("Emails found:", emails)


def test_writing_file_using_regex():
    import re

    # Step 1: Open and read the file
    with open("input.txt", "r") as file:
        content = file.read()

    # Step 2: Define the regex pattern for phone numbers
    phone_pattern = r"\b\d{3}[-.]\d{3}[-.]\d{4}\b"

    # Step 3: Find all matches
    phone_numbers = re.findall(phone_pattern, content)

    # Step 4: Write the results to a new file
    with open("output.txt", "w") as file:
        for number in phone_numbers:
            file.write(number + "\n")

    print("Phone numbers extracted and saved to output.txt")


def test_searching_replacing_text_in_file_using_regex():
    import re

    # Step 1: Open and read the file
    with open("document.txt", "r") as file:
        content = file.read()

    # Step 2: Define the regex pattern for dates (e.g., YYYY-MM-DD)
    date_pattern = r"\d{4}-\d{2}-\d{2}"

    # Step 3: Replace all dates with "DATE"
    updated_content = re.sub(date_pattern, "DATE", content)

    # Step 4: Write the updated content back to the file
    with open("document_updated.txt", "w") as file:
        file.write(updated_content)

    print("Dates replaced and saved to document_updated.txt")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< REGEX CLOSED >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
