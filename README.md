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

Maigret can be installed using pip and simply can be launched from the cloned repo.

### Package installing

**NOTE**: Python 3.8 or higher and pip is required, **Python 3.8 is recommended.**

### Cloning a repository to directory

```bash
# clone a repository
git clone https://github.com/ohmpnt/Senior-Project && cd Senior-Project
```

```bash
# clone folder Maigret and replace in our Maigret folder directory
git clone https://github.com/soxoj/maigret

# then go to the maigret directory and run this command in your terminal
pip3 install -r requirements.txt
```

```bash
# clone Infoga and replace in our Infoga folder directory
git https://github.com/m4ll0k/infoga

# Then go to the Infoga directory and run this command in your terminal
python setup.py install 
```
### Then follow these steps
```bash
# install Python Flask
pip install -U Flask
```
```bash
# install Selenium 4
pip install -U selenium
```
```bash
# install googlescrape
pip install googlescrape
```
```bash
# install googlesearch
python3 -m pip install googlesearch-python
```

```bash
# install facebook-scraper
pip install facebook-scraper
```
```bash
# install google
pip install google
```

## Usage examples

```bash
# run web server
flask run

# run web server (open debug mode: On)
python -m flask run --debug
```

## Credit

[Maigret](https://github.com/soxoj/maigret)<br/>
[Infoga](https://github.com/m4ll0k/Infoga)<br/>
[Facebook-scraper](https://github.com/kevinzg/facebook-scraper)<br/>
[Googlesearch](https://pypi.org/project/googlesearch-python/)
