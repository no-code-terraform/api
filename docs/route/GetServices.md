# Get Services

****

## Request

**URI** : `/api/services`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : NO

**Request body** : NO

## Response

**Code** : `200 OK`

**Content sample**

```json
{
  "status": "success",
  "message": "OK",
  "data": {
    "services": [
      {
        "name": "Amason EC2",
        "provider": "aws",
        "type": "compute",
        "description": "Amazon Elastic Compute Cloud (Amazon EC2) offers the broadest and deepest compute platform.",
        "url": "https://aws.amazon.com/ec2/",
        "tf_key": "ec2",
        "extra": [
          {
            "max": null,
            "min": null,
            "name": "ami",
            "type": "string",
            "choices": null,
            "default": null,
            "is_required": null,
            "is_multiple_choice": null
          }
        ]
      }
    ]
  }
}
```