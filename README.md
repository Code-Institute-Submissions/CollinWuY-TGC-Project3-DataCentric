# TableTop Six - Communal tabletop rpg book review site #

### TGC - Data Centric Development Milestone Project 3 ###
By: **Collin Wu Yuewei** -- *Code Institute Batch 8* -- 
##### Made with Python/Flask and MongoDB ######

The intent of this webpage is to be a communal forum for enthusiast to share they review on books from their favourite tabletop rpg series. Giving basic information about he books, the cost, where to get them and what to expect.
##### Home Page Preview ####
![Website Preview Image](/static/images/proj3Home.png "Where to Park Website Homepage")
##### Book Review Info Preview ####
![Website Preview Image](/static/images/proj3Book.png "Where to Park Website Search Page")
##### Footer of Page Preview ####
![Website Preview Image](/static/images/proj3Footer.png "Where to Park Website Search Page")


## Aim ##
The goal of the project is to build an data centric site with Python language with Flask framework and MongoDB to present useful information drawn from different user input via CRUD, using techonology and languages taught in the Code Institute Fullstack Web Developer Program; at Project 3, namely HTML, CSS, JS, Python, Flask, MongoDB.

__The concept chosen for this project is to create a communal book review website for enthusiast to share they review on books from their favourite tabletop rpg series. To become a resource or reference for others who might want to jump into the hobby, or looking for information__ 

The problem is that there are too many series of such tabletop rpgs, books are typically found at the main publisher's webpage at a mint condition price. While at amazon, you are able to obtain used copies for cheaper and a consolidated area for finding different books from different genres/series.

## Demo ##

