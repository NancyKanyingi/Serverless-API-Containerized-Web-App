
import base64
import json
import logging
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Receive a JSON submission through API Gateway."""

    if event.get("httpMethod") == "OPTIONS":
        return response(200, {"message": "CORS preflight successful"})

    try:
        body = event.get("body") or "{}"

        if event.get("isBase64Encoded"):
            body = base64.b64decode(body).decode("utf-8")

        if isinstance(body, str):
            payload = json.loads(body)
        else:
            payload = body

        logger.info("Received data: %s", json.dumps(payload))

        reference_id = str(uuid.uuid4())

        return response(
            200,
            {
                "message": "Submission received successfully",
                "referenceId": reference_id
            }
        )

    except (json.JSONDecodeError, ValueError) as exc:
        logger.warning("Invalid submission: %s", str(exc))
        return response(400, {"message": "Invalid JSON payload"})


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps(body)
    }
