"""Script to run train job and prediction service.
"""
import typer
import subprocess

app = typer.Typer()

@app.command()
def train():
    """Train the model"""
    from {{ cookiecutter.python_package }} import train
    train.main()

@app.command()
def serve():
    """Serve the model as an API using uvicorn."""
    from {{ cookiecutter.python_package }} import predict
    predict.main()

if __name__ == "__main__":
    app()