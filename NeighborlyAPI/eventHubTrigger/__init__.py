import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):

# Can't be use any more
    logging.info(f"Function triggered to process a message: {event.get_body().decode()}")
    logging.info(f"  EnqueuedTimeUtc = {event.enqueued_time}")
    logging.info(f"  SequenceNumber = {event.sequence_number}")
    logging.info(f"  Offset = {event.offset}")

    result = json.loads(body)
    logging.info("Python EventGrid trigger processed an event: {}".format(result))


    logging.info('Python EventGrid trigger processed an event: %s', result)