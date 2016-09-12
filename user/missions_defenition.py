from missions.mission import Mission
from missions import mission_sort_key

def new_mission(self, mission_name, room_name='first', path_len=10):
	for m in self.missions:
		if m.name == mission_name:
			return
	
	i = 0
	while i < len(self.missions):
		if self.missions[i].path_length == path_len:
			path_len += 1
		elif self.missions[i].path_length >= path_len:
			break

	mission = Mission(mission_name, room_name, path_len)
	self.missions.insert(i, mission)

def get_last_mission(self):
	if len(self.missions) > 0:
		return self.missions[0]
	else:
		return Mission('none', 10 ** 9 + 7) # Cool number!

def pop_mission(self):
	return self.missions.pop(0)