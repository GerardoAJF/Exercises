"""
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side.

When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. 

If the book is "n" pages long, and a student wants to turn to page "p", what is the minimum number of pages to turn? They can start at the beginning or the end of the book. 

    - n number of pages
    - p target page    

Return the minimum number of pages that must be turned in order to arrive at page "p". 

========SAMPLE========

Input:
n = 5
p = 3

Output:
1

| X | 1 |   | 2 | 3 |   | 4 | 5 |

Using the diagram above:
If the student wants to get to page 3, they open the book to page 1, flip 1 page and they are on the correct page. 
If they open the book to the last page, page 5, they turn 1 page and are at the correct page. 
Return 1. 
"""

def drawing_book(number_pages, to_page):
    pages = list(range(number_pages + 1))

    if number_pages % 2 == 0:
        pages.append(0)

    start_count = 0
    for page in pages:
        if page == to_page:
            break
        start_count += 1
    start_count //= 2

    end_count = 0
    for page in pages[::-1]:
        if page == to_page:
            break
        end_count += 1
    end_count //= 2

    return min(start_count, end_count)


print(drawing_book(5, 3))
