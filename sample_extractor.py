import pandas as pd


def extract_sample(input_file, output_file, sample_size=10000):
    print(f"Loading full CSV from {input_file}")
    df = pd.read_csv(input_file)

    sample_df = df.sample(n=sample_size, random_state=42)
    sample_df.to_csv(output_file, index=False)

    print(f"Sample of {sample_size} rows saved to {output_file}")
    return sample_df


#extraction
if __name__ == "__main__":
    input_csv = "D:/etl_agriculture/crop_yield.csv"
    output_csv = "D:/etl_agriculture/sample_crop_yield.csv"
    extract_sample(input_csv, output_csv)

