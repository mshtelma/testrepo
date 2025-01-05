import ray
from ray.util.placement_group import placement_group

ray.init()

pg = placement_group(
    [{"CPU": 1, "GPU": 1}] * 16,  
    strategy="STRICT_SPREAD"       
)

ray.get(pg.ready())