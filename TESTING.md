# Testing Documentation

This website is for Milestone Project 4.
Built with HTML, CSS, JavaScript and Python Django.

To go back to README :point_right: [README.md](README.md)

# Table of Contest

1. [Validation Test](#validation-test)
2. [Responsive Test](#responsive-test)
3. [Manual Test](#links-test)


# Validation Test

## HTML Validator - Test

Naviagate to HTML Validator - [W3C HTML Validator](https://validator.w3.org/) - PASS

* Home page
 1. Select Validate by Url and paste https://mn-unique-shop.herokuapp.com/ - PASS
 2. Click `Check`  - PASS
 3. Result displayed: ![Result](docs/validation/home_html_validation.PNG)

Follow the same steps for: 
* products
    * Url: https://mn-unique-shop.herokuapp.com/products - PASS
    * Result : ![Result](docs/validation/products_html_validation.PNG)

* Contacts
    * Url: https://mn-unique-shop.herokuapp.com/contact/ - PASS
    * error:
    `Stray end tag main: </div>↩</main>↩<foot`
    * Fix issue and `git commit <Fix: message>` and `git push`
    * Reapeat test
    * Result: ![Result](docs/validation/contact_html_validation.PNG)

* Signup
  * Url: https://mn-unique-shop.herokuapp.com/accounts/signup/
  * Result: PASS

* Login
 * Url: https://mn-unique-shop.herokuapp.com/accounts/login/
 * error: 
    `Stray end tag div: /div>↩    </div>↩↩ `
 *   



## CSS Validator - Test

Navigate to CSS Validator - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - PASS

* base.css
 1. Copy and Paste the css code from base.css in the project files in the By direct input tab and click Check
2. Result:

    ![CSS](docs/validation/css.gif)

* toggler.css
 1. Copy and Paste the css code from toggler.css in the project files in the By direct input tab and click Check
 2. Result:

    ![CSS](docs/validation/css.gif)

* checkout.css
 1. Copy and Paste the css code from toggler.css in the project files(checkout/static) in the By direct input tab and click Check
 2. Result:

    ![CSS](docs/validation/css.gif)

## JavaScript Validator - Test 

Navigate to JS Validator  - [JSHint Validator](https://jshint.com/) - PASS

* base.js file

 1. Copy and paste base.js file
 2. Result:
 ![Js hint](docs/validation/js_validation.PNG)

* stripe_elements.js

 1. Copy and paste stripe_elements.js file
 2. Result: Pass
 Comment: Showing 2 undefined variables Stripe 

For toasts messages javascript code:

1. Copy and paste js code from base template
2. Result: PASS

For preventing form to resubmit review:

1. Copy and paste js code from product_details template
2. Result: PASS

## Python PEP8 Validator - Test

Navigate to [PEP8 Validator](http://pep8online.com/) - PASS

For cart:
1. Copy and paste code from :
    * admin.py - PASS
    * contexts.py - PASS
    * models.py - PASS
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
2. Result: PASS on all files

For checkout:
1. Copy and paste code from :
    * admin.py - PASS
    * forms.py - PASS
    * models.py - PASS
    * signals.py
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
    * webhook_handler.py - PASS
    * webhooks.py - PASS    
2. Result: PASS on all files

For contact:
1. Copy and paste code from :
    * admin.py - PASS
    * forms.py - PASS
    * models.py - PASS
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
2. Result: PASS on all files

For home:
1. Copy and paste code from :
    * admin.py - PASS
    * models.py - PASS
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
2. Result: PASS on all files

For products:
1. Copy and paste code from :
    * admin.py - PASS
    * forms.py - PASS
    * models.py - PASS
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
2. Result: PASS on all files

For profiles:
1. Copy and paste code from :
    * admin.py - PASS
    * forms.py - PASS
    * models.py - PASS
    * test.py - PASS
    * urls.py - PASS
    * views.py - PASS
2. Result: PASS on all files

For unique_shop:
1. Copy and paste code from :
    * urls.py - PASS
    * settings - Comment:
    Errors for auto generated fields:
    ![settings.py](docs/validation/settings.PNG)
2. Result: PASS on all files

Python files in main directory:

1. Copy and paste code from :
    * custom_storages.py - PASS
    * manage.py
2. Result: PASS on all files


# Responsive Test

|Screen size\Browser |Chrome            |Opera             |Edge              |Firefox           |Safari            
|--------------------|------------------|------------------|------------------|------------------|------------------| 
|Mobile              |:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|Tablet              |:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|Not Tested        |
|Desktop             |:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

The website was tested on a varied number of devices:
### For Mobiles:
* Android - Samsung Galaxy S10 (screen size - 6.1-inch) on Chrome, Opera, Firefox and Microsoft Edge
* IOS - iPhone 7 (screen size - 4.7-inch) on Safari and Chrome
* IOS - iphone Pro 12 (screen size 6.1-inch) Safari adn chrome
### For Tablet:
* Surface Book in tablet view - Chrome, Opera, Firefox, Edge (screen size - 13.5- inch)
### For Desktop:
* PC Windows (Windows 10):
  1. Surface Book on (screen size - 13.5-inch)
  2. Surface Book on the second monitor DELL U2419H(screen size - 24-inch)
  3. Huawei matebook D15(screen size 15.6-inch)  
   
  Tested on  Chrome, Opera, Firefox and Microsoft Edge
* MacBook pro 13:
  * Tested on Safari and Chrome browser.

  
Friends and family were asked to test this website. After receiving feedback from them some minor responsive issues were addressed like increment and decrement value not visible on mobile screens bellow 400px.


Test responsiveness of website on all screen sizes using Chrome browser: 
Steps taken:
 1. In google chrome browser go to http://mn-unique-shop.herokuapp.com/
 2. Right click on the page content and inspect
 3. Click and drag the responsive window down to 350px and up to max 2400px. 
 4. Repeat on all site pages.

Comments: No issues noticed from 350px screen sizes.

# Manual Test

### Navbar links:
Steps:
- Navigate to http://mn-unique-shop.herokuapp.com/
- Checking all links working - PASS
- All links for logged out users tested - PASS 
- All links for not logged user tested - PASS
- Checking if relevant links are visible for logged in and logged out users - PASS
Repeat steps on all pages - PASS
### Buttons links:


    Checking if all buttons from all pages working - PASS

### Footer:
    Checking if footer is sticking to the bottom on the relevant pages - PASS

### Content:

    Checking on each site if relevant content is displayed for all pages.

- For logged in users - PASS
- For not logged users - PASS

## Cart

### Adding to cart

    Checking if correct items are added to shopping cart:

Steps:

- Navigating to http://mn-unique-shop.herokuapp.com/products
- Selecting product without colour and adding to cart - PASS
- Checking if correct toast message is displayed - PASS
- Value bellow basket icon in navbar added correct value - PASS
- Clicking on the cart and checking if item in the cart - PASS
- Reapeting this process for items with different colours and adding them to the cart - PASS

### Updating cart

- after update the correct toast message doisplayed - PASS
- the total and grand total of the product change accordingly - PASS
- the qunatity of items was updated correctly - PASS
