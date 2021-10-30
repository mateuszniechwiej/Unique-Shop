# Testing Documentation

This website is for Milestone Project 4.
Built with HTML, CSS, JavaScript and Python Django.

To go back to README :point_right: [README.md](README.md)

# Table of Contest

1. [Validation Test](#validation-test)
2. [Responsivnes Test](#responsivnes-test)
3. [Manual Test](#manual-test)


# Validation Test

### HTML Validator - Test

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



### CSS Validator - Test

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

### JavaScript Validator - Test 

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

### Python PEP8 Validator - Test

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
