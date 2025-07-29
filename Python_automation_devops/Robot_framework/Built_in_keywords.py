'''
# Commonly Used Built-in Keywords in Robot Framework (With Examples)

## 1. Logging and Output

**Log**
```robot
Log    This is a message in the log.
```

**Log To Console**
```robot
Log To Console    Printing directly to console!
```

**Fail**
```robot
Fail    This test failed due to some error.
```

**Pass Execution**
```robot
Pass Execution    This test is marked as passed and execution stops here.
```

---

## 2. Control Flow and Assertions

**Should Be Equal**
```robot
Should Be Equal    5    5
```

**Should Not Be Equal**
```robot
Should Not Be Equal    5    10
```

**Should Be True**
```robot
Should Be True    ${result} == 10
```

**Should Be False**
```robot
Should Be False    ${is_active}
```

**Run Keyword If**
```robot
Run Keyword If    ${status} == 'OK'    Log    Status is OK
```

**Run Keywords**
```robot
Run Keywords    Log    Step 1    AND    Log    Step 2
```

**Continue For Loop**
```robot
FOR    ${item}    IN    @{LIST}
    Run Keyword If    ${item} == 0    Continue For Loop
    Log    Processing ${item}
END
```

**Exit For Loop**
```robot
FOR    ${item}    IN    @{LIST}
    Run Keyword If    ${item} == 10    Exit For Loop
    Log    Processing ${item}
END
```

---

## 3. Variables and String Manipulation

**Set Variable**
```robot
${value}=    Set Variable    Hello
Log    ${value}
```

**Set Test Variable**
```robot
Set Test Variable    ${myvar}    TestValue
```

**Set Suite Variable**
```robot
Set Suite Variable    ${suite_var}    SuiteValue
```

**Catenate**
```robot
${greeting}=    Catenate    Hello    World
Log    ${greeting}
```

**Replace String**
```robot
${text}=    Replace String    Hello Robot    Robot    Framework
Log    ${text}    # Output: Hello Framework
```

---

## 4. Collections

**Create List**
```robot
@{numbers}=    Create List    1    2    3
Log    @{numbers}
```

**Create Dictionary**
```robot
&{person}=    Create Dictionary    name=John    age=30
Log    &{person}
```

**Append To List**
```robot
@{fruits}=    Create List    apple
Append To List    ${fruits}    banana
Log    @{fruits}
```

**Get From List**
```robot
${first}=    Get From List    ${fruits}    0
Log    ${first}
```

**Get From Dictionary**
```robot
${name}=    Get From Dictionary    ${person}    name
Log    ${name}
```

---

## 5. Error Handling and Assertions

**Should Contain**
```robot
Should Contain    @{fruits}    apple
Should Contain    Hello World    World
```

**Should Not Contain**
```robot
Should Not Contain    @{fruits}    orange
```

**Should Be Empty**
```robot
Should Be Empty    ${EMPTY}
```

**Should Not Be Empty**
```robot
Should Not Be Empty    ${name}
```

**Should Be Less Than**
```robot
Should Be Less Than    5    10
```

---

## 6. Execution Control

**Sleep**
```robot
Sleep    2s
```

**Wait Until Keyword Succeeds**
```robot
Wait Until Keyword Succeeds    1 min    5 sec    Keyword That Might Fail
```

---

## 7. Importing Libraries and Resources

**Import Library**
```robot
Import Library    SeleniumLibrary
```

**Import Resource**
```robot
Import Resource    common_resources.robot
```

---

Let me know if you'd like more detailed examples or specific use cases!
'''