from . import lsp_start
import logging

log = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='wowlsp.log', level=logging.INFO)
    lsp_start.start_stdio_server()


if __name__ == '__main__':
    main()
