# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2022 Association Prologin <association@prologin.org>
# Copyright (c) 2022 Marc 'risson' Schmitt <marc.schmitt@prologin.org>

from django.http import HttpResponse
from pypprof.net_http import PProfRequestHandler


class RequestHandler(PProfRequestHandler):
    def __init__(self, request):
        self.query = dict(request.GET.lists())
        self.wfile = HttpResponse()

    def send_response(self, code, message=None):
        self.wfile.status_code = code
        self.wfile.reason_phrase = message

    def send_error(self, code, message=None, explain=None):
        self.wfile.status_code = code
        self.wfile.reason_phrase = f"{message}\n{explain}"

    def send_header(self, keyword, value):
        self.wfile[keyword] = value

    def end_headers(self):
        pass

    def profile(self):
        super().profile(self.query)

    def wall(self):
        super().wall(self.query)

    def heap(self):
        super().heap(self.query)

    def thread(self):
        super().thread(self.query)

    def get_response(self):
        return self.wfile


def index(request):
    handler = RequestHandler(request)
    handler.index()
    return handler.get_response()


def profile(request):
    handler = RequestHandler(request)
    handler.profile()
    return handler.get_response()


def wall(request):
    handler = RequestHandler(request)
    handler.wall()
    return handler.get_response()


def heap(request):
    handler = RequestHandler(request)
    handler.heap()
    return handler.get_response()


def thread(request):
    handler = RequestHandler(request)
    handler.thread()
    return handler.get_response()


def cmdline(request):
    handler = RequestHandler(request)
    handler.cmdline()
    return handler.get_response()
