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

# Insert your WorkFlowy E-mail and Password below. Change the path to your Firefox executable if necessary; use double backslash on Windows.
WF = WorkFlowyAssistant(email, password, 'C:\\Program Files\\Mozilla Firefox\\firefox.exe')

# Replace the first string with the ID of the parent node. You can find it if you zoom in on the parent node and copy the id after
# 'https://beta.workflowy.com/#/' in the address bar of your browser. 
# Put all items to add in a list. Instead of calling the function for every item, it is better to generate the list first and call it
# once.
WF.add_new_bullet('5e8b93132997', [
    'A',
    'B',
    'C',
])
```