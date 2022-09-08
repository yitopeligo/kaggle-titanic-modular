# Modular Structure of Kaggle Titanic Jupyter Notebook

This Python MLOps application is ready to use with GCP pre-built containers. You can either create custom container or use the source distribution under dist/.

https://cloud.google.com/vertex-ai/docs/training/create-python-pre-built-container?authuser=1&_ga=2.63801327.-1526461848.1661891346

```bash
kaggle-titanic-modular/
├─ dist/
├─ trainer /
│  ├─ data/
│  │  ├─ test.csv
│  │  ├─ outputs/
│  │  ├─ train.csv
│  ├─ KaggleAux/ --> Custom package
│  ├─ data_handler.py
│  ├─ models.py
│  ├─ task.py --> Main module to execute
├─ setup.py
├─ __init__.py
├─ README.md
```
