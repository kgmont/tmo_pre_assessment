# T-Mobile SWE Pre-Assessment

## Install
`pip install -r requirements.txt`

## Run
`python -m flask run`

## Requests
**GET: /api/book**\
*Returns all books currently in DB*

**POST: /api/books**\
*Adds book to DB*

Example JSON:

    {
    	"author": "Douglas Adams",
    	"title": "The Hitchhiker's Guide to the Galaxy",
    	"yearPublished": 1979
    }


**DELETE: /api/book**\
*Deletes all books from DB*