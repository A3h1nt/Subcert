<p align="center">
  <img width="1000" height="230" src="/images/subcert.png">
</p>

# Subcert
Subcert is a subdomain enumeration tool, that finds all the valid subdomains from certificate transparency logs. 

## Table of contents
* [Setup](#Setup)
* [Demo](#Demo)
* [Contribute](#contribute)
* [Contact Me](#Contact-Me)

## Setup
### Step 1: Install Python 3
```
apt-get install python3-pip
```
### Step 2: Clone the Repository
```
git clone https://github.com/A3h1nt/Subcert.git
```
### Step 3: Install Dependencies
```
pip3 install -r requirements.txt
```
### Step 4: Move the Directory to /opt 
```
mv subcert /opt/
```
### Step 5: Add an alias in .bashrc to run the script from anywhere
```
alias subcert="python3 /opt/subcert/subcert.py"
```

## Demo
[Watch demo on Youtube](https://www.youtube.com/watch?v=xihYOaM6p8Y)

## Contribute
- Improve Code
- Suggestions
- Report Bugs

## Contact Me

You can contact me regarding anything at [A3h1nt](https://twitter.com/A3h1nt)
