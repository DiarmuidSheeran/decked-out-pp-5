# Decked Out

![Responsive Design](documentation/responsive/am-i-responsive.png "responsive-design")

## A Trading Card Game E-commerce Store
> A trading card game e-commerce store that sells products for both the YuGiOh! TCG and thE Pokemon TCG

### - Created by Diarmuid Sheeran

## Click the link below to view the live site:
>  [Decked Out's Live Site](https://decked-out-tcg-store-b1147b8f9a0a.herokuapp.com/)

## Table of Contents
1. [Decked Out](#decked-out)
2. [Site Description](#site-description)
    - [Business Model](#business-model)
        - [Business Overview](#business-overview)
        - [Site User](#site-user)
        - [Goals for the Website](#goals-for-the-website)
        - [Marketing Strategy](#marketing-strategy)
    - [SEO](#seo)
3. [Implementing the Agile Approach](#implementing-the-agile-approach)
    - [The Agile Aproach](#sites-agile-approach)
    - [Link to User Stories](#user-stories-link)
4. [Project Design](#project-design)
    - [UX](#ux)
        - [Colour Pallete](#colour-pallete)
        - [Wireframes](#wireframes)
        - [Database](#database)
5. [Site's Look and Features](#sites-look-and-features)
    - [Home](#home)
    - [User Verification](#user-verification)
    - [User Profiles](#user-profiles)
    - [Store](#store)
    - [Product Details](#product-details)
    - [Create and Edit Products](#create-and-edit-products)
    - [View Product Statistics](#view-product-statistics)
    - [Create Discount Codes](#create-discount-codes)
    - [Send Newsletters](#send-newsletters)
    - [FAQ's](#faqs)
    - [View Contact Form Submissions](#view-contact-form-submissions)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [Checkout Success and Order History](#checkout-success-and-order-history)
    - [Responsive Design](#responsive-design)

6. [Testing](#testing)
7. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Other Technologies](#other-technologies)
8. [Deployment](#deployment)
9. [Future Features](#future-features)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Site Description
* The goal of Decked out is to be an e-commerce store that allows users to purchase YuGioh and Pokemon products. 
* The site allows users to create their own account, sign in and logout.
* Authenticated users have their own profile pages that shows there order history, wishlisted products and can add default delivery information. Every logged in user can also upldoad their own profile picture to personalise their profile.
* The site allows users to interact with products by adding/removing them from their own personal wishlists. Site users can also leave reviews on products they have previously purchased.
* Users can view the stores best sellers, promotion, clearnece and new arrival products on the home page with the addition of being able to sign up for the sites newsletter.
* The site contains a products page that allows users to view all of the products in the store at once or if they so wish they can shop by sorting by either YuGiOh! or Pokemon products.
* Users have the ability to delete their account, deleting all of their information.
* Users can add, edit quantities or remove products from their shopping bag.
* The site allows users to enter a discount code to save money on their orders also site users can securly checkout using the stripe payment network. On successful completion of an order the user is emailed a copy of their order-confirmation.
* The Admin of the site is given control over creating/editing their own products and also have the abillity to view product stastics, create discount codes, send newsletters, and view contact form submissions. The Admin also has the ability delete products. 
* The site was created for the Code Institutes PP5 to demonstrate an agile apporach to creating a functioning e-commerce website.
### Business Model
#### Business Overview
Decked Out is a B2C e-commerce platform specializing in trading card games, specifically Yu-Gi-Oh! and Pokémon. Our goal is to become the go-to destination for enthusiasts and collectors alike, offering a wide range of products through our online store.

Products:

Decked Out will offer a diverse selection of Yu-Gi-Oh! and Pokémon trading card game products, including booster packs, starter decks, accessories, and merchandise. Our pricing structure will range from low to medium to high end, catering to both casual players and serious collectors.

Benefits for the Business Owner:

1. Scalability: The online platform allows for easy scalability as the business grows. We can expand our product offerings and reach new markets without the constraints of a physical location.

2. Global Reach: By operating online, Decked Out can cater to customers globally, tapping into the worldwide trading card game community.

3. Low Startup Costs: Starting an e-commerce store requires relatively low initial investment, allowing us to allocate more resources towards customer acquisition, such as advertising and marketing campaigns.

4. Impulse Buying: The affordable price point of our products encourages impulse buying, attracting customers who may be considering purchasing trading card game products.

Cons of the Business Model:

1. Customer Acquisition: Initial customer acquisition may be challenging due to saturation in the trading card game market. We'll need to implement a robust marketing strategy to stand out from competitors and attract customers.

2. Brand Building: Establishing a strong brand presence takes time and effort. Immediate results are unlikely without a well-planned marketing strategy focused on building brand awareness and credibility.

3. Trust and Loyalty: Without a physical storefront, building trust and loyalty with customers may be more challenging. Offering discounts, promotions, and excellent customer service will be essential in establishing a loyal customer base.

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)


#### Site User:
Decked Out's typical site users are trading card game enthusiasts, predominantly male, aged between 12 and 40, who have a passion for collecting and playing Yu-Gi-Oh! and Pokémon trading card games. They are likely to be avid fans of the respective franchises and enjoy engaging with the community surrounding these games.

User 1:

* The primary user demographic for Decked Out includes males aged between 12 and 40 who are         passionate about trading card games like Yu-Gi-Oh! and Pokémon. These users are likely to have a deep interest in collecting rare cards, building competitive decks, and participating in tournaments and events within the trading card game community.

User 2:

* In addition to the primary user demographic, partners of trading card game enthusiasts may also visit Decked Out to purchase gifts for them. These users may not be as familiar with trading card games but are seeking products and accessories that would make ideal gifts for their loved ones who are passionate about Yu-Gi-Oh! and Pokémon.

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

#### Goals for the Website:
Decked Out aims to create an intuitive and user-friendly online platform with the following goals:

1. Seamless Navigation: Ensure the website is easy to navigate, allowing users to quickly find the products they're looking for and proceed to checkout effortlessly.

2. Product Satisfaction: Provide users with a diverse range of authentic Yu-Gi-Oh! and Pokémon trading card game products that meet their expectations in terms of quality and authenticity.

4. Efficient Checkout Process: Enable users to complete transactions swiftly and securely, enhancing the overall shopping experience.

5. User Profiles: Allow users to create profiles where they can view past orders, update their information, and manage their preferences within a wishlist of products.

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)


#### Marketing Strategy:
Decked Out's marketing strategy focuses on reaching and engaging with its target audience effectively:

1. Social Media Promotion: Utilize platforms like Facebook to promote the store, engage with users, and encourage sharing and interaction within the trading card game community.

2. Soft Launch Sale: Host a soft online launch sale to attract early adopters and incentivize initial purchases from prospective customers.

3. Email Marketing: Collect subscribers through the site and send out emails of offers, promotions, and updates to encourage repeat business.

4. Paid Advertising: Consider using paid advertising channels such as Google Ads and Facebook Ads to target the desired demographic and drive traffic to the site, focusing on high-performing ad campaigns.

5. Influencer Partnerships: Depending on budget, collaborate with influencers within the trading card game niche to promote Decked Out's products to their audience, leveraging their influence to increase brand visibility and attract potential customers. Target influencers with a following of at least 10k in the trading card game community for optimal reach and engagement.

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

### SEO
#### SEO Project Planning for Decked Out:
Upon finalizing the decision to establish Decked Out as a trading card game store, the focus shifted towards devising an effective SEO strategy to enhance the visibility and reach of the online platform. The following steps were undertaken to plan the SEO project:

1. Research and Analysis: Utilized Google Trends to identify popular search terms within the trading card game community. Additionally, employed SEO Quake to analyze competitors' strategies and identify areas of strength.

2. Keyword Research: Conducted comprehensive keyword research using Wordtracker.com, leveraging a trial subscription to maximize insights. Compiled a list of both short-tail and long-tail keywords tailored to the trading card game niche.

Keywords:
Short-tail - Yu-Gi-Oh!, Pokémon TCG, Trading Card Games, Booster Packs, Starter Decks, Collectible Cards, Card Sleeves, Deck Boxes, Tournaments, Online Store
Long-tail - Rare Yu-Gi-Oh! cards for sale, Pokémon TCG booster packs online, Best deals on trading card game accessories, Competitive deck building tips, Yu-Gi-Oh! tournament strategies

1. Keyword Implementation: Strategically integrated the short-tail and long-tail keywords across the Decked Out website to optimize content relevance and improve search engine rankings. These keywords were strategically placed in page titles, meta descriptions, headers, and throughout product descriptions.

2. HTML Tag Optimization: Ensured proper utilization of HTML tags, including the strong tag where appropriate, to emphasize key phrases and improve readability for search engine crawlers. Additionally, ensured that all internal and external links were accurately described to enhance user experience and SEO performance.

By implementing a strategic SEO plan tailored to the trading card game niche, Decked Out aims to enhance its online presence, attract qualified traffic, and establish itself as a leading destination for Yu-Gi-Oh! and Pokémon enthusiasts.

#### Sitemap.xml
I generated a sitemap for the site so that once ready engines like google can search it effectively.

#### Robots.txt
I generated a robots.txt file so that google could crawl the site. I have blocked off the accounts app as there is no benefit for google to crawl those pages.

#### Sites Favicon:
For the site, I used the back of a Yu-Gi-Oh! card as the favicon to add a touch of authenticity and resonate with the trading card game theme.

#### Facebook Business page:
Below is a link to the sites Business page:
> [Decked Out's Business Facbook Page](https://www.facebook.com/profile.php?id=61556460457145)

Facebook tends to find and take down fake business sites. In the eventuality of this happening, below is a screenshot of the store business Facebook page as proof of creation.
<details>
<summary></summary>

>![Responsive Design](documentation/facebook/facebook-screenshot.png "responsive-design")
</details>

<br>

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Implementing the Agile Approach
### Sites Agile Approach
#### To ensure an organized and flexible development process for the Decked Out e-commerce project, I have adopted an Agile methodology. Here are the steps I've taken to implement this approach:
* I started by defining the project's scope and objectives. I identified the core functionalities and features that would be essential for the e-commerce store.
* Each major feature or functionality was expressed as a epic, which was broken down into multiple user stories written from the perspective of an end-user or an admin user. For example: "As a shopper I want to be able to view a list of products and select some to purchase."
* I converted each epic and user story into a GitHub issue. Each issue includes a clear description of the feature, its tasks, and any relevant details. I assigned labels such as "Must Have", "Should Have" to indicate priority.
* I created a Kanban board with four columns: "To Do," "In Progress," "Done," and "Nice to Have." This board serves as the projects task management indicator.
* This approach ensured I was tackling one epic's user story set of related issues at a time. This allowed me to deliver working functionality in increments as to not get distracted and finish the targeted task.
* The project could allow collaboration among team members if needed. Each issue was assigned to me but could be assigned to other team members if the project was a team project.
* As issues are started they are moved to the "In Progress" column, and when they are completed they are moved to the "Done" column.

**By following this Agile approach, I have aimed to deliver a high-quality, user-focused e-commerce site to meet user expectations and deliver a compelling online experience.**

### User Stories Link
> [Link to Epics and User Stories Board](https://github.com/users/DiarmuidSheeran/projects/8/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D)

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Project Design:
### UX
#### Colour Pallete
<details>
<summary></summary>

I have incorporated a carefully selected color palette throughout the website, aimed at creating a visually appealing design, allowing for a more streamlined and user-friendly experience.
>![Color Pallete](documentation/color_pallete/color-pallete.png "color-pallete")
</details>

#### Wireframes

<details>
<summary></summary>

With the idea for the website planned, I began creating wireframes to depict a more narrowed down outlook for how the differnet pages depending on functionality should look throught the site:
>![Wireframe Shell](documentation/wireframes/wireframe-shell.png "wireframe-shell")
>![Wireframe Home](documentation/wireframes/wireframe-home.png "wireframe-home")
>![Wireframe Products](documentation/wireframes/wireframe-products.png "wireframe-products")
>![Wireframe Products](documentation/wireframes/wireframe-profiles.png "wireframe-profiles")
>![Wireframe Cart](documentation/wireframes/wireframe-cart.png "wireframe-cart")
>![Wireframe Checkout](documentation/wireframes/wireframe-checkout.png "wireframe-checkout")
</details>

#### Database
<details>
<summary></summary>
The project relies on a PostgreSQL database hosted on ElephantSQL. Its web interface features a convenient SQL query console. The Database URL, inclusive of the API key, is securely stored as an environment variable within the Heroku platform.

<br>
Below you can find the database schema for the site:

>![Database Schema](documentation/database/database-schema.png "database-schema")
</details>

<br>

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Site's Look and Features

### Home
<details>
<summary></summary>

#### Home and Navigation

The top section includes a navigation bar with links to different product categories such as All Products, YuGiOh, Pokémon, and Special Offers. A prominent search bar allows for quick product searches. The website header highlights Free Delivery on Orders Over €50 and includes access to the user account and cart, with a clear display of the cart's current value.

The main content area showcases featured products and promotions through visually appealing banners and product slideshows. It is divided into sections for Best Sellers, Promotions, Clearance Products, and New Arrivals, each with its selection of relevant products in a slideshow.

Each product is presented with an image, name, and price, some with labels like Special Offer or Clearance.

A newsletter sign-up form is also available, inviting visitors to subscribe with their name and email address.

The footer is divided into several sections:
Contact Us provides the physical address of for the store, an email contact, and social media links.
Social Links directs to the Facebook page of the store.
FAQ includes helpful links for customer service aspects such as the Cookie Policy, About Us, Returns Policy, and Contact Us.
Site Navigation gives a structured list of links to navigate the website, including Home, Shop, Cart, and account-related features.


![Home](documentation/site_features/home-one.png "home-one")

![Home](documentation/site_features/home-two.png "home-two")


[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### User Verification
<details>
<summary></summary>

#### Registration Page

The registration page features a welcoming message "Welcome to Decked Out! Register below" with an arrow pointing to the form fields. It offers a straightforward process for creating a new user account. The form requires the user's email address, email confirmation, a chosen username, and password (entered twice for confirmation). Below the sign-up button, there's a prompt for users who already have an account to sign in, enhancing user navigation.

![register](documentation/site_features/register.png "register")

#### Login Page

On the login page, users are greeted with "Welcome to Decked Out! Sign in below" and an image of a Poklemon, adding a touch of familiarity and brand consistency. The form asks for the username or email and password. There's a "Remember Me" checkbox for convenience, and a "Forgot Password?" link for account recovery. The page also provides a direct link back to the home page for easy access.

![login](documentation/site_features/login.png "login")

#### Logout Page

The logout page is minimalist, providing a clear message "Are you sure you want to sign out?" with options to confirm sign out or cancel and return to the home page.

![logout](documentation/site_features/logout.png "logout")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### User Profiles
<details>
<summary></summary>

#### Overview

The user profile page of the store is a personalized dashboard that provides users, and admins, with a range of functionalities to manage their account and administrative tasks. Note the admin tools is only available and visable to store owner and users with adminstrative rights.

Upon logging in, the admin user is greeted with a personalized message, "Hi, Boss! You are logged in as an admin (name)", if you are an admin of the site or "Hello, (name)!, EXPLORE YOUR PROFILE OPTIONS BELOW, which adds a friendly touch to the user interface. The profile picture section allows for a customized image upload, enhancing the personalization of the users experience.

![user profile one](documentation/site_features/user-profile-one.png "user-profile-one")

#### Default Delivery Information, Wishlists and Order History

The second image showcases the user's default delivery information section, where personal address details can be entered and updated.

Adjacent to this is the Wishlist panel, which displays a list of products that the user has added to there wishlist. This feature provides a convenient way for users to keep track of desired items and offers potential for targeted marketing and reminders.

On the right side of the wishlist is the Order History section. This panel provides a detailed list of past orders, including order number, date, items purchased, and order total. This comprehensive overview allows users to track their purchase history and facilitates easy reordering or reference to past transactions.

![user profile two](documentation/site_features/user-profile-two.png "user-profile-two")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Store
<details>
<summary></summary>

#### Products Page

The products page of the store is a vibrant and organized catalog displaying a variety of YuGiOh and Pokemon trading card game products. It's designed to be user-friendly, allowing customers to easily browse and add items to the shopping bag.
The page displays a total of "33 Products" as indicated at the top, with items presented in a grid layout. Each product card includes an image, name, price, and the option to add the item to a wishlist, showcasing the site's interactive features. The products are encased in red borders, which helps to differentiate each item and adds to the overall aesthetic.
Each product card has a clear, easy-to-use quantity selector and an "Add to Bag" button, simplifying the purchasing process.

![products page](documentation/site_features/products-page.png "products-page")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Product Details
<details>
<summary></summary>

#### Products Details

The product details page on the site is designed to provide a comprehensive look at individual items available for purchase. It is both informative and user-friendly, catering to potential buyers.

The page also caters to those with admin status as it allows an admin to delete the product or edit it.

The page features a clean layout with a large image of the product on the left, and a detailed description and purchase options on the right. The design maintains the site's consistent theme with a red and black color scheme.

Below the product description and purchase options, there is a section for Product Reviews. While there are no reviews yet, the page prompts the user with the message "We see that you have purchased this product. Would you like to leave a review?" This interactive feature encourages customer engagement and feedback. This message only applies to customers who have bought the product and is disabled for users who have already left a review.

![products details](documentation/site_features/products-details.png "products-details")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Create and Edit Products
<details>
<summary></summary>

#### Add/Edit Product

The Product Management - Add page is a dedicated interface for admins to add new products to the stores inventory. The page is designed for ease of use, with clear input fields and options.
When a user navigates to an edit product page the fields are pre filled with the products information and can the fields can be edited to 

![create products](documentation/site_features/create-products.png "create-products")

The admin Products page serves as a control panel for administrators to manage existing products. It lists all the products in a table format, allowing for quick edits.
The layout is straightforward, listing products with an ID and Name, along with their Price and Action that can be taken. The page maintains the website's theme with a black and red color scheme.

![admin products](documentation/site_features/admin-products.png "admin-products")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### View Product Statistics
<details>
<summary></summary>

The Product Statistics page on Decked Out serves as an analytical tool for adminis to track sales performance. The interface is divided into two main sections: the Product Sales Record and the Recommended for Promotion area.
The left section of the page is dedicated to the Product Sales Record. This segment provides a detailed list of products with corresponding images, sales data, and purchase frequency. It allows admin users to sort products via the drop-down menu.

The right section, titled Recommended for Promotion, identifies products with a poor sales record that may benefit from additional marketing or discounts. Each product in this section includes a product image, the total sold, and the number of times purchased.

![product statistics](documentation/site_features/product-statistics.png "product-statistics")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Create Discount Codes
<details>
<summary></summary>

#### Create Discount Code

The Discount Code Creation page is a specialized adminis interface within the site designed for creating promotional codes that customers can use to obtain discounts.

The page is split into two primary sections:

Create Discount Code: This area occupies the left side of the screen and is where new discount codes are generated.
Current Discount Codes: On the right side, it lists all active discount codes, providing a quick reference for existing promotions.

![discount code create](documentation/site_features/discount-code-create.png "discount-code-create")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Send Newsletters
<details>
<summary></summary>

#### Newsletter

The Newsletter Sending page is an admin tool within the Decked Out platform that facilitates communication with customers through sending an email newsletters. This feature is crucial for marketing, customer engagement, and updates.
The page design is simple and open to further customization in the future. The page has a structure for composing and sending a newsletter. It matches the site's overall color scheme of red, black, and white, maintaining the sites consistency.

The admin user can send an email with to subcribers with an email:

Subject: A text field at the top for the admin to input the subject of the newsletter.

Content: A larger text area below the subject field, providing space to compose the main body of the newsletter.

![newsletters](documentation/site_features/newsletters.png "newsletters")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### FAQ's
<details>
<summary></summary>

#### About us

The About Us page is an informational section on the Decked Out website, detailing the store's mission, the value it offers to customers, and reasons to choose its services. It presents a welcoming and professional narrative that highlights the company's passion for trading card games and commitment to customer satisfaction.

![about us](documentation/site_features/about-us.png "about-us")

#### Cookies Ploicy

The Cookies Policy page provides users with information about how cookies are used on the site website. It explains what cookies are, their purpose for remembering login status, analyzing traffic, and customizing user experience. The page outlines users' choices regarding cookie management through their browser settings and invites users to contact the store for any concerns about the cookies policy.

![cookies policy](documentation/site_features/cookies-policy.png "cookies-policy")

#### Returns Policy

The Returns Policy page outlines the terms and conditions under which purchases can be returned. It details the eligibility criteria for returns, such as the item being in its original packaging and unused condition, and the process for submitting return requests within a specific time frame.

![returns policy](documentation/site_features/returns-policy.png "returns-policy")

#### Contact Us

The Contact Us page is a customer service feature designed to facilitate communication between the customers and the store. It includes a simple form where customers can submit their inquiries. The form fields include:

* Name
* Email
* Category of inquiry
* Message text area

![contact us](documentation/site_features/contact-us.png "contact-us")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### View Contact Form Submissions
<details>
<summary></summary>

#### Admins contact form submissions page view

The admin contact form submissions view page is a dedicated section on the site where admins can review messages sent by customers or visitors through the site's contact form.

![contact form submission views](documentation/site_features/contact-form-submission-views.png "contact-form-submission-views")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Shopping Bag
<details>
<summary></summary>

#### Shopping Bag

The Shopping Cart page on the site offers customers a clear and concise summary of their selected items before proceeding to checkout.

The page keeps with the website's overall aesthetic, featuring a simple and clean layout. The color scheme of red, black, and white and the cart is organized for ease of review and modification.

* Product Info: This section displays the product's name along with an image and the SKU number for reference.

* Price: The individual price of the product is listed beside the product info.
* Quantity: Customers can adjust the quantity of the product they wish to purchase with a plus and minus button, and clicking the update button.
* Remove: There's an option to remove the item entirely from the cart if the customer changes their mind.
* Subtotal: The subtotal for each product line is displayed, providing clarity on the cost of each type of item in the cart.

On the right side, the cart summary includes:

* Bag Total: The total price of the items currently in the cart.
* Grand Total: The final amount to be paid, which includes additional charges or discounts. It also prompts the customer that they could get free delivery by spending just a little more, incentivizing further purchases.

![cart](documentation/site_features/cart.png "cart")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Checkout
<details>
<summary></summary>

#### Checkout

The checkout page of the site is where customers can finalize their purchases. It's designed to provide a summary of the items in the cart, calculate totals, and gather payment and delivery information.

The customers can enter:

* Personal Information: Customers are prompted to enter their full name, email, and contact number.
* Delivery Address: There is a series of fields for address details, including street, city, and postal code.
* Payment Information: A secure field for entering credit card details is provided, though the 

The right hand side shows the customer:

* Product Listing: Shows an image and description of the product(s) being purchased.
* Pricing Details: Displays the price, quantity, and subtotal for each item.
* Promotional Code: There's an option to enter a discount code, with an "Apply Code" button next to it.
* Order Totals: A breakdown of the order total, including any discounts applied and the delivery fee, leading to the grand total.

![checkout one](documentation/site_features/checkout-one.png "checkout-one")

The second image shows the checkout process after a discount code has been applied:

* Discount Acknowledgment: The page acknowledges the applied discount code "gift" and indicates the amount saved.
* Adjusted Pricing: The order total is adjusted to reflect the discount, with the new grand total prominently displayed.
* Remove Discount Option: There's a feature to remove the discount if the customer decides not to use it.

![Checkout Two](documentation/site_features/checkout-two.png "checkout-two")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Checkout Success and Order History
<details>
<summary></summary>

#### Checkout Success/Order History

The Checkout Success page is the final confirmation step of the customers shopping experience, reassuring the customer that their order has been successfully processed.

The page provides a detailed summary of the order, including:

* Order Number: A unique identifier for the customer's transaction.
* Order Date: The exact date and time when the order was placed.
* Order Details: Lists the item(s) purchased, with quantity and price per item.
* Discounts (if applicable): If a discount code was applied, it shows the code used and the percentage of the discount.
* Delivery Information: The full name and address to which the order will be delivered.
* Billing Information: A breakdown of the order total, showing any discounts applied, delivery charges, and the grand total paid.

A confirmation email is sent to user on successfull completion of an order.

The User can also access this page in the future by checking their order history in their profile.

![checkout success](documentation/site_features/checkout-success.png "checkout-success")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

### Responsive Design
<details>
<summary></summary>

#### Responsive Design Approach

Key features of the responsive design include:

* A compact navigation bar that collapses into a hamburger menu, making it easy to access different sections of the site without overcrowding the screen.
* Prominent display of special offers, such as the "Opening Special" with the discount code 'GIFT', which remains clearly visible even on a smaller display.
* The main branding elements, like the Decked Out logo and the Pokémon banner, are resized appropriately to fit within the confines of a mobile screen while still maintaining their visual impact.
* Product images and descriptions in the "Best Sellers" section are scaled down to fit the mobile format without sacrificing detail, ensuring that the products are still attractively presented.
* Calls to action, such as the "Shop Now" button, are prominently placed and sized for easy tapping with a finger, which is critical for the mobile shopping experience.

The mobile-responsive design of the site is to demonstrates a commitment to accessibility and a good user experience across different devices. It allows users to interact with the site effectively.

![mobile one](documentation/site_features/mobile-one.png "mobile-one")
![mobile-two](documentation/site_features/mobile-two.png "mobile-two")

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)
</details>

<br>

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Testing
### Link to testing.md file
>  [Testing Markdown Link](https://github.com/DiarmuidSheeran/decked-out-pp-5/blob/main/TESTING.md)

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Technologies Used:
### Languages:
<details>
<summary></summary>

* HTML5
* CSS
* Javascript
* Python
</details>

### Frameworks:
<details>
<summary></summary>

* Django
* Bootstrap
</details>

### Other Technologies:
<details>
<summary></summary>

* [AWS S3 and IAM](https://aws.amazon.com/?nc2=h_lg)- Used to host static and media files for this project and IAM for the permissions based roles for accessing the S3 buckets.
* [Gitpod](https://www.gitpod.io/)- For writing and test code
* [GitHub](https://github.com/)- For hosting the source code
* [Git](https://git-scm.com/)- Used for version control throughout the project and to ensure a good clean record of work done was maintained. 
* [Heroku](https://id.heroku.com/)- Used for deploying the project
* [Elephant Sql](https://customer.elephantsql.com/)- Used for hosting the database
* [Fontawesome](https://fontawesome.com/)- Used for icon within the site
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)- Used for testing the site
* [W3C Markup Validation Service](https://validator.w3.org/)- Used to validate the html
* [W3C CSS Validation Service(Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_input)- Used for validating the css
* [PEP8 linter](https://pep8ci.herokuapp.com/)- Used for validating the python code
* [Js hint](https://jshint.com/)- Used for validating the javascript code
* Microsoft Paint was used in the making of the wireframes and the databases schema.
</details>

<br>

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Deployment
### **Cerate Django app**
<details>
<summary></summary>

    1. Install Django and gunicorn: pip3 install django gunicorn
    2. Install supporting database libraries dj_database_url and psycopg2 library: pip3 install dj_database_url psycopg2
    3. Create file for requirements: pip freeze --local > requirements.txt
    4. Create project: django-admin startproject project_name
    5. Create app: python3 manage.py startapp app_name
    6. Add app to list of installed apps in settings.py file: 'app_name'
    7. Migrate changes: manage.py migrate
    8. Run the server to test if the app is installed: python3 manage.py runserver
</details>

### **Create Database**
<details>
<summary></summary>

    1. Navigate to elephant sql site.
    2. Login or sign up
    3. Create a new instance
    4. Give your plan a Name (this is commonly the name of the project)
    5. Select the Tiny Turtle (Free) plan
    6. Select your region
    7. Create instance
    8. Copy the database url
</details>

### **Link database to site**
<details>
<summary></summary>

    1. Back in your project comment out the default database in settings.py 
    2. Add following code: DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    3. Create an env.py file and add the following code: os.environ["DATABASE_URL"] = ('your_url')
    4. Replace your_url with the database url copied from elephant sql
    5. In your settings.py file follow the same steps to hide your secrect key within the env file
    6. Make the migrations to the database: python3 manage.py makemigrations
    7. Migrate Changes: python manage.py migrate
</details>

### **Create Procfile**
<details>
<summary></summary>

    1. Create Procfile
    2. Add the following code: web: gunicorn deckedout .wsgi
</details>

### **Create Heroku app**
<details>
<summary></summary>

    1. Navigate to heroku.com & log in
    2. Click "new" and create a new App
    3. Give the application a name and then choose your region and Click "Create app"
    4. On the next page click on the Settings tab to adjust the settings
    5. Click on the 'config vars' button
    7. Add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
    8. Navigate to Deploy section of github
    9. To connect with github select github and confirm
    10. Search for your repository select it and click connect
    11. Click manual deployment which deploys the current state of a branch. (DO NOT DEPLOY code with debug turned on)
</details>

### **How to clone of the repository:**
<details>
<summary></summary>

    1. Navigate to the "Code" tab located under the repository name.
    2. Click on the "Code" button situated to the right above the listed files.
    3. Click on the clipboard icon to copy the URL of the repository.
    4. Open Git Bash in Gitpod or your preferred IDE.
    5. Change the working directory to your desired location for the cloned directory.
    6. Use the command git clone followed by pasting the copied URL.
    7. Press enter to complete the cloning process.
    8. In the terminal, install the necessary requirements by executing: pip3 install -r requirements.txt.
    9. Next, create the env.py file to define project variables.
    10. Add the env.py file to a .gitignore to prevent it from being pushed to GitHub.
    11. Generate migrations by running: python manage.py makemigrations.
    12. Apply those migrations with: python manage.py migrate.
    13. To launch the project, type python manage.py runserver in the terminal and access it locally via port 8000.
    14. This will open the project locally, allowing you to begin working on it.
    15. Optionally, consider forking the repository on GitHub for collaborative development.
</details>

### **Forking the repository on GitHub**
<details>
<summary></summary>

    1. Login to github and find the respitory (linked below)
    2. Under your profile photo on the right hand side you will see the fork button.
    3. Click the fork button and github will create a copy to your account.
>  [Decked Out's Github Repository](https://github.com/DiarmuidSheeran/decked-out-pp-5)
</details>

<br>

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Future Features

After the grading process, I envision creating some enhancements to my e-commerce platform that will elevate the user experience and drive engagement. 

* Firstly, I aim to implement a more sophisticated newsletter template, designed to captivate users' attention and deliver personalized content tailored to their interests. This will involve incorporating dynamic elements and leveraging data analytics to optimize newsletter effectiveness.

* Additionally, I plan to introduce a robust messaging system to streamline communication with users, particularly in response to contact form submissions. This feature will enable prompt and efficient resolution of inquiries and feedback, enhancing customer satisfaction and fostering positive interactions.

* To foster customer loyalty and incentivize repeat purchases, I intend to develop a points-based loyalty program. Users will earn points for transactions, which can be redeemed for discounts or exclusive rewards, thereby cultivating a loyal customer base and driving sales.

* Expanding on our discount code options, I aim to introduce a variety of new codes, including fixed-rate discounts and free delivery codes, in addition to the existing percentage-based discounts. This will provide users with more flexibility and choice when redeeming promotions, further enhancing their shopping experience.

* Lastly, I aim to enhance the product options system for administrators, enabling them to manage product variations, such as different card sets, rarities, and conditions, more comprehensively. This will empower administrators to provide users with a diverse range of choices and ensure accurate product representation on the platform.

[Back to Top](#table-of-contents) | [Jump to Credits](#credits)

## Credits

1. **Books**
    * [Python Crash Course for Begginers](https://www.amazon.co.uk/Python-Crash-Course-2nd-Edition/dp/1593279280/ref=sr_1_3?crid=1NT3V3JDTP1FO&keywords=python+programming+for+beginners&qid=1699623185&sprefix=python%2Caps%2C51&sr=8-3)

    * [Django 3 By Example third edition](https://www.amazon.co.uk/Django-Example-powerful-reliable-applications/dp/1838981950/ref=sr_1_2?crid=TAF89G4S8IY1&dib=eyJ2IjoiMSJ9.cCwPhr961_YSYkz3ppvf1BAflFg5qHa8O6kmMOT4XRf1VSRoOG1QeXU5ICFLzBg3JJc2XgCed-15QXezh03-ivAA_xSw3vbzDGu05P5sY8wRJllMj8VnTx-jF7z5CLkKwf_e3s0IdIO4zwz6UuvXNE7rxT1CufUPuuYJdivtcSZ8Rpgaq-Nhc164363mT8uvxdOtY6ei1ZAScPNrYVh4zJFhTdZTWm6RS2WP1k7VHLY.CVy7NirQpWPCelLq7jDlS_rSayfIoLshu5Aui4rar5k&dib_tag=se&keywords=django+by+example&qid=1708474722&sprefix=django+by+example%2Caps%2C47&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)

2. **Online Resources**
    * [Code Institutes Course Content](https://codeinstitute.net/ie/)

    * [W3 School](https://www.w3schools.com/)

    * [Stackoverflow](https://stackoverflow.com/)

    * [Bootstrap](https://getbootstrap.com/)

    * [Coolors](https://coolors.co/)

    * [Codemy's Online Courses](https://codemy.com/)

    * [Django Documentaion](https://docs.djangoproject.com/en/5.0/)

3. **Video Resources**
    * [Codemy Django e-commerce](https://www.youtube.com/playlist?list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50)

    * [Dennis Ivy's Django Tutorial Youtube Playlist](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)

    * [Dennis Ivys Django e-commerce tutorial](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)

4. **Images**
    * [Yugioh Product Images](https://www.yugioh-card.com/en/)
    * [Pokemon Product Images](https://www.pokemoncenter.com/)


[Back to Top](#table-of-contents)

## Acknowledgements

* I extend my most sencire gratitude to my course leader, **Alan Bushell**, for his invaluable support and guidance throughout the project and the year.
His insightful suggestions and unwavering assistance were instrumental in steering the project to successful completion. Thank you sincerely for your contribution.

* I extend my sincere appreciation to the **tutor support team at the Code Institute** for their exceptional assistance throughout the past year. Their unwavering dedication in resolving issues and, most importantly, aiding in my comprehension of challenging concepts has been invaluable. Thank you for your unwavering support and guidance.

* I am immensely grateful to the dedicated team at the **Code Institute** for their unwavering support and the wealth of valuable content provided over the past year. Your commitment and expertise have been invaluable on this journey. Thank you for your continuous support.

[Back to Top](#table-of-contents)