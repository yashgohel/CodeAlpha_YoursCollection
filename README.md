# Yours-Collection

Yours-Collection is a full-featured e-commerce web application built with Django. It serves as an online storefront, allowing administrators to manage products and users to browse, purchase, and manage their orders.

## About The Project

This project is a demonstration of a modern e-commerce platform. It includes functionalities for both customers and administrators. The frontend is designed to be responsive and user-friendly.

### Key Features

*   **User Authentication:** Secure user registration and login system.
*   **Product Management:** Admins can add, update, and delete products through a dedicated interface.
*   **Product Catalog:** Users can browse through a grid of available products.
*   **Shopping Cart:** Persistent shopping cart for users to add and manage items.
*   **Checkout Process:** A multi-step checkout process including shipping information.
*   **Order History:** Users can view their past orders in their profile.
*   **Responsive Design:** The UI is adapted for desktop, tablet, and mobile devices.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.8+
*   pip
*   Git

### Installation & Setup

1.  **Clone the repo**
    ```sh
    git clone https://github.com/yashgohel/CodeAlpha_YoursCollection
    cd CodeAlpha_YoursCollection
    ```

2.  **Create and activate a virtual environment**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file should be created by running `pip freeze > requirements.txt`)*

4.  **Apply database migrations**
    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser** (to access the admin panel)
    ```sh
    python manage.py createsuperuser
    ```

6.  **Run the development server**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## How to Use the Website

1.  **Register/Login:** Start by creating a new account or logging in if you already have one.
2.  **Admin: Add Products:**
    *   Navigate to `/adminpage`.
    *   Fill out the form to add new products with names, descriptions, prices, and images.
    *   The new products will appear on the home page.
3.  **User: Browse and Shop:**
    *   On the home page (`/`), you can see all the products.
    *   Click "Add to Cart" on any product you wish to buy.
4.  **Shopping Cart:**
    *   Navigate to `/cart` to view the items in your cart.
    *   You can adjust quantities or remove items.
5.  **Checkout:**
    *   From the cart, proceed to checkout.
    *   Fill in your shipping details on the `/shipping` page.
    *   Confirm your order to complete the purchase.
6.  **View Profile/Orders:**
    *   Go to `/profile` to see your user information and order history.
