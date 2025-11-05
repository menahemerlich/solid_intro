from classes.exercise_s1.book import Book
class Save_to_file(Book):


    def save_to_file(self, filename):
        with open(f"{filename}.txt", "a") as f:
            f.write(f"title: {self.title}, author: {self.author}, content: {self.content}")




