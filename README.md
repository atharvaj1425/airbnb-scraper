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

