## WorkFlowy Assistant
This module allows you to add multiple bullets under a parent node.

## Installation
```python
pip install workflowy-assistant
```

This module is dependent on Mozilla Firefox. Please install it if you don't have it: https://www.mozilla.org/nl/firefox/new/.

## Usage
```python
from workflowy_assistant import WorkFlowyAssistant

# Insert your WorkFlowy e-mail and password below.
email = 'abc@demo.com'
password = 'abcdef'

# Change the path to your Firefox executable if necessary; use double backslash on Windows.
pathToFirefox = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# Start the WorkFlowyAssistant
WF = WorkFlowyAssistant(email, password, pathToFirefox)

# Replace this with the ID of the parent node. You can find it if you zoom in on the parent node and copy the id after
# 'https://beta.workflowy.com/#/' in the address bar of your browser. 
parent_id = '5e8b93132997'

# Put all items you want to add in a list. Instead of calling the function for every item, it is better to generate the list first and
# call the function once.
listOfBullets = ['A','B','C']

# Add a list of new bullets under a parent node.
WF.add_new_bullet(parent_id, listOfBullets)

# Please close the process after all operations.
WF.close_browser()
```