from gendiff.cli_parser import parser_args
from gendiff.generate_diff import generate_diff


def main():
    args = parser_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
