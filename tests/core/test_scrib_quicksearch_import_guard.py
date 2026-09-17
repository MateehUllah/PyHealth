import ast
from pathlib import Path


def test_scrib_quicksearch_only_catches_import_error():
    source_path = (
        Path(__file__).parents[2]
        / "pyhealth"
        / "calib"
        / "predictionset"
        / "scrib"
        / "quicksearch.py"
    )
    module = ast.parse(source_path.read_text())
    import_guard = next(node for node in module.body if isinstance(node, ast.Try))

    assert len(import_guard.handlers) == 1
    handler = import_guard.handlers[0]
    assert isinstance(handler.type, ast.Name)
    assert handler.type.id == "ImportError"
