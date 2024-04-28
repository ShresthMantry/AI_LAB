import pandas as pd

data = {'Subjects': ['Math', 'Physics', 'Chemistry', 'Math', 'Physics'],
        'Book_Authors': ['Author1', 'Author2', 'Author3', 'Author1', 'Author2'],
        'No_of_Books': [10, 15, 5, 8, 12]}

IIIT_Library = pd.DataFrame(data)

total_books_by_subject = IIIT_Library.groupby('Subjects')['No_of_Books'].sum().reset_index()

print(total_books_by_subject)
