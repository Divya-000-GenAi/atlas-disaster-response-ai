from collections import deque
# Simulated road network. Never use as actual routing or emergency directions.
ROADS={"North Valley":{"Central Hub","East Shelter"},"Central Hub":{"North Valley","West Clinic","South Depot"},"East Shelter":{"North Valley","South Depot"},"West Clinic":{"Central Hub"},"South Depot":{"Central Hub","East Shelter"}}
def shortest_path(start,goal):
    queue=deque([(start,[start])]); seen={start}
    while queue:
        node,path=queue.popleft()
        if node==goal:return path
        for neighbor in sorted(ROADS.get(node,[])):
            if neighbor not in seen:seen.add(neighbor);queue.append((neighbor,path+[neighbor]))
    return []
def allocate(q,level):
    teams=min(q.available_teams,5 if level=="critical" else 3 if level=="high" else 2)
    return {"teams_proposed":teams,"teams_available":q.available_teams,"shelter_capacity_demo":500,"example_route":shortest_path("Central Hub","East Shelter"),"simulation_only":True}
