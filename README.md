Below is an example README that covers the full project—including the Django backend, the Scrapy scraper, and the Next.js client.

---

```markdown
# Airbnb Scraper & Clone

This project is a full-stack solution for scraping Airbnb listings and displaying them via a Next.js frontend. The project consists of three main parts:

1. **Django Backend with Django REST Framework:**  
   Provides RESTful APIs to insert and retrieve Airbnb listings stored in a MySQL database.

2. **Scrapy Scraper:**  
   Scrapes Airbnb listings (using dummy data for demonstration) and posts the data to the Django backend.

3. **Next.js Frontend with Tailwind CSS:**  
   Displays listings retrieved from the Django backend. Includes a search results page and dynamic listing detail pages.

> **Note:** Real-world scraping of Airbnb is complex and subject to legal and technical restrictions. This project uses simplified dummy data for demonstration purposes.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Django Backend](#django-backend)
  - [Scrapy Scraper](#scrapy-scraper)
  - [Next.js Frontend](#nextjs-frontend)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [CORS & Routing](#cors--routing)
- [Additional Information](#additional-information)
- [License](#license)

---

## Project Structure

```
Airbnb_Scraper/
├── server/                         # Django backend project
│   ├── airbnb_scraper/             # Django project folder
│   │   ├── airbnb_scraper/
│   │   │   ├── __init__.py
│   │   │   ├── settings.py         # Includes MySQL and CORS config
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── scrapper_app/           # Django app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── models.py           # Listing model
│   │   │   ├── serializers.py      # DRF serializer for listings
│   │   │   ├── views.py            # GET and POST endpoints
│   │   │   ├── urls.py
│   │   │   └── migrations/
│   │   │       └── __init__.py
│   │   └── manage.py
├── scraper/                        # Scrapy project folder
│   ├── scrapy.cfg
│   └── scraper/
│       ├── __init__.py
│       ├── items.py                # Defines fields for a listing
│       ├── pipelines.py            # Posts items to Django API
│       ├── settings.py             # Scrapy settings (obeys or disables robots.txt)
│       └── spiders/
│           ├── __init__.py
│           └── airbnb_spider.py    # Scrapes (dummy) Airbnb listings
└── client/                         # Next.js frontend project
    ├── app/
    │   ├── layout.js               # Root layout (includes header/footer)
    │   ├── globals.css             # Global CSS (Tailwind directives)
    │   ├── page.js                 # Search Results page (lists Airbnb listings)
    │   └── listing/
    │       └── [id]/
    │           └── page.js         # Dynamic Listing Detail page
    ├── next.config.js              # Next.js config (CommonJS version recommended)
    ├── package.json
    ├── postcss.config.js
    └── tailwind.config.js
```

---

## Prerequisites

- **Node.js** (v14+ recommended)
- **Python 3.8+**
- **MySQL** (with a database named, for example, `airbnb_db`)
- **npm** or **yarn**

---

## Setup Instructions

### Django Backend

1. **Clone the Repository and Navigate to the Server Folder:**

   ```bash
   cd Airbnb_Scraper/server
   ```

2. **Create a Virtual Environment & Install Dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install django djangorestframework mysqlclient django-cors-headers
   ```

3. **Configure Database & CORS:**

   - In `airbnb_scraper/airbnb_scraper/settings.py`, update the `DATABASES` section with your MySQL credentials.
   - Add `corsheaders` to `INSTALLED_APPS` and configure `CORS_ALLOWED_ORIGINS` to allow `http://localhost:3000`.

4. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Django Server:**

   ```bash
   python manage.py runserver 8000
   ```

### Scrapy Scraper

1. **Navigate to the Scrapy Project Folder:**

   ```bash
   cd Airbnb_Scraper/server/scraper
   ```

2. **(Optional) Adjust Scrapy Settings:**

   - If testing, you can disable `ROBOTSTXT_OBEY` in `scraper/scraper/settings.py`:
     ```python
     ROBOTSTXT_OBEY = False
     ```

3. **Run the Spider:**

   ```bash
   scrapy crawl airbnb_spider
   ```

   The spider uses dummy data and posts the scraped item to `http://localhost:8000/api/add_listing/` via the pipeline.

### Next.js Frontend

1. **Navigate to the Client Folder:**

   ```bash
   cd Airbnb_Scraper/client
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   # or if you prefer yarn:
   # yarn install
   ```

3. **Install Tailwind CSS Dependencies:**

   ```bash
   npm install -D tailwindcss postcss autoprefixer @tailwindcss/postcss
   npx tailwindcss init -p
   ```

4. **Configure Tailwind:**

   - Edit `tailwind.config.js` to include the paths for the `app` and `components` directories.

5. **Ensure Next.js Config Uses CommonJS:**  
   Create a `next.config.js` with the following content:

   ```js
   // client/next.config.js
   module.exports = {
     experimental: {
       appDir: true,  // if supported by your Next.js version
     },
   };
   ```

6. **Run the Next.js Development Server:**

   ```bash
   npm run dev
   ```

   The client should be available at [http://localhost:3000](http://localhost:3000).

---

## Running the Project

- **Backend (Django):**  
  Run on port 8000 with:
  ```bash
  python manage.py runserver 8000
  ```

- **Scrapy Scraper:**  
  In the scraper folder, run:
  ```bash
  scrapy crawl airbnb_spider
  ```

- **Frontend (Next.js):**  
  In the client folder, run:
  ```bash
  npm run dev
  ```

Visit [http://localhost:3000](http://localhost:3000) to see the search results page. Clicking on a listing will navigate to its detail page.

---

## API Endpoints

### GET Listings

- **URL:** `http://localhost:8000/api/listings/`
- **Method:** GET  
- **Description:** Retrieves all Airbnb listings from the database.

### POST Listing

- **URL:** `http://localhost:8000/api/add_listing/`
- **Method:** POST  
- **Description:** Inserts a new listing into the database.
- **Sample Payload:**

  ```json
  {
    "title": "Cozy Apartment in NYC",
    "location": "New York, USA",
    "address": "123 Broadway, New York, NY",
    "price_per_night": 120.0,
    "currency": "USD",
    "total_price": 360.0,
    "image_urls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
    "ratings": 4.8,
    "reviews": 150,
    "description": "A cozy apartment in the heart of NYC.",
    "amenities": ["WiFi", "Kitchen", "Air Conditioning"],
    "host": {"name": "John Doe", "response_rate": "90%"},
    "property_type": "Apartment"
  }
  ```

---

## CORS & Routing

- **CORS:**  
  The Django backend uses `django-cors-headers` to allow cross-origin requests from `http://localhost:3000`.

- **Client-Server Routing:**  
  The Next.js frontend fetches data from `http://localhost:8000/api/listings/` for search results and individual listings. Adjust these URLs when deploying to production.

---

## Additional Information

- **Scrapy Spider:**  
  The spider is configured to scrape dummy data from Airbnb URLs. Adjust the allowed domains and parsing logic for a real-world scenario.

- **Tailwind CSS:**  
  Tailwind is used for styling the Next.js frontend. Global styles and customizations can be added in `client/app/globals.css`.

- **Next.js App Directory:**  
  The project uses the new Next.js App Directory structure (available in Next.js 13+). Dynamic routes for individual listings are located in `client/app/listing/[id]/page.js`.

---

## License

This project is licensed under the MIT License.

---

Happy coding!
