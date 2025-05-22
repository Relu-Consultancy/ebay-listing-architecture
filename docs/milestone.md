# 📘 Project Milestones Documentation

---

## 🧱 Milestone 1: Develop Basic Application

This milestone establishes the core architecture of the application and integrates eBay API connectivity.

### 1.1 User Management

* Implement user registration and authentication system
* Role-based access control (Admin, Editor, Viewer)
* User profile management (update, delete)
* Password reset and email verification

### 1.2 eBay OAuth Integration

* Integrate eBay OAuth 2.0 authentication flow
* Handle secure token storage and refreshing
* Link eBay accounts to internal users

### 1.3 Category Management

* Fetch eBay categories via Taxonomy API
* Cache categories locally
* Provide UI to browse and select categories

### 1.4 Listing Management

* Build CRUD interface for eBay listings
* Integrate with eBay Trading API to push/pull listings
* Track status (draft, active, ended, etc.)

### 1.5 eBay API Client SDK Development

* Develop an internal SDK to encapsulate eBay API logic
* Support modular services (categories, listings, etc.)
* Implement logging and retry mechanisms

### 1.6 Docker Setup

* Dockerize backend and frontend services
* Create Docker Compose configuration for local development
* Include services like PostgreSQL and Redis
* Ensure reproducible local environments

### 1.7 CI/CD Pipeline Setup 
* Choose CI/CD platform (e.g., GitHub Actions, GitLab CI)
* Set up workflow for automated testing, build, and deployment
* Integrate Docker build and push steps
* Add environment-based deployment stages (dev, staging, prod)

---

## 🧩 Milestone 2: Develop Default Values Engine

This milestone builds a configurable system to auto-populate and manage data values for listings.

### 2.1 Default Value Template

* **Template Builder**

  * UI to create reusable templates for item specifics, shipping, return policy, etc.
* **Template Association**

  * Link templates to categories or users
* **Pre-fill Logic**

  * Automatically apply default values during listing creation

### 2.2 Custom Variables

* **Variable System**

  * Define placeholders like `{{brand}}`, `{{condition}}`
* **User-Defined Logic**

  * Allow advanced users to create rules for how variables populate
* **Storage**

  * Scoped per user or global

### 2.3 Dynamic Variables

* **Dynamic Runtime Replacement**

  * Variables resolved at runtime using listing context
* **AI/Rules Integration**

  * Integrate logic to resolve variables based on category or past data
* **Examples**

  * `{{auto_title}}` → "Marvel Spider-Man #1 (2021) – NM"

---

## 📦 Milestone 3: Bulk Upload & Comic Mapping Integration

Supports mass management of eBay listings via file-based or interactive uploads.

### 3.1 CSV/Excel Upload

* **Parser**

  * Upload and parse `.csv` or `.xlsx` files
* **Mapping UI**

  * Map file columns to listing fields
* **Error Handling**

  * Show validation results before processing

### 3.2 Batch Processing

* **Queue System**

  * Use Celery or similar to handle batch jobs
* **Progress Tracking**

  * Display upload status per row
* **Retry Logic**

  * Retry failed uploads with logs

### 3.3 Template Integration

* **Default Value Templates**

  * Use pre-defined templates in bulk uploads
* **Smart Suggestions**

  * Suggest mappings based on historical uploads

---

## 🧠 Milestone 4: AI Integration

Add intelligence to the application to assist users in creating and managing listings effectively.

### 4.1 Title & Description Generator

* **AI-Powered Suggestions**

  * Generate eBay-optimized titles and descriptions
* **Prompt Customization**

  * User-defined tone, style, keywords
* **Multilingual Support**

  * Translate descriptions for different markets

### 4.2 Smart Defaults & Autocomplete

* **AI Variable Filler**

  * Predict values for missing fields (e.g., item specifics)
* **Learning Engine**

  * Learn from previous listings to improve suggestions

### 4.3 Image & Category Detection (Optional)

* **Image Tagging**

  * Extract labels from images using vision models
* **Category Recommender**

  * Suggest best-fit categories using AI

### 4.4 AI Error Detection

* **Review Assistant**

  * Warn about missing or incorrect fields before submission
* **Listing Score**

  * Rate listing quality with tips for improvement
