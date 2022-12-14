def get_sub(name):
    return ('''resource "google_pubsub_topic" "{0}" {{
  name = "{0}-${{var.stage}}"
}}

resource "google_pubsub_subscription" "{0}" {{
  name  = "{0}-sub-${{var.stage}}"
  topic = google_pubsub_topic.{0}.name

  ack_deadline_seconds = 20
}}

''').format(name)
