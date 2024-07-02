On the day 6 of the Python training we learned about the File Handling and discussed the below concepts:

-Persistence:

Persistence in the context of programming often refers to the process of storing and retrieving data from various data sources, such as databases, files, or external APIs. Here, I'll provide some materials and explanations for dealing with data persistence in Python.

-File Modes:

Some of the most common file modes are:
- `r`: Opens a file for reading. (default)
- `w`: Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
- `a`: Opens a file for appending. Creates a new file if it does not exist.
- `x`: Creates a new file. Returns an error if the file exists.
- `r+`: Opens a file for reading and writing.
- `w+`: Opens a file for writing and reading. Creates a new file if it does not exist or truncates the file if it exists.

-Resources management:

When working with files, it is important to close the file after you are done with it. You can use the `close()` method to close the file. Alternatively, you can use the `with` statement to automatically close the file when you are done with it.

-Reading and Writing CSV Files:

CSV (Comma Separated Values) files are a common way to store tabular data. Python provides a built-in `csv` module for reading and writing CSV files.

Also, we learned about Serialization and Deserialization:

Serialization is the process of converting an object into a format that can be stored or transmitted. Deserialization is the process of converting the serialized data back into an object. Python provides built-in modules like `pickle` and `json` for serialization and deserialization.


-Serialization with Pickle:

Pickle is a module in Python that allows you to serialize and deserialize Python objects. You can use the `pickle.dump()` method to serialize an object to a file and the `pickle.load()` method to deserialize an object from a file.

