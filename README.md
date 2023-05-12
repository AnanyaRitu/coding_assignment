# coding_assignment

## User Registration:
http://127.0.0.1:8000/api/v1/registration/
<br>
Method: POST  
<br>
requires email and password in the body

## User Login:
http://127.0.0.1:8000/api/token/
<br>
Method: POST  
<br>
requires email and password in the body
<br>
It will provide an access token and refresh token. This access token is required for authentication in all the apis other than the registration api.

## Sales
### lists all the sales record
 "http://127.0.0.1:8000/api/v1/sales/"
 <br>
 Method: GET

### retrieves specific sales record
 "http://127.0.0.1:8000/api/v1/sales/<:id>/"
 <br>
 Method: GET
 
### creates new sales record
 "http://127.0.0.1:8000/api/v1/sales/"
 <br>
 Method: POST
 
### updates specific the sales record
 "http://127.0.0.1:8000/api/v1/sales/<:id>"
 <br>
 Method: PUT
