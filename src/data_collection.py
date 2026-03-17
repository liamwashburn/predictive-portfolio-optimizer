import yfinance as yf # type: ignore
import pandas as pd
from pathlib import Path


def download_market_data(tickers, start="2010-01-01"):

    print("Downloading market data...")

    data = yf.download(tickers, start=start)

    # Extract adjusted close prices
    data = data["Close"]

    return data


def save_data(df):

    output_path = Path("data/raw/market_data.csv")

    df.to_csv(output_path)

    print(f"Data saved to {output_path}")


def main():

    tickers = [
        "SPY",
        "QQQ",
        "VTI",
        "IWM",
        "BND",
        "GLD",
        "VNQ"
    ]

    data = download_market_data(tickers)

    save_data(data)


if __name__ == "__main__":
    main()