# Download

****

## Request

**URI** : `/api/download`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

**Request body** : YES

```json
{
  "status": "failure",
  "message": "Request meets validation errors",
  "errors": {
    "email": "email_exists",
    "password": "password_weak"
  }
}
```

## Response

**Code** : `400 Bad Request`

**Content sample**

```json
{
  "status": "failure",
  "message": "Request meets validation errors"
}
```

**Code** : `200 OK`