"""
sentry_freight.plugin
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2015 by Sentry Team, see AUTHORS for more details.
:license: Apache 2.0, see LICENSE for more details.
"""

import json

import sentry_freight

from sentry.plugins import ReleaseHook, ReleaseTrackingPlugin

DOC_HTML = """
<p>Configure a Freight notification with the given webhook url.</p>
<pre class="clippy">{{
    "type": "sentry",
    "config": {{"webhook_url": "{hook_url}"}}
}}</pre>
"""


class FreightReleaseHook(ReleaseHook):
    def handle(self, request):
        data = json.loads(request.body)
        if data['event'] == 'started':
            self.start_release(
                version=data['sha'],
                ref=data['ref'],
                url=data['link'],
            )
        elif data['event'] == 'finished':
            self.finish_release(
                version=data['sha'],
                ref=data['ref'],
                url=data['link'],
            )
        else:
            raise ValueError(data['event'])


class FreightPlugin(ReleaseTrackingPlugin):
    author = 'Sentry Team'
    author_url = 'https://github.com/getsentry'
    resource_links = (
        ('Bug Tracker', 'https://github.com/getsentry/sentry-freight/issues'),
        ('Source', 'https://github.com/getsentry/sentry-freight'),
    )

    title = 'Freight'
    slug = 'freight'
    description = 'Integrate Freight release tracking.'
    version = sentry_freight.VERSION

    def has_plugin_conf(self):
        return True

    def get_release_doc_html(self, hook_url):
        return DOC_HTML.format(hook_url=hook_url)

    def get_release_hook(self):
        return FreightReleaseHook
