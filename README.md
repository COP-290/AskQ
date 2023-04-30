# AskQ: A forum to ask questions and get answers

## Backend: Inside folder `flask_blog`

- Redirects from `main_.py`
- APIs for ML in `api.py`
- APIs for Questions in `question.py`
- APIs for Tags in `tag.py`
- APIs for Users in `user.py`
- APIs for Particular Question in `particular_question.py`

## Frontend: Inside folder `frontend`
Created using ReactJS and Bootstrap
Components inside `frontend/src/components`
- Home page in `main.js`
- Navbar in `navbar.js`
- Questions page in `question.js`
- Tags page in `tag.js`
- Particular Question page in `particular_question.js`
- Search page in `search.js`
- New Question page in `new_question.js`
- Profile page in `profile.js`
- Login page in `login.js`
- Signup page in `signup.js`
- All users page in `users_page.js`
- User page in `par_user.js`
- 404 page in `404.js`
- About page in `about.js`

## Unit and Integration Tests: Inside folder `test`
1. Frontend Integration test in `.github/workflows/frontend.yaml`
2. Python Unit and Integration Tests:
    - Tests related to `X` in `test_X.py` where `X` in (`user`,`tag`,`question`,`particular_question`)