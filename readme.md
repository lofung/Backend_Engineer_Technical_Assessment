How to start:
1. Main App: start with 
   python main.py
2. Test: run test_app.py

Features:
1. Doctors can be filtered by:
   1. District 
   2. Category
   3. Price range
   4. ~~Spoken languages~~ Feature paused. Need more research on how to filter with this ORM

2. Create doctors

3. Database relationships (Doctors, Categories, Districts)

4. RESTful endpoints

5. Basic testing with pytest

6. Connected to my own test project postgreSQL for easy testing.

Choice of Framework: Flask

Pros: 
   1. Lightweight, quick to set up
   2. Flexible, compared to Django
   3. Good for small projects

Potential Improvements
   1. Add pagination
   2. Add authentication (JWT or OAuth2)
   3. Add input validation
   4. Implement bulk creation of doctors
   5. Research on searching over jsonb

Production Considerations
   1. Use environment variables securely (leaving the database login and password is really only for easy reference and ease of use)
   2. Add rate limiting 
   3. Enable input validation
   4. Add logging and monitoring (e.g. Sentry, Prometheus)

General Assumptions 
   1. No need for authentication 
   2. App will run on a local or internal environment, no need of containerization 
