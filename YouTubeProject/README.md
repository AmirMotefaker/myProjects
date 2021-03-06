**How To Build a YouTube Comment Bot**

**Table of Contents:**

    Step #0: Overview

    Step #1: Install Selenium

    Step #2: Open Youtube site

    Step #3: Login with a username and password

    Step #4: Enter a search term

    Step #5: Click on a video

    Step #6: Enter a comment

    Step #7: Go back

    Step #8: Put it all together

Step #0: Overview

**Important: When running a selenium bot against a site like Youtube, it’s important to simulate human behavior to avoid being detected and banned. Therefore, adding pauses when typing or clicking is crucial to replicating what a user would do.**


Step #1: Install Selenium

You can install selenium executing the following command from your terminal:

            pip install selenium
            
To use selenium you also need a driver, which is basically a browser. You could just use your already installed browser or download a driver. I would recommend downloading a driver to avoid messing up your browser settings. You can download a driver following the link below:

Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/chromium.org/driver/)

Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox: https://github.com/mozilla/geckodriver/releases


Step #2: Open Youtube site

The first step is opening the youtube site:

    [www.youtube.com.](https://www.youtube.com/)

To open youtube with your bot, you will need to create a new python script and add the following code:

    from selenium import webdriver

    browser = webdriver.Chrome('./chromedriver')

    browser.get("https://www.youtube.com")
    
 **Note: Please note that your python script and the chrome driver file should be in the same folder.**


Step #3: Login with a username and password

signing in to Youtube. Signing in consists of five simple tasks:

    Typing your email

    Clicking next

    Typing the password

    Click next

    Sometimes clicking on confirm, although this step is not always needed.
    
    
Step #4: Enter a search term

In this step, we define how to enter a search term into the search box. To do so, we will create a function passing in the browser and the search term.
    
    
Step #5: Click on a video

Therefore all we need to do at this point is selecting one of the videos and click. We could select one random video, or alternately select the first one, and follow the list order.


Step #6: Enter a comment

Once our browser opens the video page, we can insert our comment. To enter a comment, we need to do the following:

    Move to the comment input field

    Click on the component, so it gets the focus.

    Type our comment

    Press the “Comment” button
    
    
Step #7: Go back

So far our bot has opened a video and enter a comment. We will need to go back to the video list and click on the next video. We can achieve that easily press the back button in the browser. In Selenium, we can go back to the previous page using the following code:

     browser.execute_script("window.history.go(-1)")
     
     
Step #8: Put it all together

At this point, we have some code in our bot script containing functions that will log in to youtube, enter a search term in the search box and enter a comment. The last step is connecting all the pieces.


