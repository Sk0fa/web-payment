#!/usr/bin/env python
from migrate.versioning.shell import main

import os

if __name__ == '__main__':
    db_url = f'postgresql://' \
        f'{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'

    main(repository='migrations', url=db_url, debug='False')
