def objid_str(item):
    if "_id" in item:
        item["_id"] = str(item["_id"])
    return item