# TableTop Six - Communal tabletop rpg book review site #

### TGC - Data Centric Development Milestone Project 3 ###
By: **Collin Wu Yuewei** -- *Code Institute Batch 8* -- 
##### Made with Python/Flask and MongoDB ######
<br> 

## SUMMARY ##
The intent of this webpage is to be a communal forum for enthusiast to share they review on books from their favourite tabletop rpg series. Giving basic information about he books, the cost, where to get them and what to expect.
<br>

##### Home Page Preview ####
![Website Preview Image](/static/images/proj3Home.png "Where to Park Website Homepage")
##### Book Review Info Preview ####
![Website Preview Image](/static/images/proj3Book.png "Where to Park Website Search Page")
##### Footer of Page Preview ####
![Website Preview Image](/static/images/proj3Footer.png "Where to Park Website Search Page")<br>
<br>


## PROJECT AIM/INTENT ##
The goal of the project is to build an data centric site with Python language with Flask framework and MongoDB to present useful information drawn from different user input via CRUD, using techonology and languages taught in the Code Institute Fullstack Web Developer Program; at Project 3, namely HTML, CSS, JS, Python, Flask, MongoDB.

__The concept chosen for this project is to create a communal book review website for enthusiast to share they review on books from their favourite tabletop rpg series. To become a resource or reference for others who might want to jump into the hobby, or looking for information__ 

The problem is that there are too many series of such tabletop rpgs, books are typically found at the main publisher's webpage at a mint condition price. While at amazon, you are able to obtain used copies for cheaper and a consolidated area for finding different books from different genres/series.<br>
<br>


## FULL DEMO ##

