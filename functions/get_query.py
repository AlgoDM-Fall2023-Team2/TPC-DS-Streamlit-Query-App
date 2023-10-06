# read query file
def read_query(query_file_path) -> str:
    file = open(query_file_path, "r")
    query: str = file.read()
    return query
