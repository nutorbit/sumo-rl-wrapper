import gym
import numpy as np

from sumo_rl import SumoEnvironment


def main():
    env = SumoEnvironment(
        # net_file='/Users/nutorbit/workspace/sumo/sumo/map/2way-single-intersection/single-intersection.net.xml',
        # route_file='/Users/nutorbit/workspace/sumo/sumo/map/2way-single-intersection/single-intersection-gen.rou.xml',
        net_file="test/osm.net.xml",
        route_file="test/routes.rou.xml",
        use_gui=True,
        single_agent=False,
        num_seconds=3600,
    )
    
    obs = env.reset()

    print("Number of traffic light:", len(env.ts_ids))
    
    done = False

    while True:
        actions = {
            key: env.traffic_signals[key].action_space.sample() for key in env.ts_ids
        }
        obs, rew, done, info = env.step(actions)
        print("Actions:", actions, sep="\n")
        print("Obs:", obs, sep="\n")


if __name__ == "__main__":
    main()
