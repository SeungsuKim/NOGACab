import os
import subprocess

class obj():

	def __init__(self, name, pos):
		self.name = name
		# Left, Top, Right, Bottom
		self.pos = pos

	def __str__(self):
		return self.name + ": " + str(self.pos)

	def getMid(self):
		pass


if __name__ == "__main__":
	os.chdir("./darknet")
	result = subprocess.run(["./darknet", "detect", "cfg/yolov3.cfg", "yolov3.weights", "data/NOGACab/samples/sample_night7.jpg"],
		                    stdout=subprocess.PIPE)
	if result.returncode != 0:
		print(result.stderr)
	else:
		objects = []

		output = result.stdout.decode('utf-8')
		lines = output.splitlines()[1:]
		for i in range(0, len(lines), 2):
			name = lines[i].split()[0][:-1]
			pos = list(map(int, lines[i+1].split()))
			objects.append(obj(name, pos))

		for obj in objects:
			print(obj)