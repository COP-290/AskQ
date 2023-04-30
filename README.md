# AskQ: A forum to **ask** **q**uestions and get answers

## Backend: Inside folder `flask_blog`

- Redirects from `main_.py`
- APIs for ML in `api.py`
- APIs for Questions in `question.py`
- APIs for Tags in `tag.py`
- APIs for Users in `user.py`
- APIs for Particular Question in `particular_question.py`

## Frontend: Inside folder `frontend`
Components inside `frontend/src/components`

## Unit and Integration Tests: Inside folder `test`
1. Frontend Integration test in `.github/workflows/frontend.yaml`
2. Python Unit and Integration Tests:
    - Tests related to `X` in `test_X.py` where `X` in {`user`,`tag`,`question`,`particular_question`}