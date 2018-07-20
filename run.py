import os
import sys


def main():
    deployment_env = os.getenv('DEPLOYMENT_ENV', 'dev').lower()

    config = None
    if deployment_env in ('dev', 'development'):
        try:
            import config_dev as config
        except ImportError:
            pass
    elif deployment_env in ('test', 'testing'):
        try:
            import config_test as config
        except ImportError:
            pass
    elif deployment_env in ('prod', 'production'):
        try:
            import config_prod as config
        except ImportError:
            try:
                import config
            except ImportError:
                pass

    if config is None:
        print('There is no configuration file!', file=sys.stderr)
        exit(1)

    import maruko
    app = maruko.init(config)
    app.run(host=config.HOST, port=config.PORT)


if __name__ == '__main__':
    main()
