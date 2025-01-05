import ray
from ray.util.placement_group import (
    placement_group,
    placement_group_table,
    remove_placement_group,
)
ray.init()

pg = placement_group(
    [{"CPU": 1, "GPU": 1}] * 16,  
    strategy="SPREAD"       
)

ray.get(pg.ready(), timeout=20)

ready, unready = ray.wait([pg.ready()], timeout=10)

print(placement_group_table(pg))
print("ready ", ready)
print("unready ", unready)