The full website demo can be previewed here: [Tabletop Six Webpage](https://cwy-tgc8-project-3.herokuapp.com/)

Responsive is tested using [Am I Responsive?](http://ami.responsivedesign.is/?url=https://cwy-tgc8-project-3.herokuapp.com/): 
<br> 
![Responsive Demo on Various Devices](/static/images/amiresponsive.png "Website Responsiveness Preview")
<br>

## UX ##

The target audience for this website are for people who are drivers that are on the move. Whom are going to packed locations such as malls, events...etc or are stuck in carpark queues.  

The website concept is mainly to be a clean and simple interface, where the only actions are either text-box, icons or buttons. Removing the "barrier to learn", allowing any new user to pick-up and use immediately.

This project was a mobile first and a single hand operation design in mind. It has to fill the screen and have sufficiently large fonts for pleasant viewing and accessiblity. A big striking blue Call-To-Action button right in the middle of the screen that accesses the GPS capability of modern day high-tech phones. Allowing pin-point accuracy to the current location.

Obvious blue car icons are dotted on the map as locations of carparks in the zone and have pop-ups to give essential information to the user. The available carpark is the largest of the information and is color coded depending of the current availability parking slots in relations to the total slots available at the carpark.

By hiding pages and only display the relevant page at 100% viewport, no scrolling is required to gain full access to information.

A secondary text-box search is located below the Call-To-Action button on the homepage and top-left beside the return to homepage icon on the map page to allow destination planning, re-locating the center of scanning or when GPS locator is unavailable.

On larger devices, more fanciful click-to-expand location summary table is available to view all locations in the zone and their available carpark slots at a go.
<br>
![Information Summary Table](assets/images/summarytable.png "Information Summary Table")

## Features ##
- Full 100% Viewport per page to focus the user's attention
  <br>
- Single Website, All Pages Design for minimal loading of links or other pages 
  <br>
- 3-5sec Loading Page for allowing all API data retrievial to be completed preventing interruptions on usage
  <br>
- Loading page will store a reload value into localstorage, that then stops the refreshing webpage of setTimout on the second load 
  <br>
- Combining data from different API into a JSON, allowing data from multiple sources with a linking value
- <br>
- Quick Access Call-to-Action button that use GPS/Geolocation to determine location
  <br>
- Color-coded information for better UX
  <br>
- Loading Page (_Page0_)
  - Animated circle movements to indicate loading of the webpage and intuitively let the user know to let it load for a few seconds
  - Loads faster the first time accessing and hides on loaded
  <br>
- Homepage  (_Page1_)
  - Striking blue Call to Action Button
  - Secondary Text-box option as backup if GPS/Geolocation not available or for pre-planning destination
  - Hides on either GPS or Text-box search call to give precendence to map page
  <br>
- Interactive Map (_Page2_)
  - Local Singapore Map with Detailed road names, locations and points of interest
  - A 500m blue circle zone to limit search, allowing focusing of user experience to the most important information around them. (_No one wants to walk 1km to their location if carpark is too far_)
  - Cute blur car icons with informative pop-ups for cleaner viewing
  - Color-coded percentage parking slots to emphasize on urgency to get parking
  - Quick summary table for larger screens for all carparks in the zone
  - Quick Search Text-box for location change and return to Homepage Icon on top-left 
  <br>

### Features Left to Implement ###

- More information from different API sources, example: Parking Cost/hr, Mall/Event parking capacity, etc...
- More robust data retrieval, to encompass all carparks available on top of current HDB carparks
- GPS guiding system to plan routes to chosen carpark
- ADs system for monetization, allowing future growth
- Convert to Android or iOS, making it an App (modern)

## Technologies Used ##

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
    - Makes coding way easier than base JavaScript
* [Leaflet JS](https://leafletjs.com/ "Leaflet JS Maps Homepage")
    - Interactive Maps with Pop-up and Markers
    - Boundary setting for precise data display
* [oneMap API](https://www.onemap.sg/home/ "oneMap Homepage")
    - Singapore Local Information with detailed Map of roads, places of interest, rails, malls
    - Consolidated information on carpark location and details
* [Data Gov SG](https://data.gov.sg/ "DataGovSG databases Homepage")
    - Singapore's Open source database with frequently updated information
    - Availabiliy of Carparks slots tracking due to automated gantry carparks
* [Git](https://git-scm.com/ "Installation for Git Support")/[Github](https://github.com/ "Github Homepage")
    - For version control and commits to Github
* [VSCode IDE](https://code.visualstudio.com/ "VSCode IDE Homepage")
    - Local IDE for coding HTML/CSS/JavaScript
    - Extensions used:
      - HTML CSS Support
      - HTML CSS Snippets
      - IntelliSense for CSS
      - JS-CSS-HTML Formatter
      - Live Server (Preview)
      - BootStrap 4, FontAwesome 5 Free
      - Markdown All in One
      - Mardown Preview Enhanced
      - Prettier - Code Formatter

## Testing ##

#### Responsiveness ####
The webpage was manual tested for responsiveness on physical iPhone 6S, Samsung S8+, Xiaomi Mi Max2, 1920 x 1080 laptop screen.

Due to the unavailability of localstorage on reponsiveness testing webpages like  [Responsiveness Tool](http://responsivetesttool.com/ "Responsiveness Tool Homepage")  or  [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?id=07L3WeU_nndVYwaUTleP7w "Mobile Friendly Test Homepage")  or [Am I Responsive Design](http://ami.responsivedesign.is/ "Am I Responsive Design Homepage"), I was unable to show responsiveness without disabling the loading page. Therefore the best way fo testing responsiveness was with Google Inspector as shown at the Demo section above.

All platforms had to have correct CSS design, working animation, buttons, pop-up and elements placed in the correct position.

#### Page Load Time ####

The page load time is tested using [Pingdom Tool](https://tools.pingdom.com/ "Pingdom Homepage") while being hosted by GitHub Pages. This is vital and important as the goal was to have a responsive, non-laggy webpage with no link-loading from page to page, achieving an __B__ rating of __82/100__ points also on Asia, America and European Servers. With more code optimization, I believe better page load time can be achieved.

![Page Load Time](/assets/images/pingdom.png "Website Responsiveness Preview")

#### Code Validation ####

Code validation is achieve by using developer tools provided by [W3C Developer Tools](https://w3c.github.io/developers/tools/ "W3C Developer Tools Webpage"). The webpage code tested til no errors are found on their checkers. __CSS errors are from bootstrap and leaflet js packages.__<br>
![Nu Html Validator](/assets/images/nuhtmlchecker.png), ![Internationlization Validator](/assets/images/internationlizationChecker.png), ![Link Validator](/assets/images/linkchecker.png), ![CSS Validator](/assets/images/csschecker.png).

#### Manual Testing ####

Other testing include:
- Testing GPS location accuracy with Mobile Phones
- Checking data is correct for each marker location
- Ensuring data retrieval successful
- Map/Page and markers reset on new search
- Limiting data retreival to reduce lag, but implementing a circle boundary, markers only in boundary
- Icon button testing and displaying of correct data
- Ensuring coded color for available carparks reflect correctly
- Taking into consideration the website UX, ensuring quick responsiveness and no lag

#### Browser Testing ####

The site while being hosted by Github Pages is tested on a laptop of 1920x1080 resolution:
- Brave
- Google Chrome
- Firefox
- Microsoft Edge

#### Bugs ####

Due to the async nature of JavaScript, API retrieval success is highly dependant on the responsiveness of the API source. Resulting in slower API retrieval as compared to other functions in the code. Even on a loading page with refresh, sometimes API retrieval can fail. This can be rectified by just refreshing the page.

Leaflet js popups when markers are click also function slower then other functions, leading to the need to set a timeout color-change and comparison codes. Giving a sudden change of details once the popup is seen, instead of being instantly in the correct color and format. Current solution is to use a seTimeout.

The loading screen is active and refreshes every 3 sec. Using localstorage, by inputing a variable and checking if it exist, we can break this reset cycle. However on first loading it takes twices as long to refresh and does not work on sub-servers or pages that do not allow localstorage, leading to endless refreshing.

On certain browsers, like Safari, JavaScript may not function on old versions of Safari and Firefox Browsers. However based on [W3School Browser Statics](https://www.w3schools.com/browsers/) in 2020, 80%+ uses Chrome, small number of people uses other browsers.

## Deployment ##

This project uses Git for version control and hosts the repository for all commits. It is linked to my local VSCode IDE. The depolyed site is hosted by Github Pages where it can automatically updated on new commits.

This project can be accessed via [CollinWuY's Github](https://github.com/CollinWuY/TGC-Project2) where you can clone/download to your computer directly, or immedaitely view the code. 

All the needed assets, images, videos, fonts, icons, javascript, css are in their respective folders, the main site is named index.html.

#### Downloading Locally ####

All files can be easily download on the Github site:
1.  At the top right, click on green button under __CODE__
2.  Select last option: Download .zip

![Github Download ZIP](assets/images/githubsitedl.png "Download from Github")

3.  Download the .zip file that can be opened with a ZIP unpacker or RAR unpacker 
4.  Unzip the package
5.  Double click the index.html
    -   it should open on your preferred browser.


#### Linking to Local IDE ####

Cloning this repository can be achieve by using the link provided at the Github site:
1. At the top right, click on green button under __CODE__
2. Copy the link provided: `https://github.com/CollinWuY/TGC-Project2.git`

![Github Clone URL](assets/images/githubsiteclone.png "Clone URL from Github")

3. In your preferred IDE, Run in terminal `git clone https://github.com/CollinWuY/TGC-Project2.git`
4. Repository will be cloned as a folder on your computer

## Credits ##

#### Media ####

- Background Image is by Andrey Kirov and downloaded from [Unsplash](https://unsplash.com/photos/i7qsJX0Ym44 "Unsplash Webpage for Andrey Kriov Carpark Image")
- Singapore detailed map is fron [oneMap](https://www.onemap.sg/home "oneMap Homepage")
- Details for carparks is from [oneMap](https://www.onemap.sg/home "oneMap Homepage") and [Data Gov SG](https://data.gov.sg/dataset/carpark-availability "Data Gov SG Site")

#### Icons ####

- All icons are downloaded as SVG from [Font Awesome](https://fontawesome.com/)
- Browser Tab Icon is Logo convertered using [Favicon.io](https://favicon.io/favicon-converter/)

#### Code/Concept ####

- Loading page pure css ring loader is of [DHINTECH - Pure CSS Loader UX](https://www.youtube.com/watch?v=CQ--dXUvvVA "Youtube Video on Pure CSS Loader UX")  

#### Fonts ####

- Fonts are inbuilt in VSCode IDE with Google Fonts; Google Fonts Verdana and Google Fonts Georgia
<br>
<br>

__THIS WEBSITE IS FOR EDUCATIONAL PURPOSE ONLY - ALL RIGHTS RETAIN BY COLLIN WU YUEWEI__


## Database Planning ###

Tabletop books review site community
Public can see all records
Public can send in new records
Only OP can edit past records
Only Users can leave ratings
Only Users can leave comments

Records to be browsed by categories
Records have Image
Records have Name
Records have Author
Records have Year of Publish
Records have Price (Amazon, etc...)
Records have Reviews ( 5Stars)
Records have Comments

```
category
{
    "name":
    "books": [],
    "review_average":
    "comments":
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
}
```

https://www.youtube.com/watch?v=Ep78KjstQuw Rating Stars