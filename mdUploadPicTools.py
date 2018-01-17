# -*- encoding: utf-8 -*-
import os
import sys
import glob
from qiniu import Auth, put_file
import qiniu.config

url_header = 'ozefmlquu.bkt.clouddn.com'

access_key = 'cRXononyP_ZDVinaki_QwT3APKifzO_2YafKj9HH'
secret_key = '6IMkQGY8xaF0ZeHWSqba2_jweSaNsJ0xqbYhfmfh'

def uploadPic(file, workdir):
	q = Auth(access_key, secret_key)
	bucket_name = 'image'
	remote_file_name = 'images/%s' % (file)
	token = q.upload_token(bucket_name, remote_file_name, 3600)
	localfile = '%s/%s' % (workdir, file)
	ret, info = put_file(token, remote_file_name, localfile)
	return remote_file_name

if __name__ == '__main__':
	file = sys.argv[1]
	if not os.path.isabs(file):
		file = os.path.realpath(file)
	workdir = os.path.dirname(file)
	pictures = glob.glob('%s/*.jpg' % (workdir))
	pictures = [os.path.basename(pic) for pic in pictures]
	url_dict = {picname:'http://%s/%s' % (url_header, uploadPic(picname, workdir)) for picname in pictures}
	with open(file, 'a', encoding = 'utf-8') as f:
		for key in url_dict.keys():
			f.write('\n[%s]:%s' % (os.path.splitext(key)[0], url_dict[key]))