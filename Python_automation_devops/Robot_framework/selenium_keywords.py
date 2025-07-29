'''
# Commonly Used SeleniumLibrary Keywords in Robot Framework (with Examples)

## 1. Browser Management

**Open Browser**
```robot
Open Browser    https://example.com    chrome
```

**Close Browser**
```robot
Close Browser
```

**Maximize Browser Window**
```robot
Maximize Browser Window
```

**Set Window Size**
```robot
Set Window Size    1024    768
```

---

## 2. Navigation

**Go To**
```robot
Go To    https://example.com/page2
```

**Reload Page**
```robot
Reload Page
```

**Go Back**
```robot
Go Back
```

**Go Forward**
```robot
Go Forward
```

---

## 3. Element Interaction

**Click Element**
```robot
Click Element    xpath=//button[@id="submit"]
```

**Input Text**
```robot
Input Text    id=username    myuser
```

**Clear Element Text**
```robot
Clear Element Text    id=password
```

**Select From List By Value**
```robot
Select From List By Value    id=country    IN
```

**Select From List By Label**
```robot
Select From List By Label    id=country    India
```

**Mouse Over**
```robot
Mouse Over    css=.menu-item
```

---

## 4. Element Verification

**Element Should Be Visible**
```robot
Element Should Be Visible    id=logout
```

**Element Should Contain**
```robot
Element Should Contain    id=welcome-msg    Welcome
```

**Element Should Not Be Visible**
```robot
Element Should Not Be Visible    id=error-message
```

**Page Should Contain Element**
```robot
Page Should Contain Element    xpath=//div[@class="banner"]
```

**Page Should Contain**
```robot
Page Should Contain    Login Successful
```

---

## 5. Screenshots

**Capture Page Screenshot**
```robot
Capture Page Screenshot    login_screen.png
```

**Capture Element Screenshot**
```robot
Capture Element Screenshot    id=profile-pic    profile_pic.png
```

---

## 6. Waiting

**Wait Until Element Is Visible**
```robot
Wait Until Element Is Visible    id=dashboard    timeout=10s
```

**Wait Until Element Is Not Visible**
```robot
Wait Until Element Is Not Visible    id=loading    timeout=15s
```

**Wait Until Page Contains**
```robot
Wait Until Page Contains    Welcome    timeout=5s
```

---

## 7. Alert Handling

**Handle Alert**
```robot
Handle Alert    ACCEPT
```

**Alert Should Be Present**
```robot
Alert Should Be Present
```

**Input Text Into Alert**
```robot
Input Text Into Alert    My response
```

---

## 8. Window and Frame Management

**Select Window**
```robot
Select Window    title=My Page
```

**Select Frame**
```robot
Select Frame    index=0
```

**Unselect Frame**
```robot
Unselect Frame
```

---

## 9. Getting Values

**Get Title**
```robot
${title}=    Get Title
Log    ${title}
```

**Get Location**
```robot
${url}=    Get Location
Log    ${url}
```

**Get Text**
```robot
${welcome}=    Get Text    id=welcome-msg
Log    ${welcome}
```

---

These keywords provide most of the functionality needed for web automation in Robot Framework using SeleniumLibrary.
Let me know if you want more advanced examples or explanations!
'''