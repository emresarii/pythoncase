# Person API

This API provides a simple RESTful web service for managing a list of persons. The API supports retrieving a list of persons, ordered by their creation date, while excluding their phone numbers. The service is implemented using Flask, a popular Python web framework, and returns data in JSON format. The API also includes error handling for bad requests and 404 errors. Overall, this API is designed to be simple to use and provide a basic set of operations for managing a list of persons.


## Getting Started

1- Clone this repository:
```bash
  git clone https://github.com/emresarii/pythoncase
```

2- Change directory to the API directory 
```bash
  cd pythoncase/PersonsApi
```

3- Install the required dependencies:
```bash
  pip install flask==2.0
```

4- Run the application

```bash
  python restPerson.py
```

## API

The API provides the following endpoint:

### GET /persons

#### Get all person data

```http
  GET /persons
```

#### Response Model

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | The unique identifier for the person |
| `firstName` | `string` | The first name of the person. |
| `lastName ` | `string` | The last name of the person. |
| `email ` | `string` | The email address of the person. |
| `createdDate ` | `string` | The date and time the person was created in the format "YYYY-MM-DD HH:MM:SS".|

**Person's "phone" parameter is excluded from response model**


# Error Handling
The API returns appropriate HTTP status codes for both successful and failed requests. JSON-encoded responses are returned for both successful and failed requests.

The API uses the following error codes:

- `400 Bad Request` if there is a problem with the request.
- `404 Not Found` if the requested resource does not exist.
- `500 Internal Server Error` for any internal server errors.

In the case of an error, the response body will contain an `error` field with a description of the problem.
