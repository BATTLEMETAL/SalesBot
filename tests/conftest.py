"""
conftest.py — pytest session-level setup.
Forces matplotlib into non-interactive Agg backend so tests
run cleanly on headless CI servers (Ubuntu / GitHub Actions).
Must be imported before any code that calls matplotlib.pyplot.
"""
import matplotlib
matplotlib.use("Agg")
