# Pennewise - A personal finance manager for students

## Table of contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
Pennywise is a personal finance management application designed specifically for students. It helps users effectively manage their finances, stay within budget, and achieve their financial goals.

## Features
- Expense and Balance tracking 
- Update income 
- Simple data visualization 
- Sorting expense records based on given month
- Four static categories to reduce complexity

## Technologies/Frameworks 
- Html
- Css
- Javascript
- Django Web Framework
- MySQL

## Installation
1. Clone the repository.
```bash
 git clone https://github.com/SushantHande04/Pennywise.git
```

2. Install [Python](https://www.python.org/downloads/) latest version.

3. Install [django](https://docs.djangoproject.com/en/5.0/topics/install/) web framework.
```bash
 python -m pip install django
```

4. Install [MySQL](https://www.mysql.com/downloads/) workbench and client.
- Create a database using MySQL command client
```sql
CREATE DATABASE pfm;
```

5. Navigate to settings file in Personal_Finance_manager folder 
- Change the database settings as per your requirements (line 78)

6. Migrate all database tables to your own database 
```bash
 python manage.py makemigrations 
```
```bash
 python manage.py migrate
```

7. After successful migration run the server 
```bash
 python manage.py runserver
```


## Usage
- Sign Up / Log In: Create an account or log in to your existing account.
- Add Expenses: Record your daily expenses by category.
- Update income when necessary 
- Simple data visualization: View your monthly expenses and income.
