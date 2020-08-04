"""Sending main data results to Slack: Function called by PubSub trigger to execute cron job tasks."""

import datetime
import logging
from string import Template
import config
from google.cloud import bigquery
import requests
import simplejson as json


def file_to_string(sql_path):
    """
    Converts a SQL file holding a SQL query to a string.
    sql_path: String containing a file path
    Returns String representation of a file's contents
    """

    #open a file for r reading
    with open(sql_path, 'r') as sql_file:
        return sql_file.read()


def execute_query(bq_client):
    """
    Executes transformation query to a new destination table.
    bq_client: Object representing a reference to a BigQuery Client
    """

    dataset_ref = bq_client.get_dataset(bigquery.DatasetReference(
        project=config.config_vars['project_id'],
        dataset_id=config.config_vars['output_dataset_id']))

    ##1
    table_ref = dataset_ref.table(config.config_vars['output_table_name'])
    job_config = bigquery.QueryJobConfig()
    job_config.destination = table_ref
    job_config.write_disposition = bigquery.WriteDisposition().WRITE_TRUNCATE

    sql = file_to_string(config.config_vars['sql_file_path'])
    logging.info('Attempting query on all dates...')

    # Execute Query
    query_job = bq_client.query(
        sql,
        job_config=job_config)

    results = query_job.result()
    logging.info('Query complete. The table is updated.')

    def temp_func(apple):
        list = []
        for row in apple:
            list.append("*설명서 링크:* https://bit.ly/35l1Elv\n*시작 날짜:* {}\n*Round:* {}\n*RU:* {}\n*DAU:* {}\n*NU:* {}\n*PU:* {}\n*Purchases:* {}\n*Revenue:* {} IDR\n*ARPDAU:* {} IDR\n*ARPPU:* {} IDR".format(row.date_timestamp, row.row_count, row.RU, row.DAU, row.NU, row.PU, row.Purchases, round(row.Revenue_IDR, 0), round(row.ARPDAU_IDR, 0), round(row.ARPPU_IDR),0))
        return(list)

    ##slack
    url = "https://hooks.slack.com/services/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"
    data = {
    'auth_token': 'auth1',
    'widget': 'id1',
    'title': 'Something1',
    'text': str(temp_func(results)[0]),
    'moreinfo': 'Subtitle'}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

def main(data, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        data (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    bq_client = bigquery.Client()

    try:
        current_time = datetime.datetime.utcnow()
        log_message = Template('Cloud Function was triggered on $time')
        logging.info(log_message.safe_substitute(time=current_time))

        try:
            execute_query(bq_client)

        except Exception as error:
            log_message = Template('Query failed due to '
                                   '$message.')
            logging.error(log_message.safe_substitute(message=error))

    except Exception as error:
        log_message = Template('$error').substitute(error=error)
        logging.error(log_message)

if __name__ == '__main__':
    main('data', 'context')
