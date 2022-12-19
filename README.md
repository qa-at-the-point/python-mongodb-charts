# python-mongodb-charts

- [Setup](#setup)
    - [Gitpod](#gitpod)
    - [Local Machine Requirements](#machine-requirements)
    - [Browsers and Drivers](#browsers-and-drivers)
- [Run Tests](#run-tests)

This is an example repo for working with MongoDB and visualizing data with MongoDB Charts.

> 💡 This project uses [Pylenium.io](https://docs.pylenium.io) which is a wrapper of Selenium similar to WebDriver.io for JavaScript or Watir for Ruby.

## Setup

This section will help you set things up so you can work with this project.

> 💡 Using Gitpod is the recommended way to work with QA at the Point repos, but you can clone this locally as well

### Gitpod

With Gitpod, you just open a workspace and you're done 🎉

### Machine Requirements

- 🐍 Python 3.8+
- 📦 Poetry as the package manager
- 💻 VS Code recommended

### Browsers and Drivers

Gitpod and Pylenium will automatically handle the driver binaries needed to work with Selenium.

- If in Gitpod, point pylenium.json's `local_path` to either `/usr/bin/chromedriver` (default) or `/usr/bin/geckodriver` since the browsers are _already_ installed
- Otherwise, `Pylenium` will handle downloading the correct driver binaries you need! Just make sure you have the actual browsers installed

## Run Tests

- If in Gitpod, open `Port 6080` if you'd like to see the tests run in "head" mode
- Otherwise, Pylenium runs tests in "head" mode by default

```bash
# Run all tests in the Terminal
poetry run pytest
```
