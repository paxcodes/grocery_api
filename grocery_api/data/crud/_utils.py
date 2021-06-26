def get_new_id(json_data: dict) -> int:
    """Generate a new ID based on existing {json_data}.

    Args:
        json_data (dict): The JSON data with keys as the ID.

    Returns:
        int: An ID a new resource can be assigned to.
    """
    keys = list(json_data.keys())
    last_id = int(keys.pop())
    return last_id + 1
