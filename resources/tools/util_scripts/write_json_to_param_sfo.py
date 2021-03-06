import os
import json
from global_paths import App as AppPaths

class Write_param_sfo():
	def execute(self):
		# common paths
		try:
			with open(os.path.join(AppPaths.wcm_work_dir, 'pkg.json')) as f:
				json_data = json.load(f)

			title = json_data['title']
			title_id = json_data['title_id']

			dummy_title_array = b'\x00'*128
			title = str(title) + dummy_title_array[len(title):]

			dummy_title='PKG/ROM Launcher'

			# load backup
			with open(os.path.join(AppPaths.util_resources, 'PARAM.SFO.BAK'), 'rb') as f:
				file = f.read()
				f.close()

				try:
					# add title
					start_index_title = file.find(dummy_title)
					print('DEBUG: ' + str(file[888:1025]))
					file=file[0:start_index_title]+str(title)+file[start_index_title+len(title):]

					# add title_id
					max_pos_title_id = 1025
					file=file[0:max_pos_title_id-len(str(title_id))]+str(title_id)+file[max_pos_title_id:]
					print('DEBUG: ' + str(file[start_index_title:1025]))

					# write to generated files
					newFile = open(os.path.join(AppPaths.pkg, 'PARAM.SFO'), 'wb')
					newFileByteArray = bytearray(file)
					newFile.write(newFileByteArray)

					print('\n\nExecution of \'write_json_to_param_sfo.py\': Done')
					print('-----------------------------------------------')

				except ValueError:
					print('File write error / \'PKGLAUNCH\' not found / \'title_id\' not a string')
		except Exception as e:
			print(e)