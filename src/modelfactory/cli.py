import typer
from config.config_utils import load_config

app = typer.Typer()

@app.command()
def train(config:str):
    cfg = load_config(config)
    # result = Pipeline(cfg).run()
    # typer.echo(f"Run: {result.best_run_id}")