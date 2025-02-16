

def test_create_file():
    import pandas as pd
    # Create a DataFrame
    data = {
        "Name": ["John", "Alice"],
        "Age": [30, 25],
        "City": ["New York", "Los Angeles"],
    }
    df = pd.DataFrame(data)

    # Step 1: Write the DataFrame to a CSV file
    df.to_csv("output.csv", index=False)

def test_read_large_file():
    import pandas as pd

    # Step 1: Read the CSV file in chunks
    chunk_size = 1000  # Number of rows per chunk
    chunks = pd.read_csv("large_data.csv", chunksize=chunk_size)

    # Step 2: Process each chunk
    for chunk in chunks:
        print(chunk)  # Process the chunk as needed