The full website demo can be previewed here: [Tabletop Six Webpage](https://cwy-tgc8-project-3.herokuapp.com/)

Responsive is tested using [Am I Responsive?](http://ami.responsivedesign.is/?url=https://cwy-tgc8-project-3.herokuapp.com/): <br>

![Responsive Demo on Various Devices](/static/images/amiresponsive.png "Website Responsiveness Preview")<br>
<br>

## WireFrames ##
The main wireframes made with [Wireframe CC](https://wireframe.cc/) are planned originally for the most crucial parts of the webpage, mainly the landing page and book review, as development goes, more features are added:<br>
<br>

Wireframe planning for Landing Page:
![Wireframe Landing Page](/static/images/wireframeMain.png "Wireframe planning for Landing Page")<br>
<br>

Wireframe planning for Book Review Page:
![Wireframe Book Page](/static/images/wireframeBook.png "Wireframe planning for Book Review Page")<br>
<br>

## Database Planning ##

As the database used for the project is MongoDB, database relationships are unnecessary as compared to SQL.

Things to Consider:<br>

Tabletop books review site community
- Public can see all records
- Public can send in new records
- Only OP can edit past records
- Only Users can leave ratings
- Only Users can leave comments

Records Management (database)
- Records to be browsed by categories
- Records have Image
- Records have Name
- Records have Author
- Records have Year of Publish
- Records have Price (Amazon, etc...)
- Records have Reviews ( 5Stars)
- Records have Comments
- Original Poster record

```
category
{
    "name":
    "publisher":
    "review_average": (Future Implement)
    "comments":
    "books": [], ## Using $lookup from Books, common field name -- category
}
```
```
books
{
    "category": 
    "name":
    "author":
    "release_date":
    "price":
    "reviews":
    "comments":
    "image":
    "created_by":
}
```
```
users
{
    "name":
    "email":
    "password":
    "terms_condition":
    "recieve_email":
}
```
```
mailing_list
{
    "name":
    "email":
}
```
<br>

## UX DESIGN ##

- Firstly the design is fully mobile responsive, navbar to collapsed hamburgers and book cards wrap to make 3 -> 2 -> 1 card per screen depending on size.<br>

- The layout is mainly designed for desktop users or large tablet users. There is a persistent sticky nav bar at the top as well as a persistent search banner thorughout each page for easy access.
    <br>
- The navbar has hover over indicators as well as a dropdown list for the categories available. It also changes the "Log In" to the user's name when logged in. 
    <br>
- The search bar have preset categories that are clickable (with hover color change effects) which redirects the user to the category page which shows all book reviews within it. The search bar itself when search takes the first keyword and finds the books relating to the search. You can try this by searching "Star" then completing it to "Starfinder".
    <br>
- All book review cards are linked to their own book review information page and can be clicked for quick information access
    <br>
- Buttons of Submit/Edit/Delete/Go to Category are all color coded and large for easy clicking
    <br>
- The footer is also persistent for a more holistic view as well as a call-to-action for users to donate to the site owners
    <br>
- User log in system is used to monitor new post, edits and deletes. This is to prevent other people removing valuable reviews. With that being said, there is a Adminstrative account that can access any review, edit or delete. In an event an user wants to edit a review that was not posted by them, they are redirected to the log in page. IF they want to edit the review, they would need to approach the adminstrator. 
- ##### Adminstrative Account <br>User Email:   __Admin__ <br> Password: __Admin__ <br> ######
- All users have the option to add their email to the monthly update email during creation
    <br>
- All user action to interact with the server, have color coded flash messages on success or errors
    <br>
- Forms are all validated and would not allow blank entries, if left empty will present a red outline and a small text suggesting the input. There are also quick look up for categories/series to post new reviews in.<br>
    <br>

## Features ##
- MongoDB Supported Webpage with Databases Collection Interactions
    - Card Display of Book Reviews (Governed by User Login Unique ID)
    - Communal - Free Forum (Anyone can make an Account)
    - Email mailing list database, for communications to the audience (Opted by User)
    - User login system and Admistrative Account for webpage moderation<br>

- Quick category access buttons in the search bar to see book reviews while having a Quick access Search Function with keyword search, replacing the category layout with searched book title results<br>
    - Sorted Reviews to their respective Series
    
- Beautiful quick access book review cards, that show a brief information or full book information on click<br>
    
- Quick Access Call-to-Action button that use GPS/Geolocation to determine location<br>
    
- Color-coded buttons and flashed messages for better UX<br>
  
- Monetization for both user and adminstrator of the webpage
    - Each review has to come with a link to Amazon or a Location where the book can be purchased
    - Encourages Affiliate Links that lead to used copies or cheaper pricing
    - Social Media contacts are constantly in the footer on all pages
    - Patreon Donation are encouraged with large banner at the bottom<br>
<br>

### Features Left to Implement ###

- Ability to consolidate each duplicate review into a master review copy to display at landing page
- Handling of duplicates to prevent spam or DDOS
- Consolidate all comments in a single review book info area, for better UX
- Mailing List DB to have system to write and send email to users easily for the adminstrator
- For log in users to have a profile and history of past reviews/comments
- Monetization modes to enable dropshipping or selling of items on the site itself instead of redirects
- Filtered Search option with Side Bar for better Searching<br>
<br>


## Technologies Used ##

__Front-End__
* [HTML](https://www.w3schools.com/html/ "HTML Info Page")
    - HTML is universal base language for creating webpages compatible with majority browsers

* [CSS](https://www.w3schools.com/css/ "CSS Info Page")
    - CSS is used for implementing styling to a webpage 

* [JavaScript](https://www.w3schools.com/js/ "JavaScript ES6 Info Page")
    - JavaScript is the programming language of HTML and the Web
    - Used for API data retrieval
    - Button interactions
    - Color background changes
    - Sort gathered information and creation of JSON for data collected for unified access
* [jQuery](https://jquery.com/ "jQuery Homepage")
    - Most commonly used JavaScript Library
    - Ajax API calling
    - Makes coding way easier than base JavaScript<br>
* [Wireframe CC](https://wireframe.cc/ "Wireframe Tool for Planning")
    - Used to design webpages wireframes quickly
    - Free to use

__Back-End__
* [Python](https://www.python.org/ "Python Homepage")
    - Primary Coding Lanuage for logic handling and interaction with MongoDB database
    - An interpreted, object-oriented, high-level programming language with dynamic semantics
* [Flask Framework](https://palletsprojects.com/p/flask/ "Flask Homepage")
    - Framework in conjunction with Jinja2 templating language for Python
    - Lightweight WSGI web application framework capable of scaling up
* [Jinja 2](https://jinja.palletsprojects.com/en/2.11.x/ "Jinja2 Homepage")
    - Jinja is a modern and designer-friendly templating language for Python
    - Modelled after Django’s templates
    - Fast, widely used and secure with the optional sandboxed template execution environment
* [MongoDB](https://www.mongodb.com/ "MongoDB Homepage")
    - Cross-platform document-oriented database program
    - Classified as a NoSQL database program
    - Uses JSON-like documents with optional schemas
* [Git](https://git-scm.com/ "Installation for Git Support")/[Github](https://github.com/ "Github Homepage")
    - For version control and commits to Github
* [Gitpod IDE](https://www.gitpod.io/ "Gitpod IDE Homepage")
    - Online open-source IDE from GitHub
    - Cloud narrative Development
    - Quick code reviews by sharing Links
    - Minimal IDE setup

__Deployment__
* [Heroku](https://www.heroku.com/ "Heroku Cloud Application Platform")
    - Quick free deployment of webpages
    - Whole dashboard system support
    - Connects with Github commits
    - Can be upgraded for Commerical Use/Customer Facing<br>
<br>

## Testing ##

#### Responsiveness ####
The webpage was manual tested for responsiveness on physical iPhone 6S, Samsung S8+, Xiaomi Mi Max2, 1920 x 1080 laptop screen.

[Responsiveness Tool](http://responsivetesttool.com/ "Responsiveness Tool Homepage")  and  [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?id=07L3WeU_nndVYwaUTleP7w "Mobile Friendly Test Homepage")  or [Am I Responsive Design](http://ami.responsivedesign.is/ "Am I Responsive Design Homepage"), was used to test different screen sizes and devices for responsiveness

![Responsive Demo with Responsiveness Tool](/static/images/responsivetool.png "Responsive Demo with Responsiveness Tool")<br>

![Responsive Demo with Mobile-Friendly](/static/images/mobilefriendly.png "Responsive Demo with Mobile-Friendly")<br>

All platforms had to have correct CSS design, working animation, buttons, pop-up and elements placed in the correct position.

#### Page Load Time ####

The page load time is tested using [Pingdom Tool](https://tools.pingdom.com/ "Pingdom Homepage") while being hosted on Heroku Platform. This is vital and important as the goal was to have a responsive, non-laggy webpage with no link-loading from page to page, achieving an __C__ rating of __77/100__ points also on Asia, America and European Servers. The major slow down is due to the off-site queries to the images hosting webpage Cloudinary for each review book. With more code optimization and a image database, I believe better page load time can be achieved.

![Page Load Time](/static/images/PingdomResults.png "Page Load Times by Pingdom")

#### Code Validation ####

Code validation is achieve by using developer tools provided by [W3C Developer Tools](https://w3c.github.io/developers/tools/ "W3C Developer Tools Webpage"). The webpage code tested til no errors are found on their checkers.<br>

 __CSS errors are from bootstrap packages.__<br>

![Nu Html Validator](/static/images/NuHtmlChecker.png), ![Internationlization Validator](/static/images/InternationalizationChecker.png), ![Link Validator](/static/images/LinkChecker.png), ![CSS Validator](/static/images/CSSChecker.png).

#### Manual Testing ####

Other testing include:
- Testing creation of user accounts
- Logged In User lock for posting new reviews
- Editing/Deleting can only be done by Original Poster
- Adminstrative Account access and permission to edit/delete/create any review
- All flask redirects to correct pages
- Searching jQuery Ajax Calls to Flask to MongoDB all working and updating front-end properly
- Rating Stars CSS Hover change and display in correlation to the value taken from front-end or MongoDB database

#### Browser Testing ####

The site while being hosted by Heroku Cloud Application Platform is tested on a laptop of 1920x1080 resolution:
- Brave
- Google Chrome
- Firefox
- Microsoft Edge

#### Bugs ####

Mobile repsonsiveness on screens < 350px width are not working as intended. However at 360px width it works fine. This is mainly due to the structure the pages were done with, further optimization of this may resolve this issue. However small screen width size devices are currently the minority of users.<br>

On certain browsers, like Safari, Opera, any non-google friendly browsers will cause JavaScript to not function on old versions of Safari and Firefox Browsers. Some minority browser might cause CSS to not display as intended. However based on [W3School Browser Statics](https://www.w3schools.com/browsers/) in 2020, 80%+ uses Chrome, small number of people uses other browsers.<br>
<br>

## Deployment ##

This project uses Git for version control and hosts the repository for all commits. The depolyed site is hosted by [Heroku -Deployed Site](https://cwy-tgc8-project-3.herokuapp.com/ "Deployed Site")  where it can automatically updated on new commits directly to Heroku Master instead of GitHub.

This project can be accessed via [CollinWuY's Github](https://github.com/CollinWuY/TGC-Project3-DataCentric "Project's Repository") where you can clone/download to your computer directly, or immedaitely view the code via Gitpod. 

All the needed assets, images, fonts, icons, javascript, css are in their respective folders, the main application to run is app.py.

#### Commiting to GitHub ####

Code is commited to GitHub regularly for version control:
- First by creating a Git Repository on GitHub (we are using Code-Institute's Template)
    - Link the IDE to the Git Repository, in this instance opening Gitpod directly from the Github or by type the command `git remote add origin <repository url>`
    - Whenever changes to code is saved, you can stage the changed files with `git add .` for by using the Source Control UI of Gitpod and pressing the plus sign below the text box to add stages
    - Staged content is then commited with a clear defined message with `git commit -m "<msg>"` or by typing in the Source Control UI Tab of Gitpod and pressing the Tick above it
    - The commits are then pushed to the origin GitHub linked to the IDE via `git push -u origin master` or push option in the Source Control UI tab of Gitpod

Deployment to Heroku is performed using command lines:
- Ensure you have requirements.txt file available already, if not use `pip3 install -r requirements.txt`
    - First Install Heroku on your local machine with `sudo snap install heroku --classic`, skip this step if it is already installed
    - Log in into Heroku using `heroku login -i`
    - Create a new app on Herkou `heroku create <app-name>` , as app name needs to be unique throughout the web, it is suggested to put your initials before the app name
    - Verify the remotes that have been added with `git remote -v`
    - Install Gunicorn with `pip3 install gunicorn`
    - Create a `Procfile` (no extenstion) and add in to file the FIRST LINE ONLY `web gunicorn <your main app name without .py>:app`
    - Freeze your imports and dependencies with `pip3 freeze --local > requirement.txt`
    - Finally commit your changes and push to Heroku using `git add.` `git commit -m "<msg>"` then `git push heroku master`
    
#### Setting Up Env For Heroku ####

Head to the [Heroku](https://www.heroku.com/ "Heroku Cloud Application Platform") webpage and login to your dash board
- Choose the correct application you made previously
    - Under the Settings Tab --> Config Vars (Reveal Config Vars)
    - Add in your Var keys like `MONGO_URL` and `SECRET_KEY` and their respective values
    - Click on `Open App` at the navbar above to see your webpage


#### Downloading Locally ####

_Kindly Ensure Your Local IDE has all the required plugin/extensions for Python/Flask/Jinja_

All files can be easily download on the Github site:
1.  At the top right, click on green button under __CODE__
2.  Select last option: Download .zip

![Github Download ZIP](static/images/githubsitedl.png "Download from Github")

3.  Download the .zip file that can be opened with a ZIP unpacker or RAR unpacker 
4.  Unzip the package
5.  Double click the index.html
    -   it should open on your preferred browser.


#### Linking to Local IDE ####

Cloning this repository can be achieve by using the link provided at the Github site:
1. At the top right, click on green button under __CODE__
2. Copy the link provided: `https://github.com/CollinWuY/TGC-Project3-DataCentric.git`

![Github Clone URL](static/images/githubsiteclone.png "Clone URL from Github")

3. In your preferred IDE, Run in terminal `git clone https://github.com/CollinWuY/TGC-Project3-DataCentric.git`
4. Repository will be cloned as a folder on your computer<br>
<br>

## Credits ##

#### Media ####

__DISCLAIMER__<br>
All media images rights belong to the respective companies that own the art. This webpage only displays them for identification and not used for monetary purpose.

- Book Review Images Art are taken from the respective Companies Webpages
- Banner Image is taken via Online Search
- Body Black Wooden Wallpaper is taken from [WallpaperCave](https://wallpapercave.com/w/wp3157716)

#### Icons ####

- All icons are downloaded as SVG from [Font Awesome](https://fontawesome.com/)
- Browser Tab Icon is Logo convertered using [Favicon.io](https://favicon.io/favicon-converter/)

#### Code/Concept ####

- Ratings Star Pure CSS is inspired from [Online Tutorials - Pure CSS Star Rating Widget](https://www.youtube.com/watch?v=Ep78KjstQuw "Youtube Video on Rating Stars Widget")  

#### Fonts ####

- Fonts are taken from Google Fonts; [Google Fonts Medieval Sharp](https://fonts.google.com/specimen/MedievalSharp) and [Google Fonts Monsterrat](https://fonts.google.com/specimen/Montserrat)
<br>
<br>

__THIS WEBSITE IS FOR EDUCATIONAL PURPOSE ONLY - ALL RIGHTS RETAIN BY COLLIN WU YUEWEI__
