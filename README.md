# AMSCoreProject
This repository hosts an e-commerce web application created using Flask, tailored for an online guitar store. The platform allows users to easily explore and buy a range of products, handle their shopping carts, and complete orders. The application is built using Flask's web framework and utilizes SQLAlchemy to manage the database.

Technologies Used

The application was developed using a combination of the following technologies:

HTML: Used for structuring the content and layout of web pages.
CSS: Employed to style and enhance the visual presentation of the application.
Python: The core programming language utilized for backend logic and server-side operations.
SQLite: Employed for database management and storage of essential application data.
Features

All Listings:
Explore a comprehensive array of products presented on the main page, providing easy access to various store sections.

Fender:
Delve into the Fender category to discover a range of Fender guitars, explore their specifications, and effortlessly add preferred items to your cart.

Gibson:
Browse through the Gibson category to explore a selection of Gibson guitars, delve into detailed item information, and conveniently place chosen products in your cart.

About:
Learn more about our online store through the About page, where we provide insights into our background, mission, and values.

Contact:
Connect with us via the Contact page, where you can find our contact details and reach out for any inquiries, feedback, or assistance.

Cart:
Review the items in your cart, make adjustments to quantities if needed, and proceed seamlessly to the checkout stage to complete your purchase.

Payment:
Experience a simulated payment process with our Payment feature. Input your payment details to successfully finalize your order and ensure a smooth and secure transaction.

Individual Guitar Listing:
Explore detailed information about a specific guitar by visiting its dedicated listing. Discover its unique features, specifications, and images, and easily navigate to add it to your cart or proceed with the purchase.

Database Models:
Customer: Represents customer information, including first name, last name, and email.
Product: Defines product details, such as name, make, description, price, and image URL.
Order_Template: Stores temporary order details, including customer ID, product ID, and quantity.
Order_for_post: Captures order information for final processing, including customer details, product ID, quantity, and delivery information.

Route Handling:
Utilizes Flask's route decorators to define various endpoints.
Handles requests for the homepage, about, contact, product listings (Fender and Gibson), cart, individual guitar listings, payment, and order processing.
Database Management:
Utilizes SQLAlchemy to manage the application's SQLite database.
Defines data models for customers, products, and orders.
Creates and commits entries to the database during order processing.
Dynamic Templating:
Utilizes Jinja2 templating engine to dynamically render HTML templates.
Displays product information, cart contents, and order details based on user interactions.
User Interaction:
Allows users to explore products, add items to the cart, and proceed to checkout.
Captures user input for customer and order information.
Server Configuration:
Runs the application using the Flask development server.
Configures the server to run in debug mode and listens on all available network interfaces.
The application provides a comprehensive e-commerce experience, allowing users to browse, shop, and complete orders seamlessly.

I begun planning this project by creating user stories and virtualising them with a Kanban board in JIRA:

JIRA: Kanban Board - User Stories:


1. As a visitor to the website, I want to see a visually appealing home page, so I can quickly understand the purpose of the site and navigate to other sections.

2. As a shopper, I want to be able to view a list of available products on the product listing page, so I can browse and explore the items for sale.

3. As a shopper, I want each product on the product listing page to have a dedicated page with detailed information, so I can learn more about the product before making a decision to purchase.

4. As a shopper, I want the ability to view products by category on the category page, making it easier for me to find items that match my interests.

5. As a shopper, I want a dedicated cart page where I can see all the products I've added, modify quantities, and proceed to the checkout page.

6. As a shopper, I want to see a summary of my cart on the checkout page, and be able to enter my shipping information before proceeding to payment.

7. As a shopper, I want a secure and easy-to-use payment page where I can enter my payment details (name, card number, expiry date, CVC) and complete the purchase.

8. As a shopper, I want a contact us page with store information, including the store's address, phone number, and an email contact form, so I can reach out with inquiries or feedback.

9. As a shopper, I want an about us page that provides information about the store's mission, history, and the team behind the store, giving me confidence in the products I'm buying.

10. As a shopper, I want the website to maintain a consistent look and feel across all pages, ensuring a pleasant shopping experience.

11. As a shopper, I want the website to be mobile-responsive, so I can browse and shop comfortably on any device.

12. As a shopper, I want the website to load quickly, reducing wait times and ensuring I can explore products efficiently.

13. As a store administrator, I want to be able to update the product catalog, including adding new products, updating prices, and managing stock quantities.

14. As a store administrator, I want to be able to categorize products, ensuring a well-organized shopping experience for users.

15. As a store administrator, I want to receive and manage customer inquiries and feedback submitted through the contact us page.

<img width="1440" alt="Screenshot 2023-08-16 at 15 56 56" src="https://github.com/AlexanderBonfield/AMSCoreProject/assets/125991084/852d1603-fef2-4f3c-bab8-0015e0e9d97c">







