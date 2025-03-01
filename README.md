# Stock Guru AI

Stock Guru AI is an advanced stock market analysis and investment platform powered by AI. It provides detailed stock analysis reports, investment insights, and interactive charts to help users make informed decisions. The platform features a Django backend with Jinja templating for the frontend and an admin dashboard to manage stock requests and reports.

## Features

### User Features:
- **Stock Analysis & Investment Reports**: Generate professional stock analysis and investment insights.
- **Historical Reports**: Users can view previously generated reports.
- **Interactive Charts**: Visualize stock trends with real-time data.
- **User Profiles**: Each user has their own profile to track past stock requests and reports.

### Admin Features:
- **Admin Dashboard**: Manage all user stock requests and generated reports.
- **User Management**: View and manage users' activities.
- **Report Monitoring**: Track stock analysis and investment reports generated by the system.

## Tech Stack

### Frontend:
- **HTML, CSS, Bootstrap** – Simple, responsive UI with Jinja templating.

### Backend:
- **Django** – Robust, scalable backend with built-in admin functionality.
- **Django Rest Framework (DRF)** – API development for seamless data handling.
- **PostgreSQL (Neon)** – Cloud-based PostgreSQL database for storing user data, reports, and stock analysis.

### Deployment:
- **Railway** – Hosting platform for backend and database management.

### AI & Data Processing:
- **Crew AI** – Multi-agent system for stock analysis and investment recommendations.
- **Yahoo Finance API** – Fetch real-time stock data.
- **Matplotlib & Pandas** – Data visualization and financial data processing.

## Installation & Setup

### Backend Setup (Django)
1. Clone the repository:
   ```sh
   git clone https://github.com/pravincoder/stock_guru.git
   cd stock-guru-ai
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Configure environment variables (`.env`):
   ```sh
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_neon_database_url
   YAHOO_API_KEY=your_yahoo_finance_key
   DJANGO_DEBUG=True
   EMAIL_HOST=smtp.gmail.com
   EMAIL_USE_TLS=True
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```
4. Apply migrations and create a superuser for the admin panel:
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Start the Django server locally:
   ```sh
   python manage.py runserver
   ```
6. **Deployment on Railway:**
   - Push the code to a GitHub repository.
   - Connect the repository to Railway.
   - Set up environment variables in Railway.
   - Deploy the project and access the live platform.

## Usage
- **Access the platform** at `http://localhost:8000` (or Railway-provided URL after deployment)
- **Admin Panel** is available at `http://localhost:8000/admin` (Login with the superuser credentials)
- Users can log in, request stock reports, view past reports, and analyze stock data.

## API Endpoints

### Authentication:
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in a user
- `POST /api/auth/logout/` - Log out the user
- `POST /api/auth/password-reset/` - Reset password
- `POST /api/auth/email-verify/` - Verify user email

### Stock Analysis:
- `GET /api/stocks/analyze/?symbol={symbol}&period={period}` - Fetch stock analysis
- `GET /api/stocks/reports/` - Get user-specific past reports

### Admin:
- `GET /api/admin/requests/` - View all stock requests
- `GET /api/admin/reports/` - View all generated reports

## Future Improvements
- AI-powered stock prediction models.
- Advanced portfolio tracking and alerts.
- Integration with trading platforms.

## License
This project is licensed under the MIT License.

## Contributors
- [Pravincoder](https://github.com/pravincoder) – Developer & AI Engineer

## Contact
For support or collaboration, reach out at [pravincoder@gmail.com].

