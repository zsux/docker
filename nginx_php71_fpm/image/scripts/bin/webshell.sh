#!/usr/bin/env bash
rm -rf /usr/local/bin/butterfly.server.pyc
rm -rf /usr/lib/python2.7/site-packages/butterfly/__init__.pyc
sed  -i 's/, ssl_options=ssl_opts)/, ssl_options=ssl_opts,xheaders=True)/g' /usr/local/bin/butterfly.server.py
sed  -i "s/import os/import os\nfrom tornado.auth import AuthError\nfrom tornado_http_auth import BasicAuthMixin\ncredentials = {'$1': '$2'}/g" /usr/lib/python2.7/site-packages/butterfly/__init__.py
sed  -i 's/tornado.web.RequestHandler)/tornado.web.RequestHandler,BasicAuthMixin)/g' /usr/lib/python2.7/site-packages/butterfly/__init__.py
sed  -i "s/BasicAuthMixin):/BasicAuthMixin):\n    def prepare(self):\n        self.get_authenticated_user(check_credentials_func=credentials.get, realm='Protected')/g" /usr/lib/python2.7/site-packages/butterfly/__init__.py
