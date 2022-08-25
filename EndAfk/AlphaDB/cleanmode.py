from . import db

cmdb = db.cm

async def sce(_: int):
    enabled = cmdb.find_one({"_": _})
    if enabled:
        return
    return await cmdb.insert_one({"_": _})

async def scd(_: int):
    enabled = cmdb.find_one({"_": _})
    if not enabled:
        return
    return await cmdb.delete_one({"_": _})

async def cme(_: int):
    enabled = cmdb.find_one({"_": _})
    if enabled:
        return True
    return False
    
