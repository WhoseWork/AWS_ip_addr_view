from datetime import datetime
import logging

# logger create and loglevel setting.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# main code
def lambda_handler(event, context):

    # data generation for response (dictionary type)
    rtn_json = {"statusCode":"200", "urGlobalIPv4": str(event.get('source_ip')), "accessDate": str(datetime.utcnow().isoformat())}

    # Route53 A record update

    # write execution logs to Cloudwatch
    logger.info(rtn_json)

    # response
    return rtn_json

