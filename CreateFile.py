import uuid

def create_temp_file(file_name, file_content):
    with open(rf"C:\Users\ofirb\PycharmProjects\pythonProject2\{file_name}", 'w') as f:
        f.write(file_content)
        print(f"File {file_name} created successfully")