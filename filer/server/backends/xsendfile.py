#-*- coding: utf-8 -*-
from django.http import HttpResponse
from filer.server.backends.base import ServerBase


class ApacheXSendfileServer(ServerBase):
    def serve(self, request, file, **kwargs):
        response = HttpResponse()
        response['X-Sendfile'] = file.path
        self.default_headers(request, response, file=file, **kwargs)
        return response
