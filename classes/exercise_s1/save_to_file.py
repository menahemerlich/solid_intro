
class Save_to_file:
    def __init__(self, filename, book):
        with open(f"{filename}.txt", "a") as f:
            f.write(f"title: {book.title}, author: {book.author}, content: {book.content}")




