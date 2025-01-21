import pyarrow.parquet as pq
import pyarrow as pa

def write(filename):
    # Create a table with columnar storage
    data = {
        "name": ["John", "Alice", "Bob"],
        "age": [30, 25, 40],
        "salary": [50000, 60000, 70000]
    }
    table = pa.Table.from_pydict(data)

    # Write to Parquet
    pq.write_table(table, filename)

def read(filename):
    # Read Parquet
    table_read = pq.read_table(filename)

    print("Schema:", table_read.schema)
    print("Records:", table_read.to_pydict())

def main():
    filename = "data.parquet"

    write(filename)
    read(filename)

if __name__ == "__main__":
    main()
