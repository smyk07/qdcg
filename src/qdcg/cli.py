import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="qdcg",
        description="Queryable Code Dependency Graph",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    index_parser = subparsers.add_parser("index")
    index_parser.add_argument("path")

    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("query")

    args = parser.parse_args()

    match args.command:
        case "index":
            print(f"Indexing {args.path}")

        case "query":
            print(f"Query: {args.query}")
