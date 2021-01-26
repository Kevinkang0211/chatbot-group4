#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "aa9a8da0-a395-4047-9c3d-9838fc1d9a6c")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "cd7b25b5-973c-436f-a7f6-887047b6dd3a")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://restaurant-recom-qna.azurewebsites.net/qnamaker")