import ray
from ray.util.placement_group import (
    placement_group,
    placement_group_table,
)
from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy
from vllm import LLM, SamplingParams

ray.init()

pg = placement_group(
    [{"CPU": 1, "GPU": 1}] * 16,
    strategy="SPREAD"
)

ray.get(pg.ready(), timeout=60 * 10)

ready, unready = ray.wait([pg.ready()], timeout=10)

print(placement_group_table(pg))
print("ready ", ready)
print("unready ", unready)


@ray.remote(num_cpus=1)
class Actor:
    def __init__(self):
        import torch.distributed as dist
        dist.init_process_group(backend='nccl', rank=0, world_size=16)

        self.llm = LLM(model="/model", tensor_parallel_size=16)

    def generate(self):
        sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
        outputs = self.llm.generate(["What is ML?"], sampling_params)
        return outputs[0].outputs[0].text


actor = Actor.options(
    scheduling_strategy=PlacementGroupSchedulingStrategy(placement_group=pg, )
).remote()

ray.get(actor.generate.remote(), timeout=100000)
