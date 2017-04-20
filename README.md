# Django2

Django Tutorial: Code School


## Introduction

* A grid layout
* A detail page that appears on-click
* A form
* Image uploads
* User authentication
* User Profile
* AJAX

## 1.1 A grid Layout.

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_mgec0n5fizfqaso8t73hw93q175v6u.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0f624ebe7fd6b05edfe9d561ca84aae08161d916ca26d5175ac66dc4c1eb5666bc6c0e2c1430033d98aa23ca5b0d4912394c09629e2bef)

Use _bootstrap.css_ to use the grid layout.

####Examples of counters:
**_forloop.counter_** counts the number of *for* loop iteration so far. <br>
**_forloop.counter0_** exists too. <br>

####Examples of filters:

value | filter: filter_argument <br>
value | filter | other_filter: argument <br>
{% for location in locations|dictsort:'name' %} <br>
 
## 1.2 Routing - Details Page

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_163b007o2ha24y513krpzi1oa1kjrv.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0f6346ba7e53ca6aff382572930ae861f7c20d418958fca617d94c6a7cf0ec9d60ee7e7b7779aceb4a0313c7405e2776148c10da94a889)

What are the steps? <br>
* Create a **url** in _urls.py_ <br>
* Create the new **view** in _views.py_ <br>
* Create a new html layout in _templates\something.html_ <br>

## 1.3 Template Inheritance

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_94y97pg1l0f9q2uvn3dkm724f9rbqg.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0f6346bb73a31633cdb12a0e4199c76b97264db3e8f469512c83bf5c9172f390d7a06a3ed0de31df204b3dcbc185fd90b663843cd04c81)

How to share repeated html code across web-pages.

* Step 1 - Create a template/base.html for base template
* Step 2 - Create a {% extends 'base.html' %}
* Step 3 - {% block content %}{ endblock }

## 2.1 Django Forms

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_1rgnc9lgvqpki1auyhis7fyv00j9p3.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0f6346bf7917d89ad9fdbe62874a418ece97bfca12275c38690bc41bd63146a9b21ac891a84a89ecba36d443d3b7c770de6ff7ed2a275f)

* Create a _forms.py_ module which will use **from django import forms** to create forms <br>
* In _urls.py_ create a POST URL handling <br>
* In _views.py_ create post view
* Don't forget to update main def in _views.py_ with new form

For more complex renders, like passwords and date pickers you can use **form widgets**.

## 2.2 Model Forms

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_13544w8ks1zby1i6uqq417imfauxo9.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0f6346b07c1bcf62d49fc63d5cac3f94ee63c1b260c9302db783598fee4e6764fb75e569ed3ab711226009d3ce70d5af2ea367cdb64edb)

Here we use **meta classes**.
To do it in _forms.py_, from .models import the needed model, then create the class objectForm with Forms.ModelForm 
passed as argument. In it pass class Meta where you specify model and fields in the model you need.

