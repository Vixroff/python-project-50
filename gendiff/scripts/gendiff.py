import argparse


from gendiff.generate_diff import generate_diff


def parser_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help='set format of output')
    parser.parse_args()
    args = parser.parse_args()
    return args


def main():
    args = parser_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
