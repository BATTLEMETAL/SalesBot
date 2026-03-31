"""
SalesBot — Unit Tests
Tests core data processing logic without needing Excel files on disk.
"""
import os
import sys
import pytest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from excel_reader import calculate_totals_by_region, save_data_to_csv


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_sales_df():
    """Minimal DataFrame mimicking output of read_excel_file()."""
    return pd.DataFrame({
        "Region": ["North", "South", "North", "East", "South"],
        "Sales":  [1000.0,  2000.0,  500.0,   750.0,  1500.0],
        "Product": ["A", "B", "A", "C", "B"],
    })


@pytest.fixture
def region_totals(sample_sales_df):
    return calculate_totals_by_region(sample_sales_df).reset_index()


# ---------------------------------------------------------------------------
# calculate_totals_by_region
# ---------------------------------------------------------------------------

class TestCalculateTotalsByRegion:
    def test_returns_series(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert isinstance(result, pd.Series)

    def test_north_total(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert result["North"] == 1500.0

    def test_south_total(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert result["South"] == 3500.0

    def test_east_total(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert result["East"] == 750.0

    def test_all_regions_present(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert set(result.index) == {"North", "South", "East"}

    def test_grand_total(self, sample_sales_df):
        result = calculate_totals_by_region(sample_sales_df)
        assert result.sum() == pytest.approx(5750.0)

    def test_single_region(self):
        df = pd.DataFrame({"Region": ["West", "West"], "Sales": [300.0, 700.0]})
        result = calculate_totals_by_region(df)
        assert result["West"] == 1000.0

    def test_empty_dataframe(self):
        df = pd.DataFrame({"Region": [], "Sales": []})
        result = calculate_totals_by_region(df)
        assert len(result) == 0


# ---------------------------------------------------------------------------
# save_data_to_csv
# ---------------------------------------------------------------------------

class TestSaveDataToCsv:
    def test_creates_file(self, sample_sales_df, tmp_path):
        out = str(tmp_path / "output.csv")
        save_data_to_csv(sample_sales_df, out)
        assert os.path.exists(out)

    def test_csv_has_correct_columns(self, sample_sales_df, tmp_path):
        out = str(tmp_path / "output.csv")
        save_data_to_csv(sample_sales_df, out)
        loaded = pd.read_csv(out)
        assert "Region" in loaded.columns
        assert "Sales" in loaded.columns

    def test_csv_row_count(self, sample_sales_df, tmp_path):
        out = str(tmp_path / "output.csv")
        save_data_to_csv(sample_sales_df, out)
        loaded = pd.read_csv(out)
        assert len(loaded) == len(sample_sales_df)


# ---------------------------------------------------------------------------
# report_generator — smoke test (no PDF written)
# ---------------------------------------------------------------------------

class TestReportGenerator:
    def test_generate_report_does_not_crash(self, region_totals, tmp_path):
        """Verify generate_report() runs end-to-end without raising exceptions."""
        import os
        orig_dir = os.getcwd()
        os.chdir(str(tmp_path))
        try:
            from report_generator import generate_report
            df = region_totals.copy()
            df.columns = ["Region", "Total Sales"]
            generate_report(df)              # writes sales_report.pdf to tmp_path
            assert os.path.exists("sales_report.pdf")
        finally:
            os.chdir(orig_dir)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
