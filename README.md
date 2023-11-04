# warCraftSelenium

### Using Selenium with Python to navigate WarCraft website. 

This is an example of how to test automate a simple flow of signup at Warcraft website. 

This site some challanges when using Selenium such as:
- Nested shadow DOMs
- Load time
- Actions requiring javascript execute

Required tools:
- Selenium
- Chrome webdriver
- Python
- Pytest
- Pytest-html
- Github Actions

The flow is triggered when a push update is made to the repository. At the end an artifact is generated with the report generated with Pytest-Html.

Todo:
- Use faker to generate user information for SignUp
- Implement other browsers such as Firefox and Edge
- Add differente window size resolutions
