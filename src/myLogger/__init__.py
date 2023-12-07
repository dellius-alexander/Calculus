import json
import os
import logging.config
import logging


######################################################################
LOGGING_CONFIG = f"{os.getcwd()}/Resources/logging.json"
######################################################################

# check if logging.json has been loaded
if not logging.root.handlers:
    print(f"Logging config: {LOGGING_CONFIG}")
    print(f"Current Working directory: {os.getcwd()}")
    if not os.path.exists("logs"):
        os.mkdir("logs")
    with open(LOGGING_CONFIG) as file:
        data = json.load(file)
        print(data)
    # read initial config file
    logging.config.dictConfig(config=data)
    # CustomConfig(config=data)
    # # create and start listener on port 9999
    # t = logging.config.listen(int(os.getenv('PORT')))
    # t.start()
    # # wait for listener to be ready
    # t.ready.wait()
    # # connect to listener
    # logging.config.PARENT_CONN = logging.config.connectionClass(t.address)
    # # wait for config to be applied
    # t.ready.wait()
    # # stop listener
    # t.stop()
    # # close connection
    # logging.config.PARENT_CONN.close()
    # # remove handler
    # logging.root.handlers.pop()
    # # add handler
    # logging.root.addHandler(logging.handlers.SocketHandler(t.address))
    # # set level
    # logging.root.setLevel(logging.INFO)
    # # set formatter
    # logging.root.handlers[0].setFormatter(
    #     logging.Formatter(
    #         fmt="[%(asctime)s] [%(levelname)s] [%(name)s][%(lineno)s]: %(message)s",
    #         datefmt="%Y-%m-%d %H:%M:%S",
    #         style="%",
    #     )
    # )

