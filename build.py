import os
import shutil
import fnmatch
import compileall

BUILD_FOLDER = 'build'

if not os.path.isdir(BUILD_FOLDER):
	print('Creating build directory')
	os.makedirs(BUILD_FOLDER)
else:
	print('Clearing build directory')
	shutil.rmtree(BUILD_FOLDER)

print('Compiling..')
compileall.compile_dir('.', legacy=True, force=True)

print('Moving pyc and pyo files to build folder')


for root, dirnames, filenames in os.walk('.'):
	if '__pycache__' in root:
		continue

	for filename in fnmatch.filter(filenames, '*.pyo'):
		curr_path = os.path.join(root, filename)
		dest_path = './' + BUILD_FOLDER + curr_path[1:-1] + 'c'

		if not os.path.isdir(os.path.dirname(dest_path)):
			os.makedirs(os.path.dirname(dest_path))

		print('Moving {0} -> {1}'.format(curr_path, dest_path ))
		os.rename(curr_path, dest_path)
