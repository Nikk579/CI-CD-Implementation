from app import app 


## The function should starts with test_ to be recognized by pytest
def test_home():
    response = app.test_client().get('/')

    ## Assert means to check if the condition is true
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Home Page!"}

def test_health_check():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}