# warCraftSelenium

### Using Selenium with Python to navigate WarCraft website. 

This is an example of how to test automate a simple flow of signup at Warcraft website. 

This site some challanges when using Selenium such as:
- Nested shadow DOMs
- Load time
- Disabled elements
- Actions requiring javascript execute

Required tools:
- Selenium
- Chrome webdriver
- Python
- Pytest
- Pytest-html
- Github Actions

Github Actions Workflow is activated only if a push is made to the tests folder. 

At the end an artifact is generated with the report generated with Pytest-Html.

After each run artifacts are uploaded and retained for 30 days. 

Todo:
- [x] Use faker to generate user information for SignUp
- [x] Implement other browsers such as Firefox and Edge
- [x] Add differente window size resolutions
