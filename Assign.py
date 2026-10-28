import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def create_file_if_missing(self):
        try:
            with open(self.filename, "x", encoding="utf-8"):
                pass
        except FileExistsError:
            pass
        except PermissionError:
            print("Error: You do not have permission to create the journal file.")

    def add_entry(self, text):
        if text.strip() == "":
            print("Error: Entry cannot be empty. Please write something.")
            return

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            self.create_file_if_missing()
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{current_time}]\n")
                file.write(text.strip() + "\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
        except OSError as error:
            print(f"Error: Something went wrong while saving the entry ({error}).")

    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if content.strip() == "":
                print("No journal entries found. Start by adding a new entry!")
                return

            print("\nYour Journal Entries:")
            print("-" * 33)
            print(content)
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
        except OSError as error:
            print(f"Error: Something went wrong while reading the file ({error}).")

    def search_entries(self, search_word):
        if search_word.strip() == "":
            print("Error: Please type a keyword or a date to search.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
            return
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
            return
        except OSError as error:
            print(f"Error: Something went wrong while reading the file ({error}).")
            return

        all_entries = [entry.strip() for entry in content.split("\n\n") if entry.strip()]
        matching_entries = [entry for entry in all_entries if search_word.lower() in entry.lower()]

        if matching_entries:
            print("\nMatching Entries:")
            print("-" * 33)
            for entry in matching_entries:
                print(entry)
                print()
        else:
            print(f"No entries were found for the keyword: {search_word}.")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        answer = input("\nAre you sure you want to delete all entries? (yes/no): ")

        if answer.strip().lower() == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            except FileNotFoundError:
                print("No journal entries to delete.")
            except PermissionError:
                print("Error: Permission denied. Cannot delete the journal file.")
            except OSError as error:
                print(f"Error: Could not delete the file ({error}).")
        else:
            print("Delete cancelled. Your entries are safe.")


def show_menu():
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")


def main():
    journal = JournalManager()

    while True:
        show_menu()

        try:
            choice = input("\nUser Input:\n").strip()

            if choice == "1":
                text = input("\nEnter your journal entry:\n")
                journal.add_entry(text)
            elif choice == "2":
                journal.view_entries()
            elif choice == "3":
                search_word = input("\nEnter a keyword or date to search: ")
                journal.search_entries(search_word)
            elif choice == "4":
                journal.delete_entries()
            elif choice == "5":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("\nInvalid option. Please select a valid option from the menu.")

        except (KeyboardInterrupt, EOFError):
            print("\n\nThank you for using Personal Journal Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()