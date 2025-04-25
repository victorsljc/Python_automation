"""
📌 What is Data?
    Data is a collection of raw facts, figures, or symbols that can be processed to generate meaningful information.
    It can be numbers, text, images, audio, video, or even symbols.
    Data on its own may not have meaning — its value comes when it's processed, organized, or analyzed.

📊 Types of Data
    1️⃣ Based on Nature
        Type	        Description	                        Example
        Qualitative	    Descriptive data (non-numeric)	    Colors, names, gender
        Quantitative	Numerical/measurable data	        Age, height, salary

    2️⃣ Based on Structure

        Type	        Description	                        Example
        Structured	    Organized in rows/columns (tables)	Databases, spreadsheets
        Unstructured	No specific format or structure	    Images, videos, emails
        Semi-structured	Partially organized (tags, keys)	JSON, XML, NoSQL

    3️⃣ Based on Usage in Programming (Python)

        DataType	        Description	                        Example
        Integer	            Whole numbers	                    10, -5
        Float	            Decimal numbers	                    3.14, -0.001
        String	            Text	                            "hello", "123"
        Boolean	            True or False	                    True, False
        List	            Ordered, mutable collection	        [1, 2, 3]
        Tuple	            Ordered, immutable collection	    (1, 2, 3)
        Set	                Unordered,unique values	            {1, 2, 3}
        Dictionary	        Key-value pairs	                    {"name": "Kavya"}
        NoneType	        Represents null/empty	            None

🛠️ Usage of Data
    📌 In Real World
            Analytics & Decision Making: Sales data, user behavior, trends
            AI/ML Models: Training on labeled/unlabeled data
            Healthcare: Patient records, diagnosis predictions
            Finance: Market trends, risk assessment
            Marketing: Customer segmentation, ad targeting

    📌 In Programming
            Storage & Retrieval: Databases, files
            Processing & Analysis: Using Python, Pandas, SQL
            Visualization: Charts and dashboards
            Communication: APIs exchanging JSON/XML data


🐍 Python Data Types — Introduction & Examples
        🔍 What Are Data Types?
                In Python, data types define the kind of value a variable holds, which helps the interpreter know how to store and manipulate that value.
                Python is dynamically typed, meaning you don’t need to explicitly declare the data type — it's inferred at runtime.

    🧱 Built-in Data Types in Python
        1️⃣ Numeric Types
            int: Integer values (e.g., 10, -5)
            float: Decimal values (e.g., 3.14, -0.01)
            complex: Complex numbers (e.g., 2 + 3j)

            x = 10          # int
            y = 3.14        # float
            z = 2 + 3j      # complex
            print(type(z))  # <class 'complex'>

        2️⃣ Text Type
            str: Sequence of Unicode characters (e.g., "hello")

                name = "Kavya"
                print(name.upper())  # KAVYA
        3️⃣ Sequence Types
            list: Ordered, mutable collection

                fruits = ["apple", "banana", "mango"]
                fruits.append("grape")
                print(fruits)
            tuple: Ordered, immutable collection

                coordinates = (10.5, 20.3)
                print(coordinates[0])
            range: Sequence of numbers

                for i in range(3):
                    print(i)  # 0, 1, 2
        4️⃣ Set Types
            set: Unordered collection with unique elements

                s = {1, 2, 3, 2}
                print(s)  # {1, 2, 3}
            frozenset: Immutable version of set

                fset = frozenset([1, 2, 3])
                # fset.add(4)  # ❌ will raise error
        5️⃣ Mapping Type
            dict: Key-value pairs

                student = {"name": "Kavya", "age": 22}
                print(student["name"])  # Kavya
        6️⃣ Boolean Type
            bool: True or False

                a = 5
                b = 10
                print(a < b)  # True
        7️⃣ Binary Types
            bytes, bytearray, memoryview

                b = bytes("hello", "utf-8")
                print(b)  # b'hello'
        8️⃣ None Type
            NoneType: Represents the absence of a value

                x = None
                print(x is None)  # True


"""