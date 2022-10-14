import logging
import typer

from draw import draw_from_folder
from canny_edge import extract_edges_from_folder
from prompt import draw_prompt

app = typer.Typer()
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(message)s')


@app.command()
def extract_edges(
        input_path: str = typer.Argument(..., help="path to configuration file"),
        output_path: str = typer.Argument(None, help="path to configuration file")):
    if not output_path:
        extract_edges_from_folder(input_path, input_path)
    else:
        extract_edges_from_folder(input_path, output_path)


@app.command()
def draw_edges(
        input_path: str = typer.Argument(..., help="path to configuration file"),
        output_path: str = typer.Argument(None, help="path to configuration file"),
        brushes_path: str = typer.Argument(..., help="path to configuration file")):
    if not output_path:
        draw_from_folder(input_path, input_path, brushes_path)
    else:
        draw_from_folder(input_path, output_path, brushes_path)


@app.command()
def prompt(
        prompt_path: str = typer.Argument(..., help="path to prompt file"),
        combination: int = typer.Argument(1, help="number of prompts to draw")):
    prompts = draw_prompt(prompt_path, combination)
    str_prompts = " ".join(prompts)
    logger.info(f"you have drawn : {str_prompts}")


if __name__ == '__main__':
    app()
