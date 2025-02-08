source link :- https://selectorshub.com/xpath-practice-page/
Xpaths
1. //*[@text='New User ? Register here/Activate']:
    This selects any element (*) that has an attribute named "text" whose value is exactly equal to "New User ? Register here/Activate".
    This is appropriate if the string you provided is the value of an attribute called text

2. //*[text()='New User ? Register here/Activate']:
    This selects any element (*) whose text content (the text displayed inside the element) is exactly equal to "New User ? Register here/Activate".
    The text() function extracts the text content of the element.
    This is appropriate if the string is the text that is displayed directly within the element, not the value of an attribute.

3. //*[contains(text(),'New User ? Register here/Activate')]
    source link - https://retail.onlinesbi.sbi/retail/login.htm

4. //*[contains(@href, 'step')]

5. //*[contains(@text, 'New User ? Register here/Activate')]
6. //div[@id='content']/child::p
7. //div[@id='main-section']/following::div
8. //div[@id='username']/parent::form
9. //input[@type='text']/ancestor::form
10. //input[@id = 'text']//self::input
