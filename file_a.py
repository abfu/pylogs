import logging
import file_b


def main():
    logging.basicConfig(filename='multi_mod.log', level=logging.INFO)
    logging.info('Started')
    file_b.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
