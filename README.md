# Data Centric Development Milestone Project:
### Create an online cookbook. With the focus being on databases, create a web application that allows users to store and easily access cooking recipes.

## License
This project is licensed under the MIT License - see the [license.txt](license.txt) file for details

## Author & contributor list
*Jennifer Dick*

## Table of contents
1. [Overview](#overview)
2. [Deployment](#deploy)
3. [Features](#features)
4. [Technology used](#tech)
5. [Testing](#testing)
6. [Versioning](#version)
7. [Acknowledgements and credits](#credits)

<a name="overview"></a>
## Overview
### What is this website for?
This is a site that allows users to create, read, update and delete recipes.

### What does this website do?
This website is motivated by the brief provided by [The Code Institute](https://codeinstitute.net/) and uses the criteria supplied. It was imperative that I create a site that helps users to:
* Search a recipe
* Filter these recipes by specific criteria
* Add recipes
* Edit recipes
* Delete recipes

### How does it work?
This website uses **MongoDB** which is a NoSQL document-oriented database program.

The site uses plain **HTML** and **CSS** to route users to search and filter recipes which, depending on their search style, controls which **JavaScript** to execute.

The app relies on **JavaScript** and **JQuery** to search, filter and display the user results.

**Python** **Flask**

The site is styled with **Bootstrap** and I have made the site responsive so users can use this application whilst on the go.

<a name="deploy"></a>
## Deployment - AMENDMENTS REQUIRED FOR HEROKU. PLACEHOLDER ONLY.
1. Enable GitHub Pages on GitHub settings.
2. Select Master Branch
3. GitHub URL is then produced. Copy this.
4. If deploying to own infrastructure replace api key with your own on index.html.
5. Add copied URL to Google API Console. Both the Google Maps and Google Places API need to be enabled.
5.1 Go to Google Cloud Platform Console
5.2 Select project
5.3 Select 'APIs'
5.4 Select API under 'Enabled APIs'
5.5 Select 'Credentials'
5.6 Select relevent API key
5.7 Scroll to 'Accept requests from these HTTP referrers (web sites)' and add copied URL.

<a name="features"></a>
## Features
* Eye catching index page
* Large easy to see and use search box
* Clear search results with specific criteria to further filter by
* Add, edit and delete functionality for all recipes


### Features left to implement
* None

<a name="tech"></a>
## Technology used
* [Balsamiq](https://balsamiq.com/)
    * Used to create mock ups of the site which have been uploaded as PDF files
* **Html**, **CSS** and **JavaScript**
    * Base languages used to create the site
* [Visual Studio Code]
    * Code editor used to write above code
* [JQuery](https://jquery.com/)
    *
* [mongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    *database program used
* [Summernote](https://summernote.org/)
    *Rich text editor for addrecipes.html and editrecipes.html forms
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    * Web framework used to help style this single page application
* [BBC Good Food](https://www.bbcgoodfood.com/)
    *Used for the recipe content (so I didn't have to channel my inner Delia Smith)
* [Git](https://git-scm.com/)
    * Used for version control
* [Heroku](https://www.heroku.com/)
    * Platform used to host my versioning
* Other resources used: [Fontawesome v5.7.2](https://fontawesome.com/)

<a name="testing"></a>
## Testing
* HTML code checked via a [HTML code validator](https://validator.w3.org/)
* CSS code checked via a [CSS code validator](https://jigsaw.w3.org/css-validator/)
* Asked colleagues, friends and family to check this site and access from their own devices; any small changes were made and committed.
* Used a [website response tool](https://www.responsinator.com) to test how well the website responded to different device sizes.
*  Checked every feature worked (and looked consistent) in:
    * Google Chrome
    * Internet Explorer 10
    * Microsoft Edge
    * Opera
*  Used incognito mode on **Google Chrome** to remove all cached data.

## User stories as part of testing
As a user I want to...
1. search 'x' and find EXAMPLE1. Test performed and true.
2. search 'x' and find EXAMPLE1 and click on a result and it... . Test performed and true.
3. search 'x' and find EXAMPLE1 and then change type to x and my search to be updated. Test performed and true.
4. search 'x' and find EXAMPLE1 and then type 'EXAMPLE2' and my search to be updated. Test performed and true.
5. search 'x' and find no results for any search. Test performed and true.

<a name="version"></a>
## Versioning
I used **Git** for versioning on this project. And hosted this on Heroku.

<a name="credits"></a>
## Acknowledgments/credits
* *Antonija Šimić* - mentor.
* *Paul Lewis* - colleague (Software Developer) who tested my finished site.

##Commands to remember
cmd.exe
cd flask_app
py -m venv env
env\Scripts\activate
set FLASK_ENV=development

#### *MIT © 2019 Jennifer Dick*