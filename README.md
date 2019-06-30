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
The site uses **HTML** and **CSS** to route users to search and filter recipes which, depending on their search style, controls which **Python** command runs.

**Flask** has been used as the presentation engine to process data from the database to show it on screen. 

This website uses **MongoDB** which is a NoSQL document-oriented database program.

**Pymongo** is the **Python** library used for accessing the data in **MongoDB**.

**Json** and **Bson** are dependencies used and added by **Pymongo**. **Jinga** is a dependency used by **Flask**.

The site is styled with **Bootstrap** and I have made the site responsive so users can use this application whilst on the go.

<a name="deploy"></a>
## Deployment

* I have used the automated deployment engine on Heroku which gets triggered by a push/sync.


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
* **Html** and **CSS**
    * Base languages used to create the site
* [Visual Studio Code]
    * Code editor used to write above code
* [mongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    * Database program used
* [Summernote](https://summernote.org/)
    * Rich text editor for addrecipes.html and editrecipes.html forms
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    * Web framework used to help style this single page application
* [BBC Good Food](https://www.bbcgoodfood.com/)
    * Used for all recipe content (so I didn't have to channel my inner Delia Smith)
* [Git](https://git-scm.com/)
    * Used for version control
*[Github](https://github.com/)
    * Used as hosting platform for git
* [Heroku](https://www.heroku.com/)
    * Platform used to host website
* Other resources used: [Fontawesome v5.7.2](https://fontawesome.com/)

<a name="testing"></a>
## Testing

* Used "TypeError:" as a debugger to catch when one of the operands or arguments passed to a function was incompatible with the type expected.
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
1. search 'chicken' and find five recipes. Test performed and true.
2. search 'Lankan' and find 1 recipe of 'Sri Lankan fried chicken' and click on the result and it to open the recipe page. Test performed and true.
3. search 'pizza' and find 'Fresh topped pizza' and then from the Search Results page type 'BBQ' and my search to be updated. Test performed and true.
4. search 'frog' and find 0 recipes and a warning message. Test performed and true.
5. click on "Vegan" from the dropdown filter and see the results limit. Test performed and true.
6. click on the 'Add recipe' button and be able to add a recipe and for the mandatory fields to stop form submission if not completed. Recipe to appear on the index page in a new card. Test performed and true.
7. from any chosen recipe click 'Like recipe' button and for the 'Recipe likes:' to update on the recipe and on the homepage card. Test performed and true.
8. from any chosen recipe click 'Edit recipe' button and to be taken to the edit page, make changes and for these to be reflected in recipe and index pages. Test performed and true.
9. from any chosen recipe click 'Delete recipe' button and a confirmation pop up to appear, on clicking OK the recipe will be removed from the website and database. Test performed and true.


<a name="version"></a>
## Versioning
I used **Git** for versioning on this project, hosted **Git** on **Github**. Hosted website on **Heroku**.

<a name="credits"></a>
## Acknowledgments/credits
* *Antonija Šimić* - Code Institute mentor.
* *Paul Lewis* - colleague (Software Developer) who tested my finished site.
* *Haley Schafer* - Code Institute tutor. For help with deployment to Heroku.

## Commands to remember
* cmd.exe
* cd flask_app
* py -m venv env
* env\Scripts\activate
* set FLASK_ENV=development

#### *MIT © 2019 Jennifer Dick*