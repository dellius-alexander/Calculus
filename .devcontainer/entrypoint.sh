#!/bin/bash
# -*- coding: utf-8 -*-
intro="""
This entrypoint script @ /entrypoint is used to start the server in the container.
It can be used to provide custom configuration options during server startup.
It can also be used to run tests, linting, etc. before starting the server.

Current Working Directory: $(pwd)
"""
printf "$intro"
cd /app
python3 -m __main__ --config /app/resources/config.yaml
