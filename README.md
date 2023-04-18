# Hawker

<p align="center">
  <p align="center">
    <img src="https://github.com/ohmpnt/Senior-Project/blob/main/static/assets/HawkerRM.png" height="200"/>
  </p>
</p>

<i> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Hawker definition, a person who hunts with hawks or other birds of prey. This symbolizes how our application is able to detect a user's personal information with eyes like a hawk. </i>

## About
   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **A web application** that integrates a number of OSINT techniques to search for the target user's sensitive data. The user's photo and any private information that has been made publicly accessible online are retrieved. A risk score is created using the data gathered. This rating informs the user of the level of danger associated with accessing the information and how much information they have exposed online. Finally, based on the risk score, recommendations are made to the user to enable him or her decide how to use the information and maintain their privacy.


## Main features

* detect user's exposed sensitive information
* email breach checker by [Infoga](https://github.com/m4ll0k/Infoga)
* Reverse image 
* Websites with user's account by [Maigret](https://github.com/soxoj/maigret)
* Risk Evaluation


## Installation

Maigret can be installed using pip, Docker, or simply can be launched from the cloned repo.

Standalone EXE-binaries for Windows are located in [Releases section](https://github.com/soxoj/maigret/releases) of GitHub repository.

Also you can run Maigret using cloud shells and Jupyter notebooks (see buttons below). 

[![Open in Cloud Shell](https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/soxoj/maigret&tutorial=README.md)
<a href="https://repl.it/github/soxoj/maigret"><img src="https://replit.com/badge/github/soxoj/maigret" alt="Run on Replit" height="50"></a>

<a href="https://colab.research.google.com/gist/soxoj/879b51bc3b2f8b695abb054090645000/maigret-collab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="45"></a>
<a href="https://mybinder.org/v2/gist/soxoj/9d65c2f4d3bec5dd25949197ea73cf3a/HEAD"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder" height="45"></a>

### Package installing

**NOTE**: Python 3.7 or higher and pip is required, **Python 3.8 is recommended.**

```bash
# install from pypi
pip3 install maigret

# usage
maigret username
```

### Cloning a repository

```bash
# or clone and install manually
git clone https://github.com/soxoj/maigret && cd maigret
pip3 install -r requirements.txt

# usage
./maigret.py username
```

### Docker

```bash
# official image
docker pull soxoj/maigret

# usage
docker run -v /mydir:/app/reports soxoj/maigret:latest username --html

# manual build
docker build -t maigret .
```

## Usage examples

```bash
# make HTML and PDF reports
maigret user --html --pdf

# search on sites marked with tags photo & dating
maigret user --tags photo,dating

# search for three usernames on all available sites
maigret user1 user2 user3 -a
```

Use `maigret --help` to get full options description. Also options [are documented](https://maigret.readthedocs.io/en/latest/command-line-options.html).

## Credit

[Maigret](https://github.com/soxoj/maigret)<br/>
[Infoga](https://github.com/m4ll0k/Infoga)<br/>
[Facebook-scraper](https://github.com/kevinzg/facebook-scraper)
