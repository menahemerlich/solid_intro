
class Save_to_file:
    @staticmethod
    def Save_to_file(filename, book):
        with open(f"{filename}.txt", "a") as f:
            f.write(f"title: {book.title}, author: {book.author}, content: {book.content}")




