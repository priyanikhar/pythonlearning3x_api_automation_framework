#contains common utilities
#read data from excel file
#read data from the csv file
# set the headers- application /json,application/xml

class Utils(object):
    def common_headers_json(self):
       headers = {
           "Content-Type": "application/json"
       }
       return headers
    def common_headers_xml(self):
       headers = {
           "Content-Type": "application/xml"
       }
       return headers

    def common_headers_put_delete_patch_cookie(self,token):
       headers = {
           "Content-Type": "application/json",
           "Cookie": "token=" + str(token),
       }
       return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass