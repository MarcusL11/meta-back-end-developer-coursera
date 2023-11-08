# Current Status

- I should test first if I can authenticate a Employee or Customer with via the auth/token/login method using Djoser
- I will need to create models for Employees, Customers, and Groups for the users on the platform.
-

# Project Criteria

In this project, your APIs need to make it possible for your end-users to perform certain tasks and your reviewer will be looking for the following functionalities.

1. The admin can assign users to the manager group

2. You can access the manager group with an admin token

3. The admin can add menu items (DONE)

4. The admin can add categories (DONE)

5. Managers can log in (DONE)

6. Managers can update the item of the day (DONE)

7. Managers can assign users to the delivery crew

8. Managers can assign orders to the delivery crew

9. The delivery crew can access orders assigned to them

10. The delivery crew can update an order as delivered

11. Customers can register

12. Customers can log in using their username and password and get access tokens

13. Customers can browse all categories

14. Customers can browse all the menu items at once

15. Customers can browse menu items by category

16. Customers can paginate menu items

17. Customers can sort menu items by price

18. Customers can add menu items to the cart

19. Customers can access previously added items in the cart

20. Customers can place orders

21. Customers can browse their own orders

You'll also need to give feedback on and grade the assignments of two other learners using the same criteria.

# Scope of Project

## Using Pipenv

[Creating Django Project using Pipenv](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/sn2Ez/video-subtitles)

## Function or class-based views

You can use function- or class-based views or both in this project. Follow the proper API naming convention throughout the project. Review the video about
[Function- and class-based views](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/4BASB/video-subtitles)
as well as the video about [Naming conventions](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/1jSCM/video-subtitles).

## User Groups

[User Roles ](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/12F4H/video-subtitles)

## Error Check

| HTTP Status Code | Reason                                                    |
| ---------------- | --------------------------------------------------------- |
| 200 OK           | For all successful GET, PUT, PATCH and DELETE calls       |
| 201 Created      | For all successful POST requests                          |
| 403 Forbidden    | If authorization fails for the current user token         |
| 401 Unauthorized | If user authentication fails                              |
| 400 Bad Request  | If validation fails for POST, PUT, PATCH and DELETE calls |
| 404 Not Found    | If the request was made for a non-existing resource       |

## API End points

Here are all the required API routes for this project grouped into several categories.

User registration and token generation endpoints
You can use Djoser in your project to automatically create the following endpoints and functionalities for you.

| Endpoint               | Role                                      | Method | Purpose                                                                     | My Status |
| ---------------------- | ----------------------------------------- | ------ | --------------------------------------------------------------------------- | --------- |
| `/api/users`           | No role required                          | POST   | Creates a new user with name, email and password                            | Done      |
| `/api/users/users/me/` | Anyone with a valid user token            | GET    | Displays only the current user                                              | Done      |
| `/token/login/`        | Anyone with a valid username and password | POST   | Generates access tokens that can be used in other API calls in this project | Done      |

## Djoser

[djoser end poitns](https://www.coursera.org/learn/apis/lecture/bldmJ/introduction-to-djoser-library-for-better-authentication)

## Menu-items endpoints

| Endpoint                     | Role                    | Method                   | Purpose                                                       | My Status |
| ---------------------------- | ----------------------- | ------------------------ | ------------------------------------------------------------- | --------- |
| `/api/menu-items`            | Customer, delivery crew | GET                      | Lists all menu items. Return a 200 – Ok HTTP status code      | Done      |
| `/api/menu-items`            | Customer, delivery crew | POST, PUT, PATCH, DELETE | Denies access and returns 403 – Unauthorized HTTP status code | Done      |
| `/api/menu-items/{menuItem}` | Customer, delivery crew | GET                      | Lists single menu item                                        | Done      |
| `/api/menu-items/{menuItem}` | Customer, delivery crew | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized                                    | Done      |
| `/api/menu-items`            | Manager                 | GET                      | Lists all menu items                                          | Done      |
| `/api/menu-items`            | Manager                 | POST                     | Creates a new menu item and returns 201 - Created             | Done      |
| `/api/menu-items/{menuItem}` | Manager                 | GET                      | Lists single menu item                                        | Done      |
| `/api/menu-items/{menuItem}` | Manager                 | PUT, PATCH               | Updates single menu item                                      | Done      |
| `/api/menu-items/{menuItem}` | Manager                 | DELETE                   | Deletes menu item                                             | Done      |

## User group management endpoints

| Endpoint                                   | Role    | Method | Purpose                                                                                                                                                | Status |
| ------------------------------------------ | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| `/api/groups/manager/users`                | Manager | GET    | Returns all managers                                                                                                                                   | Done   |
| `/api/groups/manager/users`                | Manager | POST   | Assigns the user in the payload to the manager group and returns 201-Created                                                                           | Done   |
| `/api/groups/manager/users/{userId}`       | Manager | DELETE | Removes this particular user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found | Done   |
| `/api/groups/delivery-crew/users`          | Manager | GET    | Returns all delivery crew                                                                                                                              | Done   |
| `/api/groups/delivery-crew/users`          | Manager | POST   | Assigns the user in the payload to delivery crew group and returns 201-Created HTTP                                                                    | Done   |
| `/api/groups/delivery-crew/users/{userId}` | Manager | DELETE | Removes this user from the delivery crew group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found      | Done   |

## Cart management endpoints

| Endpoint               | Role     | Method | Purpose                                                                                         | My Status |
| ---------------------- | -------- | ------ | ----------------------------------------------------------------------------------------------- | --------- |
| `/api/cart/menu-items` | Customer | GET    | Returns current items in the cart for the current user token                                    | Done      |
| `/api/cart/menu-items` | Customer | POST   | Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items | Done      |
| `/api/cart/menu-items` | Customer | DELETE | Deletes all menu items created by the current user token                                        | Done      |

## Order

| Endpoint                | Role          | Method     | Purpose                                                                                                                                                                                           | My Status |
| ----------------------- | ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `/api/orders`           | Customer      | GET        | Returns all orders with order items created by this user                                                                                                                                          | Done      |
| `/api/orders`           | Customer      | POST       | Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user. | Done      |
| `/api/orders/{orderId}` | Customer      | GET        | Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.                                                       | Done      |
| `/api/orders`           | Manager       | GET        | Returns all orders with order items by all users                                                                                                                                                  | Done      |
| `/api/orders/{orderId}` | Manager       | PUT, PATCH | Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.                                                              | Done      |
| `/api/orders/{orderId}` | Manager       | DELETE     | Deletes this order                                                                                                                                                                                | Done      |
| `/api/orders`           | Delivery crew | GET        | Returns all orders with order items assigned to the delivery crew                                                                                                                                 | Done      |
| `/api/orders/{orderId}` | Delivery crew | PATCH      | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.                                             | Done      |

## Additional step

Implement proper filtering, pagination and sorting capabilities for /api/menu-items and /api/orders endpoints. Review the videos about
[Filtering and searching](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/h7QUx/video-subtitles)
and [Pagination](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/mEYFj/video-subtitles)
as well as the reading [More on filtering and pagination](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/supplement/oCL3M)

## Throttling

Finally, apply some throttling for the authenticated users and anonymous or unauthenticated users. Review the video
[Setting up API throttling](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/rPE4B/video-subtitles)
and the reading [API throttling for class-based views](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/supplement/1h6WO) for guidance.
