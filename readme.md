# Issues
### Issue 1: The search term is hardcoded and not user-configurable.
### Issue 2: The code doesn't handle cases where the user input search term is less than 4 characters.
### Issue 3: The .txt files are saved in the same directory as the script, which can lead to clutter.
### Issue 4: The convert_to_str function could be simplified using str() and join().

# Solutions
### Solution 1: Added user input functionality to prompt the user for a search term.
### Solution 2: Implemented a condition to check the length of the user input and set the default search term if necessary.
### Solution 3: Added code to create a new directory "wiki_dl" if it doesn't exist and store the .txt files in that directory.
### Solution 4: Simplified the convert_to_str function using str() and join() to convert the input object to a string.


# Assignments
### Issue 1,4: Ameya Kashid
### Issue 2: Ahmed Alanazi
### Issue 3: Clement Liao
### Issue 4: Group Effort


# Description
### Issue 1: Search term was hardcoded, so we added code to let users input their own search term.  
### Issue 2: For short search terms (less than 4 characters), we made the program use a default search term to ensure relevant results.  
### Issue 3: To avoid cluttering the main directory, we created a new directory called "wiki_dl" to store the downloaded text files.  
### Issue 4: We simplified the convert_to_str function using a list comprehension and the join() method, making it more concise and readable. 





 
