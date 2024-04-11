# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#
#Issues
#Issue 1: The search term is hardcoded and not user-configurable.
#Issue 2: The code doesn't handle cases where the user input search term is less than 4 characters.
#Issue 3: The .txt files are saved in the same directory as the script, which can lead to clutter.
#Issue 4: The convert_to_str function could be simplified using str() and join().

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

# Task 4:
def convert_to_str(obj):
    return '\n'.join(str(item) for item in obj)

# IMPLEMENTATION 1: sequential example
def wiki_sequentially():
    t_start = time.perf_counter()
    
    # Task 1:
    search_term = input("Enter a search term: ")
    
    # Task 2:
    if len(search_term) < 4:
        search_term = "generative artificial intelligence"
    results = wikipedia.search(search_term)
    
    def dl_and_save(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        
        # Task 3:
        if not os.path.exists("wiki_dl"):
            os.makedirs("wiki_dl")
        out_filename = os.path.join("wiki_dl", title + ".txt")
        
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    for item in results:
        dl_and_save(item)

    print('\nsequential function:')

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 2: concurrent example w/ threads
def concurrent_threads():
    t_start = time.perf_counter()
    
    # Task 1:
    search_term = input("Enter a search term: ")
    
    # Task 2:
    if len(search_term) < 4:
        search_term = "generative artificial intelligence"
    results = wikipedia.search(search_term)
    
    def dl_and_save_thread(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        
        # Task 3:
        if not os.path.exists("wiki_dl"):
            os.makedirs("wiki_dl")
        out_filename = os.path.join("wiki_dl", title + ".txt")
        
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save_thread, results)
    print('\nthread pool function:')

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 3: concurrent example w/ processes
def concurrent_process():
    t_start = time.perf_counter()
    
    # Task 1:
    search_term = input("Enter a search term: ")
    
    # Task 2:
    if len(search_term) < 4:
        search_term = "generative artificial intelligence"
    results = wikipedia.search(search_term)
    
    def dl_and_save_process(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        
        # Task 3:
        if not os.path.exists("wiki_dl"):
            os.makedirs("wiki_dl")
        out_filename = os.path.join("wiki_dl", title + ".txt")
        
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save_process, results)
    print('\nprocess pool function:')

    t_end = time.perf_counter()
    t_lapse = t_end - t_start
    print(f'code executed in {t_lapse} seconds')

if __name__ == "__main__":
    wiki_sequentially()
    concurrent_threads()
    concurrent_process()