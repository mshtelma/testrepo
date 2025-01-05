import ray
from ray.util.placement_group import placement_group

ray.init()

pg = placement_group(
    [{"CPU": 1, "GPU": 1}] * 16,  
    strategy="SPREAD"       
)

ray.get(pg.ready())