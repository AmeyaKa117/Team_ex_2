
# Refactoring Process

The code was refactored to improve functionality and user interaction. Below is a summary of the tasks undertaken during the refactoring process:

### Issues and Resolutions

#### Issue 1: Search Term Input
- **Description**: The search term was hardcoded, which limited the tool's usability.
- **Resolution**: Modified the script to allow for user input while setting a default search term if the input is less than 4 characters.
- **Assignment**: Ameya
#### Issue 2: Default Search Term for Short Inputs
- **Description**: Short search terms provided by the user might not yield meaningful results.
- **Resolution**: Implemented a default to "generative artificial intelligence" for inputs shorter than 4 characters to ensure relevant results.
- **Assignment**: Ahmed

#### Issue 3: Organization of Downloaded Files
- **Description**: The main directory became cluttered with downloaded files.
- **Resolution**: Created a new directory "wiki_dl" where all the text files are now saved.
- **Assignment**: Clement


#### Issue 4: Function Optimization
- **Description**: The `convert_to_str` function was verbose and not optimally efficient.
- **Resolution**: Simplified the function using list comprehension and the `join()` method to enhance conciseness and readability.
- **Assignment**: Divya


