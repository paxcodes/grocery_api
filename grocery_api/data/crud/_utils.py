import json
from pathlib import Path

import aiofiles


def get_new_id(json_data: dict) -> int:
    """Generate a new ID based on existing {json_data}.

    Args:
        json_data (dict): The JSON data with keys as the ID.

    Returns:
        int: An ID a new resource can be assigned to.
    """
    keys = list(json_data.keys())
    if not keys:
        return 1
    last_id = int(keys.pop())
    return last_id + 1


async def read_json_data(json_file: Path) -> dict:
    async with aiofiles.open(json_file) as f:
        file_data = await f.read()
    return json.loads(file_data)


async def write_json_data(json_data: dict, json_file: Path) -> None:
    async with aiofiles.open(json_file, mode="w") as f:
        await f.write(json.dumps(json_data, indent=4))


def convert_tags_to_set(json_data: dict) -> dict:
    serialized_data = {}
    for id, item in json_data.items():
        serialized_data[id] = item
        serialized_data[id]['tags'] = set(item['tags']) if item['tags'] else None
    return serialized_data
    