
from pathlib import Path
import pandas as pd

app_dir = Path(__file__).parent/'data'
data_lluv = pd.read_csv(app_dir / "data_lluv.csv",index_col="time", parse_dates=True)