import parser_service

def main():
    """Entry point of the program."""
    parser = parser_service.get_parser()
    args = parser.parse_args()


if __name__ == '__main__':
    main()
