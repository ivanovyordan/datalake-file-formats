import avro.schema
import avro.datafile
import avro.io

def write(filename):
    # Define AVRO schema
    schema_str = """{
        "type": "record",
        "name": "Employee",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "int"},
            {"name": "salary", "type": "float"}
        ]
    }"""
    schema = avro.schema.parse(schema_str)

    # Create an AVRO file
    with open(filename, "wb") as out_file:
        writer = avro.datafile.DataFileWriter(out_file, avro.io.DatumWriter(), schema)
        writer.append({"name": "John", "age": 30, "salary": 50000.0})
        writer.close()

def read(filename):
    # Read and print AVRO schema
    with open(filename, "rb") as in_file:
        reader = avro.datafile.DataFileReader(in_file, avro.io.DatumReader())

        print("Schema:", reader.meta.get("avro.schema").decode("utf-8"))

        for record in reader:
            print("Record:", record)

        reader.close()


def main():
    filename = "data.avro"

    write(filename)
    read(filename)

if __name__ == "__main__":
    main()
