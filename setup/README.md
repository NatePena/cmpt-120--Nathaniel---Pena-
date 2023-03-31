# Assignment 1 - Environment Setup

## Skills Acquired/Reinforced Upon Completion

- [ ] Install Git/VCS
- [ ] Launch Git bash/Windows Command Prompt/bash shell
- [ ] Install Python3
- [ ] Create Python module
- [ ] Enter some Git commands:
  - [ ] `git clone <options>`
- [ ] Enter some gh CLI commands
  - [ ] `gh auth <options>`
  - [ ] `gh repo <options>`

---

**NOTE**: _At any time you are uncertain, ask for help rather than attempting to continue. I don't expect you to understand most of this stuff, but it is important for you to have this environment setup for ease of learning._

## Setup

### Visual Studio Code Setup

Download and install the latest version of Visual Studio Code [here](https://code.visualstudio.com/). After the editor has finished installing; launch the program. Install the following plugins by pressing the 4 blocks on the left-hand side of the editor and searching for:

- [ ] Python
- [ ] Python Extension Pack
- [ ] Python Environment Manager
- [ ] Robot Framework Language Server
- [ ] Code Runner
- [ ] Open in Browser

### Python Environment Setup

Download and install the latest version of Python 3 [here](https://www.python.org/downloads/) for you operating system. Python 3 is the language we are going to be using in the course. In order to set up your Python3 environment, open up your command shell/command prompt/Git bash in the project directory and follow the instructions **below**.

```sh
# Create a virtual environment the in project directory.
python3 -m venv venv

# Activate the virtual environment using Windows command prompt.
venv\Scripts\activate

# Activate the virtual environment using OSX/Linux
./venv/bin/activate

# Import the necessary packages.
pip3 install -r requirements.txt
```

### Accessing/creating your GitHub account

We will be using GitHub as your code repository for this course. If you do not know what that is, do not worry; I will explain in class. If you do not already have an account, please visit [GitHub](https://education.github.com/pack) and in the center of the screen you should see a green button saying `Singup for Student Developer Pack`. Select `Get student benefits`

### Creating your personal access token

Once logged in, please go to the [tokens](https://github.com/settings/tokens) page. You should see a button that says "Generate new token", press that to generate a new token. Make sure that every box in is checked. Be sure to name it and to set the expiration for at least 30 days. When you are done, press "Generate token" at the bottom of the screen. Copy the token and save it someplace safe (it should look something like):

```
# THIS IS ONLY AN EXAMPLE.
ghp_kevin17MARIST9y2022SzdscMpT120ueo123
```

Remember this is a secret... **_DO NOT GIVE OUT YOUR TOKEN_**

### Git SCM installation

Download the latest version of Git [here](https://git-scm.com/). The reference manual can be found [here](https://git-scm.com/docs). Bookmark this very handy [cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)! You will need to learn how to use this version control tool.

### GitHub CLI installation

Download and install the latest version of GitHub CLI found [here](https://cli.github.com/manual/installation). If you do not know what GitHub or a CLI is, do not worry. I will explain what they are in class. We will be using this to manage our repository. If you prefer to use Git CLI instead of GitHub CLI that is fine too.

### Forking this repository

Login into your GitHub account using the GitHub CLI...

```sh
# invoke the gh cli to log in
gh auth login

# select "Github.com"
> Github.com
  Github Enterprise Server

# only select "SSH" if you have an SSH key setup.
> HTTPS
  SSH

# select "Paste an authentication token" and then paste the token we created earlier
  Login with a web browser
> Paste an authentication token
```

## Running Pytest Test Cases

To run these test cases manually, follow the steps below:

```sh
# Activate the virtual environment using Windows command prompt.
venv\Scripts\activate

# Activate the virtual environment using OSX/Linux
./venv/bin/activate

# run the tests
pytest
```
