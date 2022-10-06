# Build TF

****

## Request

**URI** : `/api/tf/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

**Request body** : YES

```json
{
  "stages": [
    "production",
    "staging"
  ],
  "providers": {
    "aws": {
      "region": "us-east-2",
      "services": {
        "instances": [
          {
            "ami": "ami-085925f297f89fce1",
            "instance_type": "t2.micro",
            "ports": [
              8080
            ],
            "count": 1
          }
        ],
        "loadBalancers": [
          {
            "availability_zones": [
              "eu-west-2a"
            ],
            "name-elb": "my-load-balancer",
            "instances": "aws_instance.application.*.id",
            "cross_zone_load_balancing": true,
            "idle_timeout": "400",
            "connection_draining": true,
            "connection_draining_timeout": "400",
            "listeners": {
              "instance_port": "8080",
              "instance_protocol": "HTTP",
              "lb_port": "80",
              "lb_protocol": "HTTP"
            },
            "healthCheck": {
              "healthy_threshold": "2",
              "unhealthy_threshold": "2",
              "timeout": "3",
              "target": "HTTP:8080/api/healthcheck",
              "interval": "30"
            }
          }
        ]
      }
    },
    "gcp": {
      "region": "europe-west9-a",
      "project": "notional-yeti-343410",
      "services": {
        "messaging": [
          {
            "topic": "test-topic"
          }
        ]
      }
    }
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