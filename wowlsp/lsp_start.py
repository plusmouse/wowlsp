from pyls_jsonrpc.dispatchers import MethodDispatcher
from pyls_jsonrpc.endpoint import Endpoint
from pyls_jsonrpc.streams import JsonRpcStreamReader, JsonRpcStreamWriter
from sys import stdin, stdout
import logging

log = logging.getLogger(__name__)


MAX_WORKERS = 64
WOW_FILE_EXTENSIONS = ('.lua', '.xml')


class WoWLanguageServer(MethodDispatcher):
    def __init__(self, read, write):
        self._jsonrpc_stream_reader = JsonRpcStreamReader(read)
        self._jsonrpc_stream_writer = JsonRpcStreamWriter(write)
        self._endpoint = Endpoint(
            self, self._jsonrpc_stream_writer.write, max_workers=MAX_WORKERS)

    def start(self):
        self._jsonrpc_stream_reader.listen(self._endpoint.consume)

    def m_initialize(self, rootUri, capabilities, **_kwargs):
        log.info("init")
        log.info(capabilities)
        return {
            'capabilities': {
                'positionEncodingKind': 'utf-8',
                'textDocumentSync': {
                    'change': 1  # Full
                },
                # 'documentHighlightProvider': True,
                'workspace': {
                    'didChangeWatchedFiles': {
                        'watchers': [
                            {'globPattern': '.wowrc.json'}
                        ]
                    }
                }
            },
            'serverInfo': {
                'name': 'wowlsp',
            }
        }

    def m_shutdown(self, **_kwargs):
        exit()


def start_stdio_server():
    server = WoWLanguageServer(stdin.buffer, stdout.buffer)
    log.info("startup")
    server.start()
