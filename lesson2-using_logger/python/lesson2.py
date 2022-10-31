import logging
from cmreslogging.handlers import CMRESHandler

handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="talmundo-logs",
                           es_additional_fields={'Platform': 'Talentech', 'Solution': 'Workshop', 'AppName': 'Lesson2', 'Environment': 'Local'})
log = logging.getLogger("PythonTest")
log.setLevel(logging.INFO)
log.addHandler(handler)

log.info("Hello World!")
# log.debug("Hello World!", extra={'db_execution_time': db_delta})