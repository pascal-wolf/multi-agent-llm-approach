from pipeline import read_data, clean, embedding_creation, write_database, consolidation
import time

if __name__ == "__main__":
    sources = ["chatgpt", "netflix", "spotify"]
    RUN_OLD_PIPELINE = False
    start = time.time()
    for source in sources:
        print(f"Reading data from {source}")
        df = read_data(source)
        df = consolidation(df, source)
        df = clean(df, RUN_OLD_PIPELINE, source)
        df = embedding_creation(df)
        write_database(df, source)
        print(f"Data from {source} written to database")

    print(f"Pipeline completed in {time.time() - start} seconds